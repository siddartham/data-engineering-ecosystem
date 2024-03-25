import logging
from argparse import Namespace
from functools import update_wrapper, wraps
from getpass import getuser
from typing import (
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from org.cerberus_assistant.get import get_secret
from snowflake.sqlalchemy import URL as snowflake_url  # type: ignore
from snowflake.sqlalchemy.snowdialect import SnowflakeDialect  # type: ignore
from snowflake.sqlalchemy.snowdialect import check_table  # type: ignore
from sqlalchemy import Table  # type: ignore
from sqlalchemy.engine.base import Connection, Engine  # type: ignore
from sqlalchemy.engine.create import (
    create_engine as _create_engine,  # type: ignore
)
from sqlalchemy.engine.interfaces import Dialect  # type: ignore
from sqlalchemy.engine.row import Row  # type: ignore
from sqlalchemy.engine.url import URL, make_url  # type: ignore
from sqlalchemy.event.api import remove  # type: ignore
from sqlalchemy.sql import quoted_name  # type: ignore
from sqlalchemy.sql.compiler import IdentifierPreparer  # type: ignore

from .cli import parse_arguments as _parse_arguments
from .config import OKTA_URL
from .utilities import is_current_user_human, lru_cache

# This import is needed in order for Alembic to support database-specific
# behaviors
SnowflakeImpl: type
try:
    from .alembic.snowflake import SnowflakeImpl
except ImportError:
    SnowflakeImpl = object


__all__: List[str] = [
    "get_connection_url",
    "create_engine",
    "create_all",
    "parse_arguments",
    "patch_dialect",
    "DEFAULT_SCHEMA",
    "DEFAULT_STAGE_FILE_FORMAT",
]
ACCOUNT: str = "org"
DEFAULT_SCHEMA: str = "INFORMATION_SCHEMA"
DEFAULT_PORT: int = 443
DEFAULT_ROLE: str = "ALL"
DEFAULT_STAGE_FILE_FORMAT: str = (
    "(type=parquet trim_space=true null_if=('') binary_as_text=true)"
)
ENVIRONMENTS: Tuple[str, str, str] = ("dev", "qa", "prod")
DEFAULT_ENVIRONMENTS = ENVIRONMENTS  # for backwards compatibility
COMMANDS: Tuple[str, ...] = ("create", "drop", "validate")
_EXTERNAL_BROWSER: str = "externalbrowser"


@dataclass
class CreateStageArguments:
    """
    Properties:

    - name (str): The fully-qualified name of the stage (including schema)
    - file_format (str)
    - storage_integration (str): The name of the storage integration to use
    - url (str): The base URL for the storage integration
    """

    name: str
    storage_integration: str
    url: str
    file_format: str = DEFAULT_STAGE_FILE_FORMAT


# Remove this listener, as indexes are simply ignored for Snowflake,
# we don't want/need to raise an error
remove(Table, "before_create", check_table)


def _get_connection_string_optional_kwargs(
    password: str, role: str, schema: str
) -> Dict[str, str]:
    """
    These optional keyword arguments should not be passed to `URL` if
    they are just empty strings, so we assemble them as variable keywords
    """
    optional_kwargs: Dict[str, str] = {}
    if password:
        optional_kwargs.update(password=password)
    if role:
        optional_kwargs.update(role=role)
    if schema:
        optional_kwargs.update(schema=schema)
    return optional_kwargs


def _get_authenticator(
    authenticator: str, authenticator_cerberus_path: str
) -> str:
    """
    Determine the authenticator to be used based on explicit input,
    Cerberus secrets, and/or inference based on whether the user is human
    or not
    """
    # If an authenticator is not specified, infer one...
    if authenticator:
        assert authenticator in (OKTA_URL, _EXTERNAL_BROWSER)
    elif is_current_user_human():
        authenticator = _EXTERNAL_BROWSER
    elif authenticator_cerberus_path:
        authenticator = get_secret(authenticator_cerberus_path)
    else:
        authenticator = OKTA_URL
    return authenticator


def get_connection_url(
    user: str = "",
    password: str = "",
    database: str = "",
    warehouse: str = "",
    schema: str = DEFAULT_SCHEMA,
    role: str = DEFAULT_ROLE,
    authenticator: str = "",
    user_cerberus_path: str = "",
    password_cerberus_path: str = "",
    database_cerberus_path: str = "",
    warehouse_cerberus_path: str = "",
    schema_cerberus_path: str = "",
    role_cerberus_path: str = "",
    authenticator_cerberus_path: str = "",
) -> URL:
    """
    This function assembles and returns a snowflake connection string.

    Parameters:

    - **user** (str) = "": A username with which to authenticate
    - **password** (str) = "": A password with which to authenticate
    - **database** (str) = ""
    - **warehouse** (str) = ""
    - **schema** (str) = "INFORMATION_SCHEMA": A schema name.
    - **role** (str) = "ALL": A Snowflake role to be assumed, or "ALL" (the
      default).
    - **authenticator** (str) = "": Either "https://org.okta.com" or
      "externalbrowser", if provided, otherwise this will be determined to
      be "externalbrowser" for human users, and "https://org.okta.com" for
      service accounts (GIDs).

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of Org's [vaults](https://prod.cerberus.orgcloud.com). For
    example: "app/division/snowlake-prod/password".

    - **user_cerberus_path** (str) = ""
    - **password_cerberus_path** (str) = ""
    - **database_cerberus_path** (str) = ""
    - **warehouse_cerberus_path** (str) = ""
    - **schema_cerberus_path** (str) = ""
    - **role_cerberus_path** (str) = ""
    - **authenticator_cerberus_path** (str) = ""
    """
    # Determine the authentication method to use
    authenticator = _get_authenticator(
        authenticator=authenticator,
        authenticator_cerberus_path=authenticator_cerberus_path,
    )
    # If using browser authentication, we need to use the logged-in
    # user's ID
    if authenticator == _EXTERNAL_BROWSER and not user:
        user = getuser().split("\\")[-1]
    else:
        key: str
        if user_cerberus_path and not user:
            user = get_secret(user_cerberus_path)
        if password_cerberus_path and not password:
            key = password_cerberus_path.rpartition("/")[-1]
            password = get_secret(password_cerberus_path)
            if not user:
                user = key
    # Lookup other Cerberus secrets, where needed
    if database_cerberus_path and not database:
        database = get_secret(database_cerberus_path)
    if warehouse_cerberus_path and not warehouse:
        warehouse = get_secret(warehouse_cerberus_path)
    if schema_cerberus_path and (schema == DEFAULT_SCHEMA or (not schema)):
        schema = get_secret(schema_cerberus_path)
    if role_cerberus_path and (role == DEFAULT_ROLE or (not role)):
        role = get_secret(role_cerberus_path)
    return make_url(
        snowflake_url(
            account=ACCOUNT,
            warehouse=warehouse,
            database=database,
            authenticator=authenticator,
            user=user,
            **_get_connection_string_optional_kwargs(
                password=password, role=role, schema=schema
            ),
            interpolate_empty_sequences=True,
        )
    )


# For backwards compatibility
get_connection_string: Callable = get_connection_url


@lru_cache()
def create_engine(
    user: str = "",
    password: str = "",
    database: str = "",
    warehouse: str = "",
    schema: str = DEFAULT_SCHEMA,
    role: str = DEFAULT_ROLE,
    authenticator: str = "",
    user_cerberus_path: str = "",
    password_cerberus_path: str = "",
    database_cerberus_path: str = "",
    warehouse_cerberus_path: str = "",
    schema_cerberus_path: str = "",
    role_cerberus_path: str = "",
    authenticator_cerberus_path: str = "",
    echo: bool = False,
    use_secondary_roles: bool = True,
) -> Engine:
    engine: Engine = _create_engine(
        get_connection_url(
            user=user,
            password=password,
            database=database,
            warehouse=warehouse,
            schema=schema,
            role=role,
            authenticator=authenticator,
            user_cerberus_path=user_cerberus_path,
            password_cerberus_path=password_cerberus_path,
            database_cerberus_path=database_cerberus_path,
            warehouse_cerberus_path=warehouse_cerberus_path,
            schema_cerberus_path=schema_cerberus_path,
            role_cerberus_path=role_cerberus_path,
            authenticator_cerberus_path=authenticator_cerberus_path,
        ),
        echo=echo,
    )
    if use_secondary_roles:
        # We commit first, in order to ensure the subsequent statement executes
        # outside of a transaction
        connection: Connection = engine.connect()
        # connection.execute("COMMIT", ())
        connection.execute(text("COMMIT"), ())
        # See Snowflake documentation for
        # [USE SECONDARY ROLES](https://bit.ly/3o9y3XN)
        # concerning implications of the following statement
        connection.execute(text("USE SECONDARY ROLES ALL"), ())
    return engine


def create_stage(
    user: str = "",
    password: str = "",
    database: str = "",
    warehouse: str = "",
    schema: str = DEFAULT_SCHEMA,
    role: str = DEFAULT_ROLE,
    authenticator: str = "",
    echo: bool = False,
    stage_name: str = "",
    stage_file_format: str = DEFAULT_STAGE_FILE_FORMAT,
    stage_url: str = "",
    stage_storage_integration: str = "",
    user_cerberus_path: str = "",
    password_cerberus_path: str = "",
    database_cerberus_path: str = "",
    warehouse_cerberus_path: str = "",
    schema_cerberus_path: str = "",
    role_cerberus_path: str = "",
    authenticator_cerberus_path: str = "",
    bind: Union[Engine, Connection, None] = None,
    use_secondary_roles: bool = True,
    create_stage_arguments: Tuple[CreateStageArguments, ...] = (),
) -> Engine:
    """
    Stage Creation Parameters:

    - stage_name (str)
    - stage_file_format (str)
    - stage_storage_integration (str)
    - stage_url (str)
    - create_stage_arguments
      ((orm_framework.snowflake.CreateStageArguments,)) = ():
      A sequence of stage creation arguments for use in creating more than one
      stage in the same database + schema

    Connection Parameters:

    - user (str) = "": A username with which to authenticate
    - password (str) = "": A password with which to authenticate
    - database (str) = ""
    - warehouse (str) = ""
    - schema (str) = "INFORMATION_SCHEMA": A schema name.
    - role (str) = "ALL": A Snowflake role to be assumed, or "ALL" (the
      default).
    - authenticator (str) = "": Either "https://org.okta.com" or
      "externalbrowser", if provided, otherwise this will be determined to
      be "externalbrowser" for human users, and "https://org.okta.com" for
      service accounts (GIDs).
    - use_secondary_roles (bool) = True
    - bind (sqlalchemy.Engine|sqlalchemy.Connection|None) = None

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of Org's [vaults](https://prod.cerberus.cloud.com). For
    example: "app/org/snowlake-prod/password".

    - user_cerberus_path (str) = ""
    - password_cerberus_path (str) = ""
    - database_cerberus_path (str) = ""
    - warehouse_cerberus_path (str) = ""
    - schema_cerberus_path (str) = ""
    - role_cerberus_path (str) = ""
    - authenticator_cerberus_path (str) = ""
    """
    if (
        stage_name
        and stage_url
        and stage_file_format
        and stage_storage_integration
    ):
        create_stage_arguments = (
            CreateStageArguments(
                name=stage_name,
                file_format=stage_file_format,
                storage_integration=stage_storage_integration,
                url=stage_url,
            ),
        ) + create_stage_arguments
    else:
        assert create_stage_arguments and isinstance(
            create_stage_arguments[0], CreateStageArguments
        )
    if not bind:
        bind = create_engine(
            user=user,
            password=password,
            database=database,
            warehouse=warehouse,
            schema=schema,
            role=role,
            authenticator=authenticator,
            echo=echo,
            user_cerberus_path=user_cerberus_path,
            password_cerberus_path=password_cerberus_path,
            database_cerberus_path=database_cerberus_path,
            warehouse_cerberus_path=warehouse_cerberus_path,
            schema_cerberus_path=schema_cerberus_path,
            role_cerberus_path=role_cerberus_path,
            authenticator_cerberus_path=authenticator_cerberus_path,
            use_secondary_roles=use_secondary_roles,
        )
    command: str
    arguments: CreateStageArguments
    for arguments in create_stage_arguments:
        command = (
            f"create or replace stage {arguments.name} "
            f"url='{arguments.url}' "
            f"file_format={arguments.file_format} "
            f"storage_integration={arguments.storage_integration}"
        )
        logging.info(command)
        response: str
        for response in bind.execute(command):
            logging.info(response)
    return bind


def create_all(
    declarative_base: type,
    user: str = "",
    password: str = "",
    database: str = "",
    warehouse: str = "",
    schema: str = DEFAULT_SCHEMA,
    role: str = DEFAULT_ROLE,
    authenticator: str = "",
    echo: bool = False,
    checkfirst: bool = True,
    views_only: bool = False,
    tables: Optional[Iterable[Table]] = None,
    stage_name: str = "",
    stage_file_format: str = DEFAULT_STAGE_FILE_FORMAT,
    stage_url: str = "",
    stage_storage_integration: str = "",
    user_cerberus_path: str = "",
    password_cerberus_path: str = "",
    database_cerberus_path: str = "",
    warehouse_cerberus_path: str = "",
    schema_cerberus_path: str = "",
    role_cerberus_path: str = "",
    authenticator_cerberus_path: str = "",
    bind: Union[Engine, Connection, None] = None,
    use_secondary_roles: bool = True,
    create_stage_arguments: Tuple[CreateStageArguments, ...] = (),
) -> Engine:
    if checkfirst and not bind:
        # Connect to Snowflake without specifying a database
        connection: Connection = create_engine(
            user=user,
            password=password,
            warehouse=warehouse,
            schema=schema,
            role=role,
            authenticator=authenticator,
            echo=echo,
            user_cerberus_path=user_cerberus_path,
            password_cerberus_path=password_cerberus_path,
            database_cerberus_path=database_cerberus_path,
            warehouse_cerberus_path=warehouse_cerberus_path,
            schema_cerberus_path=schema_cerberus_path,
            role_cerberus_path=role_cerberus_path,
            authenticator_cerberus_path=authenticator_cerberus_path,
            use_secondary_roles=use_secondary_roles,
        ).connect()
        # Get the database name that will actually be used
        if database_cerberus_path and not database:
            database = get_secret(database_cerberus_path)

        def get_name(row: Row) -> str:
            return row.name.lower()

        if database.lower() not in map(
            get_name,
                connection.execute(text("SHOW DATABASES"), ()),
        ):
            dialect: Dialect = connection.engine.dialect
            preparer_class: Type[IdentifierPreparer] = getattr(
                dialect, "preparer"
            )
            preparer: IdentifierPreparer = preparer_class(dialect=dialect)
            connection.execute(text("COMMIT", ()))
            connection.execute(
                text(f"CREATE DATABASE {preparer.quote(database)}"), ()
            )
        connection.close()
    if not bind:
        # Create the engine connecting to our selected database
        bind = create_engine(
            user=user,
            password=password,
            database=database,
            warehouse=warehouse,
            schema=schema,
            role=role,
            authenticator=authenticator,
            echo=echo,
            user_cerberus_path=user_cerberus_path,
            password_cerberus_path=password_cerberus_path,
            database_cerberus_path=database_cerberus_path,
            warehouse_cerberus_path=warehouse_cerberus_path,
            schema_cerberus_path=schema_cerberus_path,
            role_cerberus_path=role_cerberus_path,
            authenticator_cerberus_path=authenticator_cerberus_path,
            use_secondary_roles=use_secondary_roles,
        )
    if views_only and not tables:
        # Create schemas and views
        declarative_base.metadata.create_views(  # type: ignore
            bind=bind,
            checkfirst=checkfirst,
        )
    else:
        # Create schemas, tables, and views
        declarative_base.metadata.create_all(  # type: ignore
            bind=bind, checkfirst=checkfirst, tables=tables
        )
    if (
        stage_name
        and stage_storage_integration
        and stage_url
        and stage_file_format
    ) or create_stage_arguments:
        create_stage(
            user=user,
            password=password,
            database=database,
            warehouse=warehouse,
            schema=schema,
            role=role,
            authenticator=authenticator,
            echo=echo,
            stage_name=stage_name,
            stage_file_format=stage_file_format,
            stage_url=stage_url,
            stage_storage_integration=stage_storage_integration,
            user_cerberus_path=user_cerberus_path,
            password_cerberus_path=password_cerberus_path,
            database_cerberus_path=database_cerberus_path,
            warehouse_cerberus_path=warehouse_cerberus_path,
            schema_cerberus_path=schema_cerberus_path,
            role_cerberus_path=role_cerberus_path,
            authenticator_cerberus_path=authenticator_cerberus_path,
            bind=bind,
            use_secondary_roles=use_secondary_roles,
        )
    return bind


def drop_all(
    declarative_base: type,
    user: str = "",
    password: str = "",
    database: str = "",
    warehouse: str = "",
    schema: str = DEFAULT_SCHEMA,
    role: str = DEFAULT_ROLE,
    authenticator: str = "",
    echo: bool = False,
    checkfirst: bool = True,
    views_only: bool = False,
    tables: Optional[Iterable[Table]] = None,
    user_cerberus_path: str = "",
    password_cerberus_path: str = "",
    database_cerberus_path: str = "",
    warehouse_cerberus_path: str = "",
    schema_cerberus_path: str = "",
    role_cerberus_path: str = "",
    authenticator_cerberus_path: str = "",
    bind: Union[Engine, Connection, None] = None,
    undeclared: bool = True,
    undeclared_only: bool = False,
    use_secondary_roles: bool = True,
) -> Engine:
    if not bind:
        # Create the engine connecting to our selected database
        bind = create_engine(
            user=user,
            password=password,
            database=database,
            warehouse=warehouse,
            schema=schema,
            role=role,
            authenticator=authenticator,
            echo=echo,
            user_cerberus_path=user_cerberus_path,
            password_cerberus_path=password_cerberus_path,
            database_cerberus_path=database_cerberus_path,
            warehouse_cerberus_path=warehouse_cerberus_path,
            schema_cerberus_path=schema_cerberus_path,
            role_cerberus_path=role_cerberus_path,
            authenticator_cerberus_path=authenticator_cerberus_path,
            use_secondary_roles=use_secondary_roles,
        )
    if undeclared or undeclared_only:
        declarative_base.metadata.drop_undeclared(bind=bind)  # type: ignore
        if undeclared_only:
            return bind
    if views_only and not tables:
        # Drop schemas and views
        declarative_base.metadata.drop_views(  # type: ignore
            bind=bind,
            checkfirst=checkfirst,
        )
    else:
        # Drop schemas, tables, and views
        declarative_base.metadata.drop_all(  # type: ignore
            bind=bind, checkfirst=checkfirst, tables=tables
        )
    return bind


@lru_cache()
def patch_dialect(
    snowflake_dialect_class: Type[SnowflakeDialect] = SnowflakeDialect,
) -> None:
    """
    This function causes Snowflake entity names to be rendered as uppercase
    rather than lowercase
    """
    # Note: This function is cached, intentionally, to prevent reuse.

    def normalize_name(
        self: SnowflakeDialect, name: Optional[str]
    ) -> Optional[str]:
        """
        This function overrides `SnowflakeDialect.normalize_name` in order to
        cause entity names to be rendered as UPPERCASE rather than lowercase,
        by default.
        """
        if name is None:
            return None
        if name.lower() == name and not (
            getattr(self.identifier_preparer, "_requires_quotes")(name.upper())
        ):
            name = name.upper()
        elif name.upper() == name:
            name = quoted_name(name, quote=True)
        else:
            name = name
        return name

    update_wrapper(normalize_name, snowflake_dialect_class.normalize_name)
    snowflake_dialect_class.normalize_name = normalize_name


def parse_arguments(
    prog: str = "",
    environments: Sequence[str] = DEFAULT_ENVIRONMENTS,
    roles: Sequence[str] = (),
    commands: Sequence[str] = COMMANDS,
    include: Iterable[str] = (
        "authenticator_cerberus_path",
        "authenticator",
        "checkfirst",
        "command",
        "database_cerberus_path",
        "database",
        "dont_use_secondary_roles",
        "echo",
        "environment",
        "exclude_from_cache_validation",
        "ignore_foreign_key",
        "log",
        "only_validate",
        "password_cerberus_path",
        "password",
        "role_cerberus_path",
        "role",
        "schema_cerberus_path",
        "schema",
        "stage_file_format",
        "stage_name",
        "stage_storage_integration",
        "stage_url",
        "undeclared_only",
        "undeclared",
        "user_cerberus_path",
        "user",
        "views_only",
        "warehouse_cerberus_path",
        "warehouse",
    ),
) -> Namespace:
    """
    Parse Snowflake CLI arguments and return the resulting instance of
    `argparse.Namespace`.

    Parameters:

    - prog (str): The CLI command or command + sub-command
      triggering this function. For example:
      "my-datastore-orm snowflake".
    - environments ([str]) = ("dev", "qa", "prod"): The environment names
      to consider valid
    - roles ([str]) = (): The roles to consider valid. If none are provided,
      any value is considered valid for this argument
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
        roles=roles,
        commands=commands,
        include=include,
    )


# region Patch Dialect


@wraps(SnowflakeDialect.normalize_name)
def _snowflake_dialect_normalize_name(
    self: SnowflakeDialect, name: Optional[str]
) -> Optional[str]:
    """
    This function overrides `SnowflakeDialect.normalize_name` in order to
    cause entity names to be rendered as UPPERCASE rather than lowercase,
    by default.
    """
    if name is None:
        return None
    if name.lower() == name and not (
        getattr(self.identifier_preparer, "_requires_quotes")(name.upper())
    ):
        name = name.upper()
    elif name.upper() == name:
        name = quoted_name(name, quote=True)
    else:
        name = name
    return name


@lru_cache()
def patch_dialect() -> None:
    """
    This function causes Snowflake entity names to be rendered as uppercase
    rather than lowercase
    """
    # Note: This function is cached, intentionally, to prevent reuse.
    SnowflakeDialect.normalize_name = _snowflake_dialect_normalize_name


patch_dialect()

# endregion
