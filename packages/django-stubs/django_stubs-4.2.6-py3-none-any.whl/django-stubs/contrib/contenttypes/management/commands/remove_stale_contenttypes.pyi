from typing import Any

from django.core.management import BaseCommand
from django.db.models.base import Model
from django.db.models.deletion import Collector

class Command(BaseCommand): ...

class NoFastDeleteCollector(Collector):
    data: dict[type[Model], set[Model] | list[Model]]
    dependencies: dict[Any, Any]
    fast_deletes: list[Any]
    field_updates: dict[Any, Any]
    using: str
    def can_fast_delete(self, *args: Any, **kwargs: Any) -> bool: ...
