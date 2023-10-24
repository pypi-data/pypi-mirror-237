from decimal import Decimal
from typing import Any

from typing_extensions import Self, TypeAlias

_NUMERIC_TYPES: TypeAlias = int | float | Decimal

class MeasureBase:
    STANDARD_UNIT: str | None
    UNITS: dict[str, float]
    ALIAS: dict[str, str]
    LALIAS: dict[str, str]
    def __init__(self, default_unit: str | None = ..., **kwargs: Any) -> None: ...
    standard: Any
    def __getattr__(self, name: str) -> float: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: Self) -> bool: ...
    def __add__(self, other: Self) -> Self: ...
    def __iadd__(self, other: Self) -> Self: ...
    def __sub__(self, other: Self) -> Self: ...
    def __isub__(self, other: Self) -> Self: ...
    def __mul__(self, other: _NUMERIC_TYPES) -> Any: ...
    def __imul__(self, other: _NUMERIC_TYPES) -> Self: ...
    def __rmul__(self, other: Any) -> Self: ...
    def __truediv__(self, other: _NUMERIC_TYPES) -> Self: ...
    def __itruediv__(self, other: _NUMERIC_TYPES) -> Self: ...
    def __bool__(self) -> bool: ...
    def default_units(self, kwargs: dict[str, Any]) -> tuple[float, str]: ...
    @classmethod
    def unit_attname(cls, unit_str: str) -> str: ...

class Distance(MeasureBase):
    STANDARD_UNIT: str

class Area(MeasureBase):
    STANDARD_UNIT: str

D: TypeAlias = Distance

A: TypeAlias = Area
