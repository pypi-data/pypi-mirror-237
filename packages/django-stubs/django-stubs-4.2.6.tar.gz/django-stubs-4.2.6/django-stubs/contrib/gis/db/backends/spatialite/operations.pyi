from typing import Any

from django.contrib.gis.db.backends.base.operations import BaseSpatialOperations
from django.contrib.gis.db.backends.utils import SpatialOperator
from django.db.backends.sqlite3.operations import DatabaseOperations

class SpatialiteNullCheckOperator(SpatialOperator): ...

class SpatiaLiteOperations(BaseSpatialOperations, DatabaseOperations):
    name: str
    spatialite: bool
    Adapter: Any
    collect: str
    extent: str
    makeline: str
    unionagg: str
    gis_operators: Any
    disallowed_aggregates: Any
    select: str
    function_names: Any
    @property
    def unsupported_functions(self) -> set[str]: ...  # type: ignore[override]
    @property
    def spatial_version(self) -> Any: ...
    def geo_db_type(self, f: Any) -> None: ...
    def get_distance(self, f: Any, value: Any, lookup_type: Any) -> Any: ...
    def geos_version(self) -> Any: ...
    def proj_version(self) -> Any: ...
    def lwgeom_version(self) -> Any: ...
    def spatialite_version(self) -> Any: ...
    def spatialite_version_tuple(self) -> Any: ...
    def spatial_aggregate_name(self, agg_name: Any) -> Any: ...
    def geometry_columns(self) -> Any: ...
    def spatial_ref_sys(self) -> Any: ...
    def get_geometry_converter(self, expression: Any) -> Any: ...
