from typing import Any

from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.backends.oracle.base import DatabaseWrapper

class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):
    connection: DatabaseWrapper
    sql_create_column: str
    sql_alter_column_type: str
    sql_alter_column_null: str
    sql_alter_column_not_null: str
    sql_alter_column_default: str
    sql_alter_column_no_default: str
    sql_delete_column: str
    sql_create_column_inline_fk: str
    sql_delete_table: str
    sql_create_index: str
    def quote_value(self, value: Any) -> str: ...
    def remove_field(self, model: Any, field: Any) -> None: ...
    def delete_model(self, model: Any) -> None: ...
    def alter_field(self, model: Any, old_field: Any, new_field: Any, strict: bool = ...) -> None: ...
    def normalize_name(self, name: Any) -> str: ...
    def prepare_default(self, value: Any) -> Any: ...
