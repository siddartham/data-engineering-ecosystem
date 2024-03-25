import logging
from logging.config import fileConfig
from types import ModuleType
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Literal,
    Optional,
    Tuple,
    Type,
    Union,
)

import alembic  # type: ignore
import alembic.autogenerate.compare
from alembic.runtime.environment import EnvironmentContext  # type: ignore
from alembic.runtime.migration import MigrationContext  # type: ignore
from sqlalchemy.engine.base import Connection, Engine  # type: ignore
from sqlalchemy.engine.url import URL  # type: ignore
from sqlalchemy.schema import Column  # type: ignore
from sqlalchemy.sql.schema import (  # type: ignore
    ForeignKey,
    ForeignKeyConstraint,
    SchemaItem,
    Table,
)
from sqlalchemy.sql.sqltypes import DateTime, Integer, Numeric  # type: ignore
from sqlalchemy.sql.type_api import TypeEngine  # type: ignore

from ..declarative import MetaData
from ..types import get_column_type_class
from ..utilities import get_bind_dialect_name
from . import ddl

try:
    from alembic.runtime.environment import AutogenContext  # type: ignore
except ImportError:
    AutogenContext = EnvironmentContext  # type: ignore

snowflake: Optional[ModuleType]
try:
    from . import snowflake
except ImportError:
    snowflake = None

# Prevent linters from identifying these imports as unused
assert ddl
assert snowflake

context: EnvironmentContext = alembic.context  # type: ignore
if TYPE_CHECKING:
    assert issubclass(EnvironmentContext, AutogenContext)


def _compare_type(
    migration_context: MigrationContext,
    inspector_column: Type[Column],
    metadata_column: Type[Column],
    inspector_column_type: TypeEngine,
    metadata_column_type: TypeEngine,
) -> Optional[bool]:
    """
    This function is passed to the `compare_type` parameter of
    `EnvironmentContext.configure` in order to ensure Snowflake's
    implementation of an integer (as a zero-precision decimal) is recognized as
    such.

    A return value of `False` indicates that the two types are the same. A
    return value of `True` indicates the two types are different. A return
    value of `None` indicates default comparison logic should be used.
    """
    if are_column_types_compatible(
        metadata_column_type, inspector_column_type
    ):
        return False
    return None


def _get_foreign_key_constraint_comparator(
    foreign_key_constraint: ForeignKeyConstraint,
) -> Tuple[Tuple[Any, ...], ...]:
    column: Column
    foreign_key: ForeignKey
    items: Tuple[Any, ...]
    number_of_columns: int = len(foreign_key_constraint.columns)
    return tuple(
        sorted(
            zip(
                (column.name for column in foreign_key_constraint.columns),
                (
                    foreign_key.column.name
                    for foreign_key in foreign_key_constraint.elements
                ),
                (
                    (foreign_key_constraint.name,)
                    * number_of_columns
                    # foreign_key.name
                    # for foreign_key in foreign_key_constraint.elements
                ),
                (
                    foreign_key.use_alter
                    for foreign_key in foreign_key_constraint.elements
                ),
                (
                    foreign_key.onupdate
                    for foreign_key in foreign_key_constraint.elements
                ),
                (
                    foreign_key.ondelete
                    for foreign_key in foreign_key_constraint.elements
                ),
                (
                    foreign_key.deferrable
                    for foreign_key in foreign_key_constraint.elements
                ),
                (
                    foreign_key.initially
                    for foreign_key in foreign_key_constraint.elements
                ),
                (
                    foreign_key.deferrable
                    for foreign_key in foreign_key_constraint.elements
                ),
                (
                    foreign_key.link_to_name
                    for foreign_key in foreign_key_constraint.elements
                ),
                (
                    foreign_key.match
                    for foreign_key in foreign_key_constraint.elements
                ),
            ),
            # Sort by only the column and reference column names
            key=lambda items: items[:2],
        )
    )


def _compare_foreign_key_constraints(
    foreign_key_constraint_a: ForeignKeyConstraint,
    foreign_key_constraint_b: ForeignKeyConstraint,
) -> bool:
    """
    This function compares two foreign key constraints and returns `True`
    if they are the same or `False` if they are different.
    """
    foreign_key_constraint_a_comparator: Tuple[Tuple[Any, ...], ...] = (
        _get_foreign_key_constraint_comparator(foreign_key_constraint_a)
    )
    foreign_key_constraint_b_comparator: Tuple[Tuple[Any, ...], ...] = (
        _get_foreign_key_constraint_comparator(foreign_key_constraint_b)
    )
    if (
        foreign_key_constraint_a_comparator
        == foreign_key_constraint_b_comparator
    ):
        return True
    else:
        message: str = (
            f"{repr(foreign_key_constraint_a_comparator)}!="
            f"{repr(foreign_key_constraint_b_comparator)}"
        )
        logging.info(message)
        print(message)
        return False


def _get_include_object_function(
    dialect_name: str,
) -> Callable[
    [
        Any,
        Optional[str],
        Literal[
            "schema",
            "table",
            "column",
            "index",
            "unique_constraint",
            "foreign_key_constraint",
        ],
        bool,
        SchemaItem,
    ],
    bool,
]:
    def include_object(
        schema_item: Any,
        name: Optional[str],
        type_: Literal[
            "schema",
            "table",
            "column",
            "index",
            "unique_constraint",
            "foreign_key_constraint",
        ],
        reflected: bool,
        compare_to: SchemaItem,
    ) -> bool:
        if (
            type_ == "table"
            and isinstance(schema_item, Table)
            and schema_item.info.get("is_view", False)
        ):
            return False
        elif type_ == "index" and dialect_name in (
            "hive",
            "snowflake",
            "databricks",
        ):
            return False
        elif (
            type_ == "foreign_key_constraint"
            and isinstance(schema_item, ForeignKeyConstraint)
            and isinstance(compare_to, ForeignKeyConstraint)
        ):
            return not _compare_foreign_key_constraints(
                schema_item, compare_to
            )
        return True

    return include_object


def _render_item(
    type_name: str, item: Any, autogen_context: AutogenContext
) -> Union[str, Literal[False]]:
    """
    This function causes the default rendering to occur—we just use
    it as a hook to add imports
    """
    if type_name == "type":
        item_type: type
        if isinstance(item, type):
            item_type = item
        else:
            item_type = type(item)
        autogen_context.imports.add(  # type: ignore
            f"import {item_type.__module__}  # type: ignore"
        )
    return False


def _re_key_metadata_tables(
    metadata: MetaData,
) -> Dict[str, Table]:
    # Assign schemas to tables
    tables: Dict[str, Table] = {}
    table: Table
    for table in metadata.tables.values():
        tables[table.key] = table
    original_tables: Dict[str, Table] = metadata.tables
    metadata.tables = tables
    return original_tables


def _should_include_schemas(dialect_name: str) -> bool:
    return dialect_name not in ("databricks",)


def run(
    metadata: MetaData,
    bind: Union[Engine, Connection, str, URL] = "",
    version_table: str = "ALEMBIC_VERSION",
    version_table_schema: Optional[str] = None,
    echo: bool = False,
) -> None:
    """
    Run migrations in online or offline mode, as determined by
    `alembic.context`, against the indicated metadata and engine, connection,
    or URL.

    Parameters:

    - bind (
      str|sqlalchemy.engine.interfaces.Connectable|sqlalchemy.engine.url.URL
      ): The engine, connection object, or URL of a database with which
      we are comparing `metadata`.
    - metadata (orm_framework.declarative.MetaData): This should be
      the metadata associated with your declarative base.
    - version_table (str) = "ALEMBIC_VERSION": The name of the database table
      used to track version information.
    - version_table_schema (str) = None: The name of the database schema
      wherein the `version_table` is located. If not provided, the default
      schema will be used.
    """
    # Ensure metadata is bound
    if bind:
        metadata.bind = bind
    bind = metadata.bind
    original_metadata_tables: Dict[str, Table] = _re_key_metadata_tables(
        metadata
    )
    dialect_name: str = get_bind_dialect_name(bind)
    include_object: Callable[
        [
            Any,
            Optional[str],
            Literal[
                "schema",
                "table",
                "column",
                "index",
                "unique_constraint",
                "foreign_key_constraint",
            ],
            bool,
            SchemaItem,
        ],
        bool,
    ] = _get_include_object_function(dialect_name)
    # Interpret the config file for Python logging.
    fileConfig(context.config.config_file_name)  # type: ignore
    # Determine if we should be in online or offline mode
    offline: bool = context.is_offline_mode()
    message: str = f"Running migrations {'offline' if offline else 'online'}"
    print(message)
    logging.info(message)
    if offline:
        if isinstance(bind, Engine):
            bind = bind.url
        elif isinstance(bind, Connection):
            bind = bind.engine.url
        context.configure(
            url=bind,
            target_metadata=metadata,
            literal_binds=True,
            dialect_opts={"paramstyle": "named"},
            sqlalchemy_module_prefix="sqlalchemy.",
            version_table=version_table,
            version_table_schema=version_table_schema,
            include_schemas=_should_include_schemas(dialect_name),
            include_object=include_object,
            compare_type=_compare_type,  # type: ignore
            render_item=_render_item,
        )
    else:
        metadata.bind.echo = echo
        context.configure(
            connection=metadata.bind.connect(),
            target_metadata=metadata,
            sqlalchemy_module_prefix="sqlalchemy.",
            version_table=version_table,
            version_table_schema=version_table_schema,
            include_schemas=_should_include_schemas(dialect_name),
            compare_type=_compare_type,  # type: ignore
            include_object=include_object,
            render_item=_render_item,
            incremental=True,
            transactional_ddl=True,
        )
    with context.begin_transaction():
        context.run_migrations()
    # Restore the original metadata tables
    metadata.tables = original_metadata_tables
