import re
from argparse import Namespace
from functools import wraps
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
    cast,
)

import sqlalchemy  # type: ignore
from databricks.sql.client import Cursor as DatabricksCursor  # type: ignore
from databricks.sql.types import Row  # type: ignore
from databricks.sqlalchemy.dialect import DatabricksDialect  # type: ignore
from cerberus_assistant.get import get_secret
from pyspark.sql import SparkSession  # type: ignore
from sqlalchemy import Table, types  # type: ignore
from sqlalchemy.engine import CursorResult  # type: ignore
from sqlalchemy.engine.base import Connection, Engine  # type: ignore
from sqlalchemy.engine.create import (  # type: ignore  # noqa
    create_engine as _create_engine,
)
from sqlalchemy.engine.url import URL, make_url  # type: ignore
from sqlalchemy.sql.compiler import IdentifierPreparer  # type: ignore
from typing_extensions import ParamSpec, TypedDict

from .cli import parse_arguments as _parse_arguments
from .utilities import (
    get_bind_schema,
    get_dialect_identifier_preparer,
    lru_cache,
)

from databricks.sql.client import (  # type: ignore  # isort: skip
    Connection as DatabricksConnection,
)


__all__: List[str] = [
    "get_connection_url",
    "create_engine",
    "create_all",
    "patch_dialect",
]

ENVIRONMENTS: Tuple[str, ...] = ("dev", "qa", "prod", "published")
COMMANDS: Tuple[str, ...] = ("create", "drop", "validate")
DEFAULT_HOSTNAME: str = "community.cloud.databricks.com"
DEFAULT_CATALOG: str = "development"

DEV_CATALOG: str = DEFAULT_CATALOG
QA_CATALOG: str = DEV_CATALOG

_GET_COLUMNS_TYPE_MAP: Dict[str, types.TypeEngine] = {
    "boolean": sqlalchemy.types.Boolean,
    "smallint": sqlalchemy.types.SmallInteger,
    "int": sqlalchemy.types.Integer,
    "bigint": sqlalchemy.types.BigInteger,
    "float": sqlalchemy.types.Float,
    "double": sqlalchemy.types.Float,
    "string": sqlalchemy.types.String,
    "varchar": sqlalchemy.types.String,
    "char": sqlalchemy.types.String,
    "binary": sqlalchemy.types.String,
    "array": sqlalchemy.types.String,
    "map": sqlalchemy.types.String,
    "struct": sqlalchemy.types.String,
    "uniontype": sqlalchemy.types.String,
    "decimal": sqlalchemy.types.Numeric,
    "date": sqlalchemy.types.Date,
    "timestamp": sqlalchemy.types.TIMESTAMP,
}


"""
TODO: Refactor this - it's pretty slow
The current version of the databricks sqlalchemy dialect makes use of
DESCRIBE TABLE EXTENDED, which requires parsing the output with regex.

See: https://github.com/databricks/databricks-sql-python/blob/v3.0.1/src/databricks/sqlalchemy/base.py#L222  # noqa

"""
_CONSTRAINT_STATEMENT: str = """
with key_column_usage as (
    select
    constraint_catalog,
    constraint_schema,
    constraint_name,
    table_name,
    column_name,
    ordinal_position,
    position_in_unique_constraint
    from information_schema.key_column_usage
),
all_constraints as (
    select
    key_column_usage.constraint_catalog,
    key_column_usage.constraint_schema,
    key_column_usage.constraint_name,
    table_constraints.constraint_type,
    key_column_usage.table_name,
    key_column_usage.column_name,
    key_column_usage.ordinal_position,
    constraint_table_usage.table_name as referenced_table,
    referenced_key_column_usage.column_name as referenced_column,
    referenced_key_column_usage.constraint_schema as referenced_schema
    from key_column_usage
    left join information_schema.constraint_table_usage
    on key_column_usage.constraint_catalog
      = constraint_table_usage.constraint_catalog
    and key_column_usage.constraint_schema
      = constraint_table_usage.constraint_schema
    and key_column_usage.constraint_name
      = constraint_table_usage.constraint_name
    join information_schema.table_constraints
    on key_column_usage.constraint_catalog
      = table_constraints.constraint_catalog
    and key_column_usage.constraint_schema
      = table_constraints.constraint_schema
    and key_column_usage.constraint_name
      = table_constraints.constraint_name
    left join information_schema.referential_constraints
    on table_constraints.constraint_name
      = referential_constraints.constraint_name
    and table_constraints.constraint_schema
      = referential_constraints.constraint_schema
    and table_constraints.constraint_catalog
      = referential_constraints.constraint_catalog
    left join key_column_usage as referenced_key_column_usage
    on referenced_key_column_usage.constraint_name
      = referential_constraints.unique_constraint_name
    and referenced_key_column_usage.constraint_catalog
      = referential_constraints.constraint_catalog
    and referenced_key_column_usage.constraint_schema
      = referential_constraints.constraint_schema
    and referenced_key_column_usage.ordinal_position
      = key_column_usage.position_in_unique_constraint
)
select * from all_constraints
where constraint_schema = %(schema)s
and constraint_type in ('PRIMARY KEY', 'FOREIGN KEY')
order by ordinal_position asc
"""


class _ReflectedConstraint(TypedDict):
    name: Optional[str]


class _ReflectedPrimaryKeyConstraint(_ReflectedConstraint):
    constrained_columns: List[str]


class _ReflectedForeignKeyConstraint(_ReflectedConstraint):
    constrained_columns: List[str]
    referred_schema: str
    referred_table: str
    referred_columns: List[str]


class _ReflectedColumn(TypedDict):
    name: str
    type: types.TypeEngine
    nullable: bool
    default: Optional[str]


class _ReflectedIndex:
    name: Optional[str]
    column_names: List[Optional[str]]
    expressions: List[str]
    unique: Optional[bool]  # Not supported by Databricks
    duplicates_constraint: Optional[str]
    include_columns: Optional[List[str]]
    column_sorting: Optional[Dict[str, Tuple[str]]]
    dialect_options: Dict[str, Any]


_DatabricksParamSpec = ParamSpec("_DatabricksParamSpec")


def get_connection_url(
    http_path: str = "",
    hostname: str = DEFAULT_HOSTNAME,
    access_token: str = "",
    catalog: str = DEFAULT_CATALOG,
    schema: str = "",
    access_token_cerberus_path: str = "",
) -> URL:
    if access_token_cerberus_path and not access_token:
        access_token = get_secret(access_token_cerberus_path)
    if not http_path:
        # `sparkContext.getConf()` isn't supported on clusters of 'Shared'
        # access type, so, any cluster used here will need to be Single-User
        # or a job cluster.
        spark: SparkSession = SparkSession.builder.getOrCreate()
        print("No http path found")
        org_id: str = spark.sparkContext.getConf().get(
            "spark.databricks.clusterUsageTags.orgId", ""
        )
        cluster_id: str = spark.sparkContext.getConf().get(
            "spark.databricks.clusterUsageTags.clusterId", ""
        )
        assert org_id and cluster_id
        http_path = f"/sql/protocolv1/o/{org_id}/{cluster_id}"
    assert http_path, "A cluster HTTP path is required to connect."
    return make_url(
        f"databricks://token:{access_token}@{hostname}"
        f"?http_path={http_path}&catalog={catalog}&schema={schema}"
    )


# For backwards compatibility
get_connection_string: Callable = get_connection_url


@lru_cache()
def create_engine(
    http_path: str = "",
    hostname: str = DEFAULT_HOSTNAME,
    access_token: str = "",
    catalog: str = DEFAULT_CATALOG,
    schema: str = "",
    access_token_cerberus_path: str = "",
    echo: bool = True,
) -> Engine:
    engine: Engine = _create_engine(
        get_connection_url(
            http_path=http_path,
            hostname=hostname,
            access_token=access_token,
            catalog=catalog,
            schema=schema,
            access_token_cerberus_path=access_token_cerberus_path,
        ),
        echo=echo,
    )

    return engine


def create_all(
    declarative_base: type,
    http_path: str = "",
    hostname: str = DEFAULT_HOSTNAME,
    access_token: str = "",
    catalog: str = DEFAULT_CATALOG,
    schema: str = "",
    access_token_cerberus_path: str = "",
    echo: bool = False,
    views_only: bool = False,
    tables: Optional[Iterable[Table]] = None,
    checkfirst: bool = True,
    bind: Union[Engine, Connection, None] = None,
) -> Engine:
    if not bind:
        bind = create_engine(
            http_path=http_path,
            hostname=hostname,
            access_token=access_token,
            catalog=catalog,
            schema=schema,
            access_token_cerberus_path=access_token_cerberus_path,
            echo=echo,
        )

    if views_only and not tables:
        declarative_base.metadata.create_views(  # type: ignore
            bind=bind, checkfirst=checkfirst
        )
    else:
        declarative_base.metadata.create_all(  # type: ignore
            bind=bind, checkfirst=checkfirst, tables=tables
        )


def drop_all(
    declarative_base: type,
    http_path: str = "",
    hostname: str = DEFAULT_HOSTNAME,
    access_token: str = "",
    catalog: str = DEFAULT_CATALOG,
    schema: str = "",
    access_token_cerberus_path: str = "",
    echo: bool = False,
    views_only: bool = False,
    tables: Optional[Iterable[Table]] = None,
    checkfirst: bool = True,
    bind: Union[Engine, Connection, None] = None,
    undeclared: bool = True,
    undeclared_only: bool = False,
) -> Engine:
    if not bind:
        bind = create_engine(
            http_path=http_path,
            hostname=hostname,
            access_token=access_token,
            catalog=catalog,
            schema=schema,
            access_token_cerberus_path=access_token_cerberus_path,
            echo=echo,
        )
    if undeclared or undeclared_only:
        declarative_base.metadata.drop_undeclared(bind=bind)  # type: ignore
        if undeclared_only:
            return bind
    if views_only and not tables:
        declarative_base.metadata.drop_views(  # type: ignore
            bind=bind, checkfirst=checkfirst
        )
    else:
        declarative_base.metadata.drop_all(  # type: ignore
            bind=bind, checkfirst=checkfirst, tables=tables
        )


def parse_arguments(
    prog: str = "",
    environments: Sequence[str] = ENVIRONMENTS,
    commands: Sequence[str] = COMMANDS,
    include: Iterable[str] = (
        "access_token",
        "access_token_cerberus_path",
        "hostname",
        "http_path",
        "checkfirst",
        "command",
        "echo",
        "environment",
        "log",
        "catalog",
        "only_validate",
        "schema",
        "undeclared_only",
        "undeclared",
        "views_only",
        "exclude_from_cache_validation",
        "ignore_foreign_key",
        "only_validate",
    ),
) -> Namespace:
    """
    Parse Databricks CLI arguments and return the resulting instance of
    `argparse.Namespace`.

    Parameters:

    - prog (str): The CLI command or command + sub-command
      triggering this function. For example:
      "my-datastore-orm databricks".
    - environments ([str]) = ("dev", "qa", "prod"): The environment names
      to consider valid
    - commands ([str]) = ("dev", "qa", "prod"):
      Valid values for the `command` argument. If an empty tuple/list is
      provided, no "command" argument is added to the parser
    - include ({str}): An iterable of the names of all parameters to include.
      If not provided, *all* parameters are used

    This function returns a `Namespace` object with properties corresponding
    to those specified in the `include` argument.
    """
    return _parse_arguments(
        prog=prog,
        environments=environments,
        commands=commands,
        include=include,
    )


# region Patch Dialect


# Save a reference to unpatched methods
_original_databricks_dialect_get_table_names: Callable[
    _DatabricksParamSpec, List[str]
] = DatabricksDialect.get_table_names
_original_databricks_dialect_get_view_names: Callable[
    _DatabricksParamSpec, List[str]
] = DatabricksDialect.get_view_names
_original_databricks_dialect_has_table: Callable[
    _DatabricksParamSpec, bool
] = DatabricksDialect.has_table


def _databricks_dialect_has_table(
    self: DatabricksDialect,
    connection: Connection,
    table_name: str,
    schema: Optional[str] = None,
    **kwargs: Any,
) -> bool:
    if len(table_name) == 0:
        return False
    return _original_databricks_dialect_has_table(
        self, connection, table_name, schema, **kwargs
    )


@wraps(DatabricksDialect.get_pk_constraint)
def _databricks_dialect_get_pk_constraint(
    self: DatabricksDialect,
    connection: Connection,
    table_name: str,
    schema: Optional[str] = None,
    **kwargs: Any,
) -> Optional[_ReflectedPrimaryKeyConstraint]:
    if not schema:
        schema = get_bind_schema(connection.engine)
    assert schema, repr(locals())
    primary_key_constraints: Tuple[_ReflectedPrimaryKeyConstraint, ...] = (
        tuple(
            _databricks_dialect_get_schema_constraints(connection, schema)
            .get("PRIMARY KEY", {})
            .get(table_name, {})
            .values()
        )
    )
    return primary_key_constraints[0] if primary_key_constraints else None


@lru_cache()
def _databricks_dialect_get_schema_constraints(
    connection: Connection,
    schema: str,
) -> Dict[
    str,
    Dict[
        str,
        Dict[
            str,
            Union[
                _ReflectedForeignKeyConstraint, _ReflectedPrimaryKeyConstraint
            ],
        ],
    ],
]:
    preparer: IdentifierPreparer = get_dialect_identifier_preparer(
        "databricks"
    )
    contraint_types_tables_constraints: Dict[
        str,
        Dict[
            str,
            Dict[
                str,
                Union[
                    _ReflectedForeignKeyConstraint,
                    _ReflectedPrimaryKeyConstraint,
                ],
            ],
        ],
    ] = {}
    result: CursorResult = connection.execute(
        _CONSTRAINT_SELECT_STATEMENT, {"schema": preparer.quote(schema)}
    )
    row: Row
    for row in result:
        # Databricks stores constraints as uppercase, but the
        # metadata naming convention produces uppercase names,
        # so when reflecting we convert the names to uppercase to
        # produce correct matches for comparison
        constraint_name: str = row.constraint_name.upper()
        if row.constraint_type not in contraint_types_tables_constraints:
            contraint_types_tables_constraints[row.constraint_type] = {}
        if (
            row.table_name
            not in contraint_types_tables_constraints[row.constraint_type]
        ):
            contraint_types_tables_constraints[row.constraint_type][
                row.table_name
            ] = {}
        if (
            constraint_name
            not in contraint_types_tables_constraints[row.constraint_type][
                row.table_name
            ]
        ):
            if row.constraint_type == "FOREIGN KEY":
                contraint_types_tables_constraints[row.constraint_type][
                    row.table_name
                ][constraint_name] = _ReflectedForeignKeyConstraint(
                    name=constraint_name,
                    constrained_columns=[row.column_name],
                    referred_schema=row.referenced_schema,
                    referred_table=row.referenced_table,
                    referred_columns=[row.referenced_column],
                )
            if row.constraint_type == "PRIMARY KEY":
                contraint_types_tables_constraints[row.constraint_type][
                    row.table_name
                ][constraint_name] = _ReflectedPrimaryKeyConstraint(
                    name=constraint_name,
                    constrained_columns=[row.column_name],
                )
        else:
            contraint_types_tables_constraints[row.constraint_type][
                row.table_name
            ][constraint_name]["constrained_columns"].append(row.column_name)
            if row.constraint_type == "FOREIGN KEY":
                cast(
                    _ReflectedForeignKeyConstraint,
                    contraint_types_tables_constraints[row.constraint_type][
                        row.table_name
                    ][constraint_name],
                )["referred_columns"].append(row.referenced_column)
    return contraint_types_tables_constraints


@wraps(DatabricksDialect.get_foreign_keys)
def _databricks_dialect_get_foreign_keys(
    self: DatabricksDialect,
    connection: Connection,
    table_name: str,
    schema: Optional[str] = None,
    **kwargs: Any,
) -> Iterable[_ReflectedForeignKeyConstraint]:
    if not schema:
        schema = get_bind_schema(connection.engine)
    assert schema, repr(locals())
    yield from _databricks_dialect_get_schema_constraints(
        connection, schema
    ).get("FOREIGN KEY", {}).get(table_name, {}).values()


_PRECISION_SCALE_PATTERN: re.Pattern = re.compile(r"DECIMAL\((\d+,\d+)\)")


@wraps(DatabricksDialect.get_columns)
def _databricks_dialect_get_columns(
    self: DatabricksDialect,
    connection: Connection,
    table_name: str,
    schema: Optional[str] = None,
    **kwargs: Any,
) -> List[_ReflectedColumn]:
    """
    The provided `get_columns` method in the Databricks dialect
    does not have support for returning column information for columns
    that have precision and scale. This method overrides the default
    `get_columns` method to add support for columns with precision and
    scale.
    """
    # Pattern to extract the raw column type from the full type name
    # where the full name contains parenthesis (e.g. DECIMAL(38,4) -> decimal)
    raw_column_name_pattern: re.Pattern = re.compile(r"\w+")

    def _get_numeric_with_precision_and_scale(
        type_name: str,
    ) -> types.Numeric:
        """
        Given a type name with precision and scale,
        return a sqlalchemy.types.Numeric instance
        with the extracted precision and scale
        """
        precision_scale_match: Optional[re.Match] = re.search(
            _PRECISION_SCALE_PATTERN, type_name
        )
        numeric: types.Numeric = types.Numeric()
        precision: int
        scale: int
        if precision_scale_match:
            precision, scale = map(
                int, precision_scale_match.group(1).split(",")
            )
            numeric = types.Numeric(precision=precision, scale=scale)
        return numeric

    databricks_connection: DatabricksConnection = connection.connection
    databricks_cursor: DatabricksCursor = databricks_connection.cursor()
    columns_response: List[Row] = databricks_cursor.columns(
        table_name=table_name,
        schema_name=schema,
        catalog_name=self.catalog,
    ).fetchall()
    column: Row
    columns: List[_ReflectedColumn] = []
    for column in columns_response:
        raw_column_type_matched: Optional[re.Match] = re.search(
            raw_column_name_pattern, column.TYPE_NAME
        )
        raw_column_type: str = column.TYPE_NAME
        if raw_column_type_matched:
            raw_column_type = raw_column_type_matched.group(0)
        raw_column_type = raw_column_type.lower()
        column_type: types.TypeEngine = _GET_COLUMNS_TYPE_MAP[raw_column_type]
        if raw_column_type == "decimal":
            column_type = _get_numeric_with_precision_and_scale(
                column.TYPE_NAME
            )
        columns.append(
            _ReflectedColumn(
                name=column.COLUMN_NAME,
                type=column_type,
                nullable=bool(column.NULLABLE),
                default=column.COLUMN_DEF,
            )
        )
    return columns


@wraps(DatabricksDialect.get_indexes)
def _databricks_dialect_get_indexes(
    self: DatabricksDialect,
    connection: Connection,
    table_name: str,
    schema: Optional[str] = None,
    **kwargs: Any,
) -> List[_ReflectedIndex]:
    """
    Indices aren't supported by Databricks, so always return
    an empty list.
    """
    return []


@lru_cache()
def patch_dialect() -> None:
    """
    This function patches the dialects to facilitate schema reflection
    and alembic migrations
    """
    DatabricksDialect.get_pk_constraint = _databricks_dialect_get_pk_constraint
    DatabricksDialect.get_foreign_keys = _databricks_dialect_get_foreign_keys
    DatabricksDialect.get_indexes = _databricks_dialect_get_indexes
    DatabricksDialect.has_table = _databricks_dialect_has_table
    DatabricksDialect.get_columns = _databricks_dialect_get_columns


patch_dialect()

# endregion
