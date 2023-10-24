from typing import Any, Generic, Literal, TypeVar

from django.db import models
from django.forms.forms import BaseForm
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.utils.datastructures import _ListOrTuple
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View
from django.views.generic.detail import BaseDetailView, SingleObjectMixin, SingleObjectTemplateResponseMixin

_FormT = TypeVar("_FormT", bound=BaseForm)
_ModelFormT = TypeVar("_ModelFormT", bound=BaseModelForm)
_M = TypeVar("_M", bound=models.Model)

class FormMixin(Generic[_FormT], ContextMixin):
    initial: dict[str, Any]
    form_class: type[_FormT] | None
    success_url: str | None
    prefix: str | None
    def get_initial(self) -> dict[str, Any]: ...
    def get_prefix(self) -> str | None: ...
    def get_form_class(self) -> type[_FormT]: ...
    def get_form(self, form_class: type[_FormT] | None = ...) -> _FormT: ...
    def get_form_kwargs(self) -> dict[str, Any]: ...
    def get_success_url(self) -> str: ...
    def form_valid(self, form: _FormT) -> HttpResponse: ...
    def form_invalid(self, form: _FormT) -> HttpResponse: ...
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: ...

class ModelFormMixin(Generic[_M, _ModelFormT], FormMixin[_ModelFormT], SingleObjectMixin[_M]):
    fields: _ListOrTuple[str] | Literal["__all__"] | None
    def get_form_class(self) -> type[_ModelFormT]: ...
    def get_form_kwargs(self) -> dict[str, Any]: ...
    def get_success_url(self) -> str: ...
    def form_valid(self, form: _ModelFormT) -> HttpResponse: ...

class ProcessFormView(View):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def put(self, *args: Any, **kwargs: Any) -> HttpResponse: ...

class BaseFormView(FormMixin[_FormT], ProcessFormView): ...
class FormView(TemplateResponseMixin, BaseFormView[_FormT]): ...

class BaseCreateView(ModelFormMixin[_M, _ModelFormT], ProcessFormView):
    object: _M | None
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...

class CreateView(SingleObjectTemplateResponseMixin, BaseCreateView[_M, _ModelFormT]):
    template_name_suffix: str

class BaseUpdateView(ModelFormMixin[_M, _ModelFormT], ProcessFormView):
    object: _M
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...

class UpdateView(SingleObjectTemplateResponseMixin, BaseUpdateView[_M, _ModelFormT]):
    template_name_suffix: str

class DeletionMixin(Generic[_M]):
    success_url: str | None
    object: _M
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def delete(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...
    def get_success_url(self) -> str: ...

class BaseDeleteView(Generic[_M, _ModelFormT], DeletionMixin[_M], FormMixin[_ModelFormT], BaseDetailView[_M]):
    object: _M
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class DeleteView(Generic[_M, _ModelFormT], SingleObjectTemplateResponseMixin, BaseDeleteView[_M, _ModelFormT]):
    object: _M
    template_name_suffix: str

class DeleteViewCustomDeleteWarning(Warning): ...
