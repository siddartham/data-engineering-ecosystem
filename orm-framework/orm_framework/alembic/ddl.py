from typing import Any

from alembic.ddl.base import (  # type: ignore
    ColumnComment,
    ColumnName,
    alter_table,
    format_column_name,
    format_table_name,
)
from sqlalchemy.ext.compiler import compiles  # type: ignore
from sqlalchemy.sql.compiler import DDLCompiler  # type: ignore


@compiles(ColumnComment, "snowflake")
def _alter_column_comment(
    element: ColumnComment, compiler: DDLCompiler, **kwargs: Any
) -> str:
    """
    This provides functionality for compiling column comment updates for
    Snowflake.
    """
    comment: str = element.comment or ""
    return (
        f"COMMENT ON COLUMN "
        f"{format_table_name(compiler, element.table_name, element.schema)}."
        f"{format_column_name(compiler, element.column_name)} "
        f"IS '{comment}'"
    )


@compiles(ColumnName, "snowflake")
def _visit_column_name(
    element: ColumnName, compiler: DDLCompiler, **kwargs: Any
) -> str:
    return (
        f"{alter_table(compiler, element.table_name, element.schema)} "
        "RENAME COLUMN "
        f"{format_column_name(compiler, element.column_name)} TO "
        f"{format_column_name(compiler, element.newname)}"
    )
