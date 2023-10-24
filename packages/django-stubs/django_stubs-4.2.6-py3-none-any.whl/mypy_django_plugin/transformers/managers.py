from typing import Final, Optional, Union

from mypy.checker import TypeChecker
from mypy.nodes import (
    GDEF,
    CallExpr,
    Decorator,
    FuncBase,
    FuncDef,
    MemberExpr,
    Node,
    OverloadedFuncDef,
    RefExpr,
    StrExpr,
    SymbolTableNode,
    TypeInfo,
    Var,
)
from mypy.plugin import AttributeContext, ClassDefContext, DynamicClassDefContext
from mypy.semanal import SemanticAnalyzer
from mypy.semanal_shared import has_placeholder
from mypy.types import AnyType, CallableType, FunctionLike, Instance, Overloaded, ProperType, TypeOfAny, TypeVarType
from mypy.types import Type as MypyType
from mypy.typevars import fill_typevars

from mypy_django_plugin.lib import fullnames, helpers

MANAGER_METHODS_RETURNING_QUERYSET: Final = frozenset(
    (
        "alias",
        "all",
        "annotate",
        "complex_filter",
        "defer",
        "difference",
        "distinct",
        "exclude",
        "extra",
        "filter",
        "intersection",
        "none",
        "only",
        "order_by",
        "prefetch_related",
        "reverse",
        "select_for_update",
        "select_related",
        "union",
        "using",
    )
)


def get_method_type_from_dynamic_manager(
    api: TypeChecker, method_name: str, manager_instance: Instance
) -> Optional[ProperType]:
    """
    Attempt to resolve a method on a manager that was built from '.from_queryset'
    """

    manager_type_info = manager_instance.type.get_containing_type_info(method_name)

    if (
        manager_type_info is None
        or "django" not in manager_type_info.metadata
        or "from_queryset_manager" not in manager_type_info.metadata["django"]
    ):
        # Manager isn't dynamically added
        return None

    queryset_fullname = manager_type_info.metadata["django"]["from_queryset_manager"]
    assert isinstance(queryset_fullname, str)
    queryset_info = helpers.lookup_fully_qualified_typeinfo(api, queryset_fullname)
    assert queryset_info is not None

    is_fallback_queryset = queryset_info.metadata.get("django", {}).get("any_fallback_queryset", False)

    base_that_has_method = queryset_info.get_containing_type_info(method_name)
    if base_that_has_method is None:
        return None
    method_type = _get_funcdef_type(base_that_has_method.names[method_name].node)
    if not isinstance(method_type, FunctionLike):
        return method_type

    items = []
    for item in method_type.items:
        items.append(
            _process_dynamic_method(
                method_name,
                item,
                base_that_has_method=base_that_has_method,
                queryset_info=queryset_info,
                manager_instance=manager_instance,
                is_fallback_queryset=is_fallback_queryset,
            )
        )
    return Overloaded(items) if len(items) > 1 else items[0]


def _process_dynamic_method(
    method_name: str,
    method_type: CallableType,
    *,
    queryset_info: TypeInfo,
    base_that_has_method: TypeInfo,
    manager_instance: Instance,
    is_fallback_queryset: bool,
) -> CallableType:
    variables = method_type.variables
    ret_type = method_type.ret_type

    # For methods on the manager that return a queryset we need to override the
    # return type to be the actual queryset class, not the base QuerySet that's
    # used by the typing stubs.
    if method_name in MANAGER_METHODS_RETURNING_QUERYSET:
        if not is_fallback_queryset:
            ret_type = Instance(queryset_info, manager_instance.args)
        else:
            # The fallback queryset inherits _QuerySet, which has two generics
            # instead of the one exposed on QuerySet. That means that we need
            # to add the model twice. In real code it's not possible to inherit
            # from _QuerySet, as it doesn't exist at runtime, so this fix is
            # only needed for pluign-generated querysets.
            ret_type = Instance(queryset_info, [manager_instance.args[0], manager_instance.args[0]])
        variables = []
    args_types = method_type.arg_types[1:]
    if _has_compatible_type_vars(base_that_has_method):
        typed_var = manager_instance.args or queryset_info.bases[0].args
        if (
            typed_var
            and isinstance(typed_var[0], Instance)
            and typed_var[0].type.has_base(fullnames.MODEL_CLASS_FULLNAME)
        ):
            ret_type = _replace_type_var(ret_type, base_that_has_method.defn.type_vars[0].fullname, typed_var[0])
            args_types = [
                _replace_type_var(arg_type, base_that_has_method.defn.type_vars[0].fullname, manager_instance.args[0])
                for arg_type in args_types
            ]
    if base_that_has_method.self_type:
        # Manages -> Self returns
        ret_type = _replace_type_var(ret_type, base_that_has_method.self_type.fullname, manager_instance)

    # Drop any 'self' argument as our manager is already initialized
    return method_type.copy_modified(
        arg_types=args_types,
        arg_kinds=method_type.arg_kinds[1:],
        arg_names=method_type.arg_names[1:],
        variables=variables,
        ret_type=ret_type,
    )


def _get_funcdef_type(definition: Union[Node, None]) -> Optional[ProperType]:
    if isinstance(definition, FuncBase):
        return definition.type
    elif isinstance(definition, Decorator):
        return definition.func.type
    return None


def _has_compatible_type_vars(type_info: TypeInfo) -> bool:
    """
    Determines whether the provided 'type_info',
    is a generically parameterized subclass of models.QuerySet[T], with exactly
    one type variable.

    Criteria for compatibility:
    1. 'type_info' must be a generic class with exactly one type variable.
    2. All superclasses of 'type_info', up to and including models.QuerySet,
       must also be generic classes with exactly one type variable.

    Examples:

    Compatible:
        class _MyModelQuerySet(models.QuerySet[T]): ...
        class MyModelQuerySet(_MyModelQuerySet[T_2]):
            def example(self) -> T_2: ...

    Incompatible:
        class MyModelQuerySet(models.QuerySet[T], Generic[T, T2]):
            def example(self, a: T2) -> T_2: ...

    Returns:
        True if the 'base' meets the criteria, otherwise False.
    """
    args = type_info.defn.type_vars
    if not args or len(args) > 1 or not isinstance(args[0], TypeVarType):
        # No type var to manage, or too many
        return False
    type_var: Optional[MypyType] = None
    # check that for all the bases it has only one type vars
    for sub_base in type_info.bases:
        unic_args = list(set(sub_base.args))
        if not unic_args or len(unic_args) > 1:
            # No type var for the sub_base, skipping
            continue
        if type_var and unic_args and type_var != unic_args[0]:
            # There is two different type vars in the bases, we are not compatible
            return False
        type_var = unic_args[0]
    if not type_var:
        # No type var found in the bases.
        return False

    if type_info.has_base(fullnames.QUERYSET_CLASS_FULLNAME):
        # If it is a subclass of _QuerySet, it is compatible.
        return True
    # check that at least one base is a subclass of queryset with Generic type vars
    return any(_has_compatible_type_vars(sub_base.type) for sub_base in type_info.bases)


def _replace_type_var(ret_type: MypyType, to_replace: str, replace_by: MypyType) -> MypyType:
    """
    Substitutes a specified type variable within a Mypy type expression with an actual type.

    This function is recursive, and it operates on various kinds of Mypy types like Instance,
    ProperType, etc., to deeply replace the specified type variable.

    Parameters:
    - ret_type: A Mypy type expression where the substitution should occur.
    - to_replace: The type variable to be replaced, specified as its full name.
    - replace_by: The actual Mypy type to substitute in place of 'to_replace'.

    Example:
    Given:
        ret_type = "typing.Collection[T]"
        to_replace = "T"
        replace_by = "myapp.models.MyModel"
    Result:
        "typing.Collection[myapp.models.MyModel]"
    """
    if isinstance(ret_type, TypeVarType) and ret_type.fullname == to_replace:
        return replace_by
    elif isinstance(ret_type, Instance):
        # Since it is an instance, recursively find the type var for all its args.
        ret_type.args = tuple(_replace_type_var(item, to_replace, replace_by) for item in ret_type.args)
    if isinstance(ret_type, ProperType) and hasattr(ret_type, "item"):
        # For example TypeType has an item. find the type_var for this item
        ret_type.item = _replace_type_var(ret_type.item, to_replace, replace_by)
    if isinstance(ret_type, ProperType) and hasattr(ret_type, "items"):
        # For example TypeList has items. find recursively type_var for its items
        ret_type.items = [_replace_type_var(item, to_replace, replace_by) for item in ret_type.items]
    return ret_type


def resolve_manager_method_from_instance(instance: Instance, method_name: str, ctx: AttributeContext) -> MypyType:
    api = helpers.get_typechecker_api(ctx)
    method_type = get_method_type_from_dynamic_manager(api, method_name, instance)
    return method_type if method_type is not None else ctx.default_attr_type


def resolve_manager_method(ctx: AttributeContext) -> MypyType:
    """
    A 'get_attribute_hook' that is intended to be invoked whenever the TypeChecker encounters
    an attribute on a class that has 'django.db.models.BaseManager' as a base.
    """
    # Skip (method) type that is currently something other than Any of type `implementation_artifact`
    if not isinstance(ctx.default_attr_type, AnyType):
        return ctx.default_attr_type
    elif ctx.default_attr_type.type_of_any != TypeOfAny.implementation_artifact:
        return ctx.default_attr_type

    # (Current state is:) We wouldn't end up here when looking up a method from a custom _manager_.
    # That's why we only attempt to lookup the method for either a dynamically added or reverse manager.
    if isinstance(ctx.context, MemberExpr):
        method_name = ctx.context.name
    elif isinstance(ctx.context, CallExpr) and isinstance(ctx.context.callee, MemberExpr):
        method_name = ctx.context.callee.name
    else:
        ctx.api.fail("Unable to resolve return type of queryset/manager method", ctx.context)
        return AnyType(TypeOfAny.from_error)

    if isinstance(ctx.type, Instance):
        return resolve_manager_method_from_instance(instance=ctx.type, method_name=method_name, ctx=ctx)
    else:
        ctx.api.fail(f'Unable to resolve return type of queryset/manager method "{method_name}"', ctx.context)
        return AnyType(TypeOfAny.from_error)


def create_new_manager_class_from_from_queryset_method(ctx: DynamicClassDefContext) -> None:
    """
    Insert a new manager class node for a: '<Name> = <Manager>.from_queryset(<QuerySet>)'.
    When the assignment expression lives at module level.
    """
    semanal_api = helpers.get_semanal_api(ctx)

    # TODO: Emit an error when called in a class scope
    if semanal_api.is_class_scope():
        return

    # Don't redeclare the manager class if we've already defined it.
    manager_sym = semanal_api.lookup_current_scope(ctx.name)
    if manager_sym and isinstance(manager_sym.node, TypeInfo):
        # This is just a deferral run where our work is already finished
        return

    new_manager_info = create_manager_info_from_from_queryset_call(semanal_api, ctx.call, ctx.name)
    if new_manager_info is None:
        if not ctx.api.final_iteration:
            ctx.api.defer()
        return

    # So that the plugin will reparameterize the manager when it is constructed inside of a Model definition
    helpers.add_new_manager_base(semanal_api, new_manager_info.fullname)


def register_dynamically_created_manager(fullname: str, manager_name: str, manager_base: TypeInfo) -> None:
    manager_base.metadata.setdefault("from_queryset_managers", {})
    # The `__module__` value of the manager type created by Django's
    # `.from_queryset` is `django.db.models.manager`. But we put new type(s) in the
    # module currently being processed, so we'll map those together through metadata.
    runtime_fullname = ".".join(["django.db.models.manager", manager_name])
    manager_base.metadata["from_queryset_managers"][runtime_fullname] = fullname


def create_manager_info_from_from_queryset_call(
    api: SemanticAnalyzer, call_expr: CallExpr, name: Optional[str] = None
) -> Optional[TypeInfo]:
    """
    Extract manager and queryset TypeInfo from a from_queryset call.
    """

    if (
        # Check that this is a from_queryset call on a manager subclass
        not isinstance(call_expr.callee, MemberExpr)
        or not isinstance(call_expr.callee.expr, RefExpr)
        or not isinstance(call_expr.callee.expr.node, TypeInfo)
        or not call_expr.callee.expr.node.has_base(fullnames.BASE_MANAGER_CLASS_FULLNAME)
        or not call_expr.callee.name == "from_queryset"
        # Check that the call has one or two arguments and that the first is a
        # QuerySet subclass
        or not 1 <= len(call_expr.args) <= 2
        or not isinstance(call_expr.args[0], RefExpr)
        or not isinstance(call_expr.args[0].node, TypeInfo)
        or not call_expr.args[0].node.has_base(fullnames.QUERYSET_CLASS_FULLNAME)
    ):
        return None

    base_manager_info, queryset_info = call_expr.callee.expr.node, call_expr.args[0].node
    if queryset_info.fullname is None:
        # In some cases, due to the way the semantic analyzer works, only
        # passed_queryset.name is available. But it should be analyzed again,
        # so this isn't a problem.
        return None  # type: ignore[unreachable]

    if len(call_expr.args) == 2 and isinstance(call_expr.args[1], StrExpr):
        manager_name = call_expr.args[1].value
    else:
        manager_name = f"{base_manager_info.name}From{queryset_info.name}"

    # Always look in global scope, as that's where we'll declare dynamic manager classes
    manager_sym = api.globals.get(manager_name)
    if (
        manager_sym is not None
        and isinstance(manager_sym.node, TypeInfo)
        and manager_sym.node.has_base(base_manager_info.fullname)
        and manager_sym.node.metadata.get("django", {}).get("from_queryset_manager") == queryset_info.fullname
    ):
        # Reuse an identical, already generated, manager
        new_manager_info = manager_sym.node
    else:
        # Create a new `TypeInfo` instance for the manager type
        try:
            new_manager_info = create_manager_class(
                api=api,
                base_manager_info=base_manager_info,
                name=manager_name,
                line=call_expr.line,
                with_unique_name=name is not None and name != manager_name,
            )
        except helpers.IncompleteDefnException:
            return None

        populate_manager_from_queryset(new_manager_info, queryset_info)
        register_dynamically_created_manager(
            fullname=new_manager_info.fullname,
            manager_name=manager_name,
            manager_base=base_manager_info,
        )

    # Add the new manager to the current module
    # TODO: use proper SemanticAnalyzer API for that.
    module = api.modules[api.cur_mod_id]
    if name is not None and name != new_manager_info.name:
        # Unless names are equal, there's 2 symbol names that needs the manager info
        module.names[name] = SymbolTableNode(GDEF, new_manager_info, plugin_generated=True)

    module.names[new_manager_info.name] = SymbolTableNode(GDEF, new_manager_info, plugin_generated=True)
    return new_manager_info


def create_manager_class(
    api: SemanticAnalyzer, base_manager_info: TypeInfo, name: str, line: int, with_unique_name: bool
) -> TypeInfo:
    base_manager_instance = fill_typevars(base_manager_info)
    assert isinstance(base_manager_instance, Instance)

    # If any of the type vars are undefined we need to defer. This is handled by the caller
    if any(has_placeholder(type_var) for type_var in base_manager_info.defn.type_vars):
        raise helpers.IncompleteDefnException

    if with_unique_name:
        manager_info = helpers.add_new_class_for_module(
            module=api.modules[api.cur_mod_id],
            name=name,
            bases=[base_manager_instance],
        )
    else:
        manager_info = helpers.create_type_info(name, api.cur_mod_id, bases=[base_manager_instance])

    manager_info.line = line
    manager_info.type_vars = base_manager_info.type_vars
    manager_info.defn.type_vars = base_manager_info.defn.type_vars
    manager_info.defn.line = line

    return manager_info


def populate_manager_from_queryset(manager_info: TypeInfo, queryset_info: TypeInfo) -> None:
    """
    Add methods from the QuerySet class to the manager.
    """

    # Stash the queryset fullname which was passed to .from_queryset So that
    # our 'resolve_manager_method' attribute hook can fetch the method from
    # that QuerySet class
    django_metadata = helpers.get_django_metadata(manager_info)
    django_metadata["from_queryset_manager"] = queryset_info.fullname

    # We collect and mark up all methods before django.db.models.query.QuerySet as class members
    for class_mro_info in queryset_info.mro:
        if class_mro_info.fullname == fullnames.QUERYSET_CLASS_FULLNAME:
            break
        for name, sym in class_mro_info.names.items():
            if not isinstance(sym.node, (FuncDef, OverloadedFuncDef, Decorator)):
                continue
            # Insert the queryset method name as a class member. Note that the type of
            # the method is set as Any. Figuring out the type is the job of the
            # 'resolve_manager_method' attribute hook, which comes later.
            #
            # class BaseManagerFromMyQuerySet(BaseManager):
            #    queryset_method: Any = ...
            #
            helpers.add_new_sym_for_info(
                manager_info,
                name=name,
                sym_type=AnyType(TypeOfAny.implementation_artifact),
            )

    # For methods on BaseManager that return a queryset we need to update
    # the return type to be the actual queryset subclass used. This is done
    # by adding the methods as attributes with type Any to the manager
    # class. The actual type of these methods are resolved in
    # resolve_manager_method.
    for method_name in MANAGER_METHODS_RETURNING_QUERYSET:
        helpers.add_new_sym_for_info(
            manager_info,
            name=method_name,
            sym_type=AnyType(TypeOfAny.implementation_artifact),
        )


def create_new_manager_class_from_as_manager_method(ctx: DynamicClassDefContext) -> None:
    """
    Insert a new manager class node for a

    ```
    <manager name> = <QuerySet>.as_manager()
    ```
    """
    semanal_api = helpers.get_semanal_api(ctx)
    # Don't redeclare the manager class if we've already defined it.
    manager_node = semanal_api.lookup_current_scope(ctx.name)
    if manager_node and manager_node.type is not None:
        # This is just a deferral run where our work is already finished
        return

    manager_sym = semanal_api.lookup_fully_qualified_or_none(fullnames.MANAGER_CLASS_FULLNAME)
    assert manager_sym is not None
    manager_base = manager_sym.node
    if manager_base is None:
        if not semanal_api.final_iteration:
            semanal_api.defer()
        return

    assert isinstance(manager_base, TypeInfo)

    callee = ctx.call.callee
    assert isinstance(callee, MemberExpr)
    assert isinstance(callee.expr, RefExpr)

    queryset_info = callee.expr.node
    if queryset_info is None:
        if not semanal_api.final_iteration:
            semanal_api.defer()
        return

    assert isinstance(queryset_info, TypeInfo)

    manager_class_name = manager_base.name + "From" + queryset_info.name
    current_module = semanal_api.modules[semanal_api.cur_mod_id]
    existing_sym = current_module.names.get(manager_class_name)
    if (
        existing_sym is not None
        and isinstance(existing_sym.node, TypeInfo)
        and existing_sym.node.has_base(fullnames.MANAGER_CLASS_FULLNAME)
        and existing_sym.node.metadata.get("django", {}).get("from_queryset_manager") == queryset_info.fullname
    ):
        # Reuse an identical, already generated, manager
        new_manager_info = existing_sym.node
    else:
        # Create a new `TypeInfo` instance for the manager type
        try:
            new_manager_info = create_manager_class(
                api=semanal_api,
                base_manager_info=manager_base,
                name=manager_class_name,
                line=ctx.call.line,
                with_unique_name=True,
            )
        except helpers.IncompleteDefnException:
            if not semanal_api.final_iteration:
                semanal_api.defer()
            return

        populate_manager_from_queryset(new_manager_info, queryset_info)
        register_dynamically_created_manager(
            fullname=new_manager_info.fullname,
            manager_name=manager_class_name,
            manager_base=manager_base,
        )

        # So that the plugin will reparameterize the manager when it is constructed inside of a Model definition
        helpers.add_new_manager_base(semanal_api, new_manager_info.fullname)

    # Whenever `<QuerySet>.as_manager()` isn't called at class level, we want to ensure
    # that the variable is an instance of our generated manager. Instead of the return
    # value of `.as_manager()`. Though model argument is populated as `Any`.
    # `transformers.models.AddManagers` will populate a model's manager(s), when it
    # finds it on class level.
    var = Var(name=ctx.name, type=Instance(new_manager_info, [AnyType(TypeOfAny.from_omitted_generics)]))
    var.info = new_manager_info
    var._fullname = f"{current_module.fullname}.{ctx.name}"
    var.is_inferred = True
    # Note: Order of `add_symbol_table_node` calls matters. Depending on what level
    # we've found the `.as_manager()` call. Point here being that we want to replace the
    # `.as_manager` return value with our newly created manager.
    added = semanal_api.add_symbol_table_node(
        ctx.name, SymbolTableNode(semanal_api.current_symbol_kind(), var, plugin_generated=True)
    )
    assert added
    # Add the new manager to the current module
    added = semanal_api.add_symbol_table_node(
        # We'll use `new_manager_info.name` instead of `manager_class_name` here
        # to handle possible name collisions, as it's unique.
        new_manager_info.name,
        # Note that the generated manager type is always inserted at module level
        SymbolTableNode(GDEF, new_manager_info, plugin_generated=True),
    )
    assert added


def reparametrize_any_manager_hook(ctx: ClassDefContext) -> None:
    """
    Add implicit generics to manager classes that are defined without generic.

    Eg.

        class MyManager(models.Manager): ...

    is interpreted as:

        _T = TypeVar('_T', covariant=True)
        class MyManager(models.Manager[_T]): ...

    Note that this does not happen if mypy is run with disallow_any_generics = True,
    as not specifying the generic type is then considered an error.
    """

    manager = ctx.api.lookup_fully_qualified_or_none(ctx.cls.fullname)
    if manager is None or manager.node is None:
        return
    assert isinstance(manager.node, TypeInfo)

    if manager.node.type_vars:
        # We've already been here
        return

    parent_manager = next(
        (base for base in manager.node.bases if base.type.has_base(fullnames.BASE_MANAGER_CLASS_FULLNAME)),
        None,
    )
    if parent_manager is None:
        return

    is_missing_params = (
        len(parent_manager.args) == 1
        and isinstance(parent_manager.args[0], AnyType)
        and parent_manager.args[0].type_of_any is TypeOfAny.from_omitted_generics
    )
    if not is_missing_params:
        return

    type_vars = tuple(parent_manager.type.defn.type_vars)

    # If we end up with placeholders we need to defer so the placeholders are
    # resolved in a future iteration
    if any(has_placeholder(type_var) for type_var in type_vars):
        if not ctx.api.final_iteration:
            ctx.api.defer()
        else:
            return

    parent_manager.args = type_vars
    manager.node.defn.type_vars = list(type_vars)
    manager.node.add_type_vars()
