from collections.abc import Iterator
from typing import Any

from django.contrib.gis.geos.geometry import GEOSGeometry

class Point(GEOSGeometry):
    has_cs: bool
    def __init__(
        self, x: Any | None = ..., y: Any | None = ..., z: Any | None = ..., srid: Any | None = ...
    ) -> None: ...
    def __iter__(self) -> Iterator[float]: ...
    def __len__(self) -> int: ...
    @property
    def x(self) -> float: ...
    @x.setter
    def x(self, value: float) -> None: ...
    @property
    def y(self) -> float: ...
    @y.setter
    def y(self, value: float) -> None: ...
    @property
    def z(self) -> float | None: ...
    @z.setter
    def z(self, value: float) -> None: ...
    @property
    def coords(self) -> tuple[float, ...]: ...
    @coords.setter
    def coords(self, tup: Any) -> None: ...
