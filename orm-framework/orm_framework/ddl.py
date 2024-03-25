import collections.abc
import logging
import re
from collections import OrderedDict
from copy import copy
from typing import (
    Any,
    Container,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
    Callable
)
from urllib import parse

from sqlalchemy import (  # type: ignore  # noqa
    Boolean,
    Column,
    ColumnDefault,
    DefaultClause,
    ForeignKeyConstraint,
    PrimaryKeyConstraint,
    Table,
    text,
    types
)
from sqlalchemy.engine.base import Connection, Engine  # type: ignore
from sqlalchemy.ext.compiler import compiles  # type: ignore
from sqlalchemy.sql import Selectable, ddl  # type: ignore
from sqlalchemy.sql.compiler import DDLCompiler  # type: ignore
from sqlalchemy.sql.ddl import (  # type: ignore
    AddConstraint,
    CreateColumn,
    CreateIndex,
    CreateTable,
    DDLElement,
    DropConstraint,
    DropTable,
    sort_tables_and_constraints,
)
from sqlalchemy.sql.expression import BindParameter  # type: ignore

from .utilities import (
    SUPPORTED_DIALECTS,
    get_dialect_qualified_table_name,
    get_dialect_table_name,
    is_declared_view,
    is_view,
)

__all__: List[str] = [
    "register_hive_create_table_compiler",
    "DropPrimaryKey",
    "AddPrimaryKey",
    "DUMMY_STATEMENT",
]

log: logging.Logger = logging.getLogger(__name__)
DUMMY_STATEMENT: str = "SELECT 'DUMMY_STATEMENT'"

_original_sort_tables_and_constraints: Callable[  # type: ignore
    ..., List[tuple]
] = sort_tables_and_constraints


def _foreign_key_filter(foreign_key_constraint: ForeignKeyConstraint) -> bool:
    """
    This function serves as an input to the `filter_fn` parameter of the
    `ddl.sort_tables_and_constraints` function to determine how to sort
    ForeignKeyConstraints during the execution of DDLs.

    When this function returns True, the foreign key is appended
    to an iterable of foreign key constraints to be applied after all other
    CreateTable DDLs have been executed.

    These constraints are applied as `ALTER TABLE` statements as opposed to
    in-line `CONSTRAINT`s in the `CREATE TABLE` statement.

    Parameters:

    - foreign_key_constraint (ForeignKeyConstraint): A sqlalchemy
    ForeignKeyConstraint
    """
    return (
        foreign_key_constraint.table == foreign_key_constraint.referred_table
    )


def _sort_tables_and_constraints(*args: Any, **kwargs: Any) -> List[tuple]:
    kwargs.update({"filter_fn": _foreign_key_filter})

    return _original_sort_tables_and_constraints(*args, **kwargs)


ddl.sort_tables_and_constraints = _sort_tables_and_constraints  # type: ignore


# region Views
class CreateView(DDLElement):
    __visit_name__: str = "create_view"
    __slots__: Tuple[str, ...] = (
        "element",
        "statement",
        "or_replace",
        "materialized",
        "if_not_exists",
        "bind",
    )

    def __init__(
        self,
        element: Table,
        statement: Union[str, Selectable],
        or_replace: bool = False,
        materialized: bool = False,
        if_not_exists: bool = False,
        bind: Union[Engine, Connection, None] = None,
    ):
        self.element: Table = element
        self.statement: Union[str, Selectable] = statement
        self.or_replace: bool = or_replace
        self.materialized: bool = materialized
        self.if_not_exists: bool = if_not_exists and not or_replace
        self.bind = bind


class DropView(DDLElement):

    __visit_name__: str = "drop_view"
    __slots__: Tuple[str, ...] = (
        "element",
        "materialized",
        "if_exists",
        "bind",
    )

    def __init__(
        self,
        element: Table,
        materialized: bool = False,
        if_exists: bool = True,
        bind: Union[Engine, Connection, None] = None,
    ) -> None:
        self.element: Table = element
        self.materialized: bool = materialized
        self.if_exists: bool = if_exists
        self.bind: Union[Engine, Connection, None] = bind


@compiles(CreateColumn, "databricks")
def _visit_create_column(
    element: CreateColumn, compiler: DDLCompiler, **kwargs: Any
) -> str:
    column: Column = element.element
    element.element = column
    if column.default and isinstance(column.type, Boolean):
        if isinstance(column.server_default.arg, BindParameter):
            column.server_default = DefaultClause(
                text(
                    "true"
                    if bool(column.server_default.arg.value)
                    else "false"
                )
            )
    return compiler.visit_create_column(element, **kwargs)


@compiles(CreateView)
def _visit_create_view(
    element: CreateView, compiler: DDLCompiler, **kwargs: Any
) -> Optional[str]:
    # If the dialect-specific "table_name" argument for table
    # is populated with an empty string, we do not create the table
    # for that dialect
    dialect_name: Union[str, bytes] = (
        compiler.dialect.name
        if compiler and compiler.dialect
        else element.bind.dialect.name  # type: ignore
    )
    qualified_table_name: str = get_dialect_qualified_table_name(
        dialect_name, element.element, quote=compiler.preparer.quote
    )
    if not qualified_table_name:
        log.info(
            f"The {str(dialect_name)} name for "
            f"{str(element.element.__tablename__)} "
            'is "", so this table will not be created.'
        )
        return DUMMY_STATEMENT
    return "CREATE {}{}VIEW {}{} AS {}".format(
        "OR REPLACE " if element.or_replace else "",
        "MATERIALIZED " if element.materialized else "",
        "IF NOT EXISTS " if element.if_not_exists else "",
        qualified_table_name,
        (
            element.statement
            if isinstance(element.statement, str)
            else compiler.sql_compiler.process(
                element.statement, literal_binds=True
            )
        ),
    )


@compiles(DropView)
def _visit_drop_view(
    element: DropView, compiler: DDLCompiler, **kwargs: Any
) -> Optional[str]:
    dialect_name: Union[str, bytes] = (
        compiler.dialect.name
        if compiler and compiler.dialect
        else element.bind.dialect.name  # type: ignore
    )
    qualified_table_name: str = get_dialect_qualified_table_name(
        dialect_name, element.element, quote=compiler.preparer.quote
    )
    if not qualified_table_name:
        log.info(
            f"The {str(dialect_name)} name for "
            f"{str(element.element.__tablename__)} "
            'is "", so this table will not be created.'
        )
        return DUMMY_STATEMENT
    return "DROP {}VIEW {}{}".format(
        "MATERIALIZED " if element.materialized else "",
        "IF EXISTS " if element.if_exists else "",
        qualified_table_name,
    )


# endregion
# region Builtins


@compiles(types.String, "databricks")
def compile_string_databricks(
    type_: types.TypeEngine,
    compiler: DDLCompiler,
    **kwargs: Any,
) -> str:
    # Renders the sqlalchemy String type to a Databricks STRING type
    return "STRING"


@compiles(types.Numeric, "databricks")
def compile_numeric_databricks(
    type_: types.TypeEngine,
    compiler: DDLCompiler,
    **kwargs: Any,
) -> str:
    """
    The DatabricksDialect class doesn't handle precision or scale, so we
    need to handle it here by overriding the Numeric type compilation.
    """
    return compiler.visit_DECIMAL(type_, **kwargs)


@compiles(CreateTable, *(set(SUPPORTED_DIALECTS) - {"hive", "databricks"}))
def _visit_create_table(
    element: CreateTable, compiler: DDLCompiler, **kwargs: Any
) -> Optional[str]:
    dialect_name: Union[str, bytes] = (
        compiler.dialect.name
        if compiler and compiler.dialect
        else element.bind.dialect.name  # type: ignore
    )
    # If the dialect-specific "table_name" argument for table
    # is populated with an empty string, we do not create the table
    # for that dialect
    table_name: str = get_dialect_table_name(dialect_name, element.element)
    if table_name == "" or is_declared_view(element.element):
        return DUMMY_STATEMENT
    return compiler.visit_create_table(element, **kwargs)


@compiles(CreateTable, "databricks")
def _visit_create_table_databricks(
    element: CreateTable, compiler: DDLCompiler, **kwargs: Any
) -> str:
    element_table: Table = element.element

    def _databricks_post_create_table(table: Table) -> str:
        column: Column
        if any(
            map(
                lambda column: isinstance(column.default, ColumnDefault),
                element_table.columns,
            )
        ):
            return (
                " USING DELTA"
                "\nTBLPROPERTIES("
                "'delta.feature.allowColumnDefaults' = 'supported',"
                "'delta.minReaderVersion' = '2',"
                "'delta.minWriterVersion' = '5',"
                "'delta.columnMapping.mode' = 'name'"
                ");"
            )
        return (
            " USING DELTA"
            "\nTBLPROPERTIES("
            "'delta.minReaderVersion' = '2',"
            "'delta.minWriterVersion' = '5',"
            "'delta.columnMapping.mode' = 'name'"
            ");"
        )

    compiler.post_create_table = _databricks_post_create_table
    table_name: str = get_dialect_table_name("databricks", element.element)
    if table_name == "" or is_declared_view(element.element):
        return DUMMY_STATEMENT

    return compiler.visit_create_table(element, **kwargs)


@compiles(DropTable)
def _visit_drop_table(
    element: DropTable, compiler: DDLCompiler, **kwargs: Any
) -> Optional[str]:
    dialect_name: Union[str, bytes] = (
        compiler.dialect.name
        if compiler and compiler.dialect
        else (
            element.bind.dialect.name
            if element.bind and element.bind.dialect
            else element.element.bind.dialect.name
        )  # type: ignore
    )
    # If the dialect-specific "table_name" argument for table
    # is populated with an empty string, we do not create the table
    # for that dialect
    table_name: str = get_dialect_table_name(dialect_name, element.element)
    # If the table name is empty, this table/view is skipped for this dialect
    # If this is a *declared* view, hooks will be in place to handle the drop
    if table_name == "" or is_declared_view(element.element):
        return DUMMY_STATEMENT
    drop_statement: str = compiler.visit_drop_table(element, **kwargs)
    # If this is an *undeclared view*, we will try to drop it by substituting
    # "VIEW" for "TABLE" (this may not always work, such as w/ materialized
    # views, however)
    if is_view(
        element.element,
        bind=element.bind or element.element.bind,
    ):
        if " TABLE " in drop_statement:
            drop_statement = drop_statement.replace(" TABLE ", " VIEW ", 1)
        elif " table " in drop_statement:
            drop_statement = drop_statement.replace(" table ", " view ", 1)
        else:
            assert " VIEW " in drop_statement or " view " in drop_statement
    return drop_statement


class AddPrimaryKey(DDLElement):

    __visit_name__: str = "add_primary_key"

    def __init__(
        self,
        table_name: str,
        schema: Optional[str] = None,
        column_names: Iterable[str] = (),
        bind: Union[Engine, Connection, None] = None,
    ) -> None:
        self._bind: Union[Engine, Connection, None] = bind
        self.table_name: str = table_name
        self.schema: Optional[str] = schema
        self.column_names: Tuple[str, ...] = tuple(column_names)


class DropPrimaryKey(DDLElement):
    __visit_name__: str = "drop_primary_key"

    def __init__(
        self,
        table_name: str,
        schema: Optional[str] = None,
        bind: Union[Engine, Connection, None] = None,
    ) -> None:
        self._bind: Union[Engine, Connection, None] = bind
        self.table_name: str = table_name
        self.schema: Optional[str] = schema


def _get_element_compiler_table_name(
    element: AddPrimaryKey, compiler: DDLCompiler
) -> str:
    table_name: str = compiler.preparer.quote(element.table_name)
    if element.schema:
        table_name = f"{compiler.preparer.quote(element.schema)}.{table_name}"
    return table_name


def _get_constraint_compiler_parent_table_name(
    constraint: DropConstraint, compiler: DDLCompiler
) -> str:
    table_name: str = compiler.preparer.quote(constraint.element.parent.name)
    if constraint.element.parent.schema:
        table_name = (
            f"{compiler.preparer.quote(constraint.element.parent.schema)}"
            f".{table_name}"
        )
    return table_name


@compiles(AddPrimaryKey)
def _visit_add_primary_key(
    element: AddPrimaryKey, compiler: DDLCompiler, **kwargs: Any
) -> str:
    table_name: str = _get_element_compiler_table_name(element, compiler)
    column_names: Iterable[str] = (
        compiler.preparer.quote(column_name)
        for column_name in element.column_names
    )
    return (
        f"ALTER TABLE {table_name} ADD "
        f"PRIMARY KEY ({', '.join(column_names)})"
    )


@compiles(DropConstraint, "databricks")
def _visit_drop_constraint_databricks(
    constraint: DropConstraint, compiler: DDLCompiler, **kwargs: Any
) -> str:
    table_name: str = _get_constraint_compiler_parent_table_name(
        constraint, compiler
    )
    formatted_name: str = compiler.preparer.format_constraint(
        constraint.element
    )
    # The constraint name needs to be lowercased in databricks
    formatted_name = formatted_name.lower()
    cascade: str = "CASCADE " if constraint.cascade else ""
    if_exists: str = "IF EXISTS " if constraint.if_exists else ""

    return (
        f"ALTER TABLE {table_name} DROP CONSTRAINT "
        f"{if_exists}"
        f"{formatted_name}"
        f"{cascade}"
    )


@compiles(DropConstraint)
def _visit_drop_constraint(
    constraint: DropConstraint, compiler: DDLCompiler, **kwargs: Any
) -> str:
    table_name: str = _get_constraint_compiler_parent_table_name(
        constraint, compiler
    )
    formatted_name: str = compiler.preparer.format_constraint(
        constraint.element
    )
    cascade: str = "CASCADE " if constraint.cascade else ""
    if_exists: str = "IF EXISTS " if constraint.if_exists else ""

    return (
        f"ALTER TABLE {table_name} DROP CONSTRAINT "
        f"{if_exists}"
        f"{formatted_name}"
        f"{cascade}"
    )


@compiles(DropPrimaryKey)
def _visit_drop_primary_key(
    element: DropPrimaryKey, compiler: DDLCompiler, **kwargs: Any
) -> str:
    table_name: str = _get_element_compiler_table_name(element, compiler)
    return f"ALTER TABLE {table_name} DROP PRIMARY KEY"


@compiles(CreateIndex, *("snowflake", "databricks"))
def _visit_create_index(
    element: CreateIndex, compiler: DDLCompiler, **kwargs: Any
) -> Optional[str]:
    """
    Do not create indices for snowflake or databricks
    """
    return DUMMY_STATEMENT

@compiles(CreateColumn, "presto", "hive")
def _visit_create_column(
    element: CreateColumn, compiler: DDLCompiler, **kwargs: Any
) -> Optional[str]:
    """
    Do not set primary keys, not-nulls, or autoincrements for
    the hive and presto dialects
    """
    column: Column = copy(element.element)
    column.autoincrement = False
    column.index = False
    column.nullable = True
    column.primary_key = False
    element.element = column
    kwargs["first_pk"] = False
    return compiler.visit_create_column(element, **kwargs)


@compiles(PrimaryKeyConstraint, "presto", "hive")
def _visit_primary_key_constraint(
    element: PrimaryKeyConstraint, compiler: DDLCompiler, **kwargs: Any
) -> Optional[str]:
    """
    Do not create primary keys for the hive and presto dialects
    """
    return DUMMY_STATEMENT


@compiles(ForeignKeyConstraint, "presto", "hive")
def _visit_foreign_key_constraint(
    element: ForeignKeyConstraint, compiler: DDLCompiler, **kwargs: Any
) -> Optional[str]:
    """
    Do not create foreign keys for the hive and presto dialects
    """
    return DUMMY_STATEMENT


@compiles(AddConstraint, "presto", "hive")
def _visit_add_constraint(
    element: AddConstraint, compiler: DDLCompiler, **kwargs: Any
) -> Optional[str]:
    """
    Do not create constraints for the presto or hive dialects.
    """
    return DUMMY_STATEMENT


@compiles(CreateIndex, "presto", "hive", "snowflake")
def _visit_create_index_presto_hive_snowflake(
    element: CreateIndex, compiler: DDLCompiler, **kwargs: Any
) -> Optional[str]:
    """
    Do not create indices for the presto, hive or snowflake dialects.
    """
    return DUMMY_STATEMENT


# endregion
# region Hive


def _iter_hive_table_options(
    table: Table,
    location: str,
    defaults: Dict[str, Union[str, Dict[str, str]]],
    exclude: Container[str] = (),
) -> Iterable[Tuple[str, Union[str, Dict[str, str]]]]:
    key: str
    value: Union[str, Dict[str, str]]
    item: Tuple[str, Union[str, Dict[str, str]]]
    dialect_option_items: Iterable[
        Tuple[str, Union[str, Dict[str, str]]]
    ] = table.dialect_options.get("hive", {}).items()
    if exclude:
        dialect_option_items = filter(
            lambda item: item[0] not in exclude, dialect_option_items
        )
    for key, value in dialect_option_items:
        if key == "location" and location:
            assert isinstance(value, str)
            value = parse.urljoin(location, value)
        defaults.pop(key, None)
        yield key, value
    # For any defaults for which no value was found, yield the default value
    for key, value in defaults.items():
        yield key, value


def _get_hive_table_arguments(
    table: Table,
    location: str,
    defaults: Dict[str, Union[str, Dict[str, str]]],
) -> str:
    return "\n".join(
        _format_hive_table_argument(key, value)
        for key, value in _iter_hive_table_options(
            table=table,
            location=location,
            defaults=defaults,
            exclude={"table_name", "TABLE_NAME"},
        )
    )


def _format_hive_table_argument_value(value: str) -> str:
    """
    Return a single-quoted string value if the value contains characters which
    are not alphanumeric or underscores, otherwise return the unmodified
    string.
    """
    if not re.match(r"^[a-zA-Z0-9_]*$", value):
        value = f"'{value}'"
    return value


def _format_hive_table_argument(
    key: str,
    value: Union[str, Sequence[str], Dict[str, str]],
) -> str:
    key = key.upper()
    if key in ("STORED_AS", "PARTITIONED_BY"):
        key = key.replace("_", " ")
    if key == "PARTITIONED BY" and isinstance(value, str):
        value = (value,)
    value_repr: str
    if isinstance(value, str):
        value_repr = _format_hive_table_argument_value(value)
    elif isinstance(value, dict):
        dict_key: str
        dict_value: str
        value_repr = "({})".format(
            ", ".join(
                "'{}' = '{}'".format(dict_key, dict_value)
                for dict_key, dict_value in value.items()
            )
        )
    elif isinstance(value, collections.abc.Iterable):
        value_repr = "({})".format(
            ", ".join(
                _format_hive_table_argument("", item).lstrip()
                for item in value
            )
        )
    else:
        value_repr = repr(value)
    return f"{key} {value_repr}"


def register_hive_create_table_compiler(
    location: str,
    stored_as: Optional[str] = None,
    tblproperties: Union[Dict[str, str], Iterable[Tuple[str, str]]] = None,
) -> None:
    """
    This function registers a compiler for `CreateTable` DDL elements which
    amends "CREATE TABLE" statements with hive-specific arguments.

    Parameters:

    - **location** (str) = None: If provided, this will be used as
      the root URL/path for tables (specified with the "LOCATION" keyword in
      the "CREATE TABLE" statement), and all "hive_location" keys in a
      mapping's `__table_args__` attribute will be joined with
      this value (if specified as relative paths or left as the default,).
    - **stored_as** (str) = "PARQUET": The default value for the
      "STORED AS" argument for "CREATE TABLE" statements.
    - **tblproperties** ({str: str}) = {"has_encrypted_data": "false",
      "classification": "parquet"}:
      This argument is used as the
      default value for the "TBLPROPERTIES" argument in "CREATE TABLE"
      statements.
    """

    @compiles(CreateTable, "hive")
    def visit_create_table(
        element: CreateTable, compiler: DDLCompiler, **kwargs: Any
    ) -> Optional[str]:
        """
        Amend "CREATE TABLE" statements with hive-specific arguments
        """
        nonlocal location
        nonlocal stored_as
        nonlocal tblproperties
        table: Table = element.element
        hive_table_name: str = get_dialect_table_name("hive", table)
        defaults: Dict[str, Union[str, Dict[str, str]]] = {}
        if stored_as is not None:
            defaults["stored_as"] = stored_as
        if tblproperties:
            if not isinstance(tblproperties, Dict):
                tblproperties = OrderedDict(tblproperties)
            defaults["tblproperties"] = tblproperties
        # If the hive table name is an empty string, return `None`, otherwise
        # return the compiled statement
        return (
            "{}\n\n".format(
                "\n".join(
                    (
                        # Replace the first occurrence of "CREATE TABLE" with
                        # "CREATE EXTERNAL TABLE"
                        re.sub(
                            r"\bCREATE\s+TABLE\b",
                            "CREATE EXTERNAL TABLE",
                            # Replace the default table name with a
                            # hive-specific table name, if applicable
                            re.sub(
                                f"\\b{table.name}\\b",
                                hive_table_name,
                                compiler.visit_create_table(element, **kwargs),
                                flags=re.IGNORECASE,
                                count=1,
                            ),
                            flags=re.IGNORECASE,
                            count=1,
                        ),
                        _get_hive_table_arguments(
                            table=table,
                            location=location,
                            defaults=defaults,
                        ),
                    )
                )
            )
            if hive_table_name
            else None
        )


# endregion
