from typing import Any

from django.db.models.query_utils import DeferredAttribute

class SpatialProxy(DeferredAttribute):
    def __init__(self, klass: Any, field: Any, load_func: Any | None = ...) -> None: ...
    def __get__(self, instance: Any, cls: Any | None = ...) -> Any: ...
    def __set__(self, instance: Any, value: Any) -> Any: ...
