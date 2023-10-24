from django.db.models.fields import Field
from django.utils.functional import cached_property

from .base import Operation

class FieldOperation(Operation):
    model_name: str
    name: str
    def __init__(self, model_name: str, name: str, field: Field | None = ...) -> None: ...
    @cached_property
    def name_lower(self) -> str: ...
    @cached_property
    def model_name_lower(self) -> str: ...
    def is_same_model_operation(self, operation: FieldOperation) -> bool: ...
    def is_same_field_operation(self, operation: FieldOperation) -> bool: ...

class AddField(FieldOperation):
    field: Field
    preserve_default: bool
    def __init__(self, model_name: str, name: str, field: Field, preserve_default: bool = ...) -> None: ...

class RemoveField(FieldOperation): ...

class AlterField(FieldOperation):
    field: Field
    preserve_default: bool
    def __init__(self, model_name: str, name: str, field: Field, preserve_default: bool = ...) -> None: ...

class RenameField(FieldOperation):
    old_name: str
    new_name: str
    def __init__(self, model_name: str, old_name: str, new_name: str) -> None: ...
    @cached_property
    def old_name_lower(self) -> str: ...
    @cached_property
    def new_name_lower(self) -> str: ...
