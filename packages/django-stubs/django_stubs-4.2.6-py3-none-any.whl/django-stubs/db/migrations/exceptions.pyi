from django.db.migrations.migration import Migration
from django.db.utils import DatabaseError

class AmbiguityError(Exception): ...
class BadMigrationError(Exception): ...
class CircularDependencyError(Exception): ...
class InconsistentMigrationHistory(Exception): ...
class InvalidBasesError(ValueError): ...
class IrreversibleError(RuntimeError): ...

class NodeNotFoundError(LookupError):
    message: str
    origin: Migration | None
    node: tuple[str, str]
    def __init__(self, message: str, node: tuple[str, str], origin: Migration | None = ...) -> None: ...

class MigrationSchemaMissing(DatabaseError): ...
class InvalidMigrationPlan(ValueError): ...
