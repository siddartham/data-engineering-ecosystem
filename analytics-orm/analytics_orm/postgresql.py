import functools
import json
from argparse import Namespace
from collections import namedtuple
from functools import wraps
from itertools import chain
from subprocess import CalledProcessError
from typing import (
    Any,
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

import psycopg2.errors  # type: ignore
from more_itertools import unique_everseen
from cerberus_assistant.get import get_secret
from sqlalchemy import Table, text  # type: ignore
from sqlalchemy.dialects.postgresql.base import PGDialect  # type: ignore
from sqlalchemy.dialects.postgresql.base import (  # type: ignore
    PGExecutionContext,
)
from sqlalchemy.engine.base import Connection, Engine  # type: ignore
from sqlalchemy.engine.create import (  # type: ignore  # noqa
    create_engine as _create_engine,
)
from sqlalchemy.engine.interfaces import Dialect  # type: ignore
from sqlalchemy.engine.row import Row  # type: ignore
from sqlalchemy.engine.url import URL  # type: ignore
from sqlalchemy.exc import DBAPIError  # type: ignore
from sqlalchemy.sql.compiler import IdentifierPreparer  # type: ignore

from .cli import parse_arguments as _parse_arguments
from .declarative import Base
from .utilities import lru_cache, run, translate_all_engine_schemas_to

__all__: List[str] = [
    "get_connection_url",
    "DEFAULT_USER",
    "DEFAULT_HOST",
    "DEFAULT_PORT",
    "DEFAULT_DATABASE",
    "parse_arguments",
    "patch_dialect",
    "get_local_docker_user_password_host_port_database",
    "UserPasswordHostPortDatabase",
]


DEFAULT_USER: str = "postgres"
DEFAULT_HOST: str = "localhost"
DEFAULT_PORT: int = 5432
DEFAULT_DATABASE: str = "postgres"
COMMANDS: Tuple[str, ...] = ("create", "drop", "validate")
DEFAULT_ENVIRONMENTS: Tuple[str, ...] = ("dev", "qa", "prod")


def get_connection_url(
    user: str = DEFAULT_USER,
    password: str = "",
    host: str = DEFAULT_HOST,
    port: int = DEFAULT_PORT,
    database: str = DEFAULT_DATABASE,
    user_cerberus_path: str = "",
    password_cerberus_path: str = "",
    host_cerberus_path: str = "",
    port_cerberus_path: str = "",
    database_cerberus_path: str = "",
) -> URL:
    """
    This function assembles a PostgreSQL connection string.

    Parameters:

    - **user** (str) = "postgres"
    - **password** (str) = ""
    - **host** (str) = "localhost"
    - **port** (int) = 5432
    - **database** (str) = "postgres"

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of Orgs [vaults](https://prod.cerberus.orgcloud.com). For
    example: "app/division/postgres-prod/password".

    - **user_cerberus_path** (str) = ""
    - **password_cerberus_path** (str) = ""
    - **host_cerberus_path** (str) = ""
    - **port_cerberus_path** (str) = ""
    - **database_cerberus_path** (str) = ""
    """
    # Retrieve Cerberus secrets
    key: str
    if user_cerberus_path and (user == DEFAULT_USER or (not user)):
        user = get_secret(user_cerberus_path)
    if password_cerberus_path and not password:
        key = password_cerberus_path.rpartition("/")[-1]
        password = get_secret(password_cerberus_path)
        if not user:
            user = key
    if host_cerberus_path and host == DEFAULT_HOST:
        host = get_secret(host_cerberus_path)
    if port_cerberus_path and port == DEFAULT_PORT:
        port = int(get_secret(port_cerberus_path))
    if database_cerberus_path and database == DEFAULT_DATABASE:
        database = get_secret(database_cerberus_path)
    # Construct and return the URL
    return URL.create(
        drivername="postgresql",
        username=user,
        password=password,
        host=host,
        port=port,
        database=database or None,
    )


# For backwards compatibility
get_connection_string: Callable = get_connection_url


def parse_arguments(
    prog: str = "",
    environments: Sequence[str] = DEFAULT_ENVIRONMENTS,
    commands: Sequence[str] = COMMANDS,
    include: Iterable[str] = (
        "checkfirst",
        "command",
        "database",
        "database_cerberus_path",
        "echo",
        "environment",
        "host",
        "host_cerberus_path",
        "ignore_foreign_key",
        "log",
        "only_validate",
        "password",
        "password_cerberus_path",
        "port",
        "port_cerberus_path",
        "undeclared",
        "undeclared_only",
        "user",
        "user_cerberus_path",
        "views_only",
    ),
) -> Namespace:
    """
    Parse postgresql CLI arguments and return the resulting instance of
    `argparse.Namespace`.

    Parameters:

    - prog (str): The CLI command or command + sub-command
      triggering this function. For example:
      "my-datastore-orm postgresql".
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


@lru_cache()
def create_engine(
    user: str = DEFAULT_USER,
    password: str = "",
    host: str = DEFAULT_HOST,
    port: int = DEFAULT_PORT,
    database: str = DEFAULT_DATABASE,
    user_cerberus_path: str = "",
    password_cerberus_path: str = "",
    host_cerberus_path: str = "",
    port_cerberus_path: str = "",
    database_cerberus_path: str = "",
    connect_args: Tuple[Tuple[str, str], ...] = (),
    echo: bool = False,
) -> Engine:
    """
    Create a SQLAlchemy engine for connecting to a PostgreSQL
    database.

    Parameters:

    - **user** (str) = "postgres"
    - **password** (str) = ""
    - **host** (str) = "localhost"
    - **port** (int) = 5432
    - **database** (str) = "postgres"
    - **echo** (bool)

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of Orgs [vaults](https://prod.cerberus.orgcloud.com). For
    example: "app/division/postgres-prod/password".

    - **user_cerberus_path** (str) = ""
    - **password_cerberus_path** (str) = ""
    - **port_cerberus_path** (str) = ""
    - **database_cerberus_path** (str) = ""

    Please note that this connection is cached and re-used in subsequent calls
    referencing the same environment, so maintaining a persistent reference
    within the client application is not necessary.
    """
    return translate_all_engine_schemas_to(
        _create_engine(
            get_connection_url(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database,
                user_cerberus_path=user_cerberus_path,
                password_cerberus_path=password_cerberus_path,
                host_cerberus_path=host_cerberus_path,
                port_cerberus_path=port_cerberus_path,
                database_cerberus_path=database_cerberus_path,
            ),
            echo=echo,
            **(dict(connect_args=dict(connect_args)) if connect_args else {}),
        ),
        None,
    )


def create_all(
    declarative_base: Type[Base],
    user: str = DEFAULT_USER,
    password: str = "",
    host: str = DEFAULT_HOST,
    port: int = DEFAULT_PORT,
    database: str = DEFAULT_DATABASE,
    user_cerberus_path: str = "",
    password_cerberus_path: str = "",
    host_cerberus_path: str = "",
    port_cerberus_path: str = "",
    database_cerberus_path: str = "",
    connect_args: Tuple[Tuple[str, str], ...] = (),
    echo: bool = False,
    checkfirst: bool = True,
    tables: Optional[Iterable[Table]] = None,
    views_only: bool = False,
    bind: Union[Engine, Connection, None] = None,
) -> Engine:
    """
    Create the database, schemas, views and tables.

    Parameters:

    - **declarative_base** (type): A declarative base class created
      using `analytics_orm.declarative.declarative_base()`
      or a class decorated with
      `@analytics_orm.declarative.declarative_base()`.
    - **user** (str) = "postgres"
    - **password** (str) = ""
    - **host** (str) = "localhost"
    - **port** (int) = 5432
    - **database** (str) = "postgres"

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of Org's [vaults](https://prod.cerberus.orgcloud.com). For
    example: "app/division/postgres-prod/password".

    - **user_cerberus_path** (str) = ""
    - **password_cerberus_path** (str) = ""
    - **port_cerberus_path** (str) = ""
    - **database_cerberus_path** (str) = ""
    """
    connection: Connection
    if checkfirst and not bind:
        # First check to see if the database exists, and if not--create it
        connection: Connection = create_engine(
            database=DEFAULT_DATABASE,
            user=user,
            password=password,
            host=host,
            port=port,
            user_cerberus_path=user_cerberus_path,
            password_cerberus_path=password_cerberus_path,
            host_cerberus_path=host_cerberus_path,
            port_cerberus_path=port_cerberus_path,
            connect_args=connect_args,
            echo=echo,
        ).connect()
        # Get the database name that will actually be used
        if database_cerberus_path and database == DEFAULT_DATABASE:
            database = get_secret(database_cerberus_path)

        def get_first_row_value(row: Row) -> str:
            return row[0].lower()

        if database.lower() not in map(
            get_first_row_value,
            connection.execute(text("SELECT datname FROM pg_database")),
        ):
            dialect: Dialect = connection.dialect
            preparer_class: Type[IdentifierPreparer] = getattr(
                dialect, "preparer"
            )
            preparer: IdentifierPreparer = preparer_class(dialect=dialect)
            connection.execute(text("COMMIT"))
            connection.execute(
                text(f"CREATE DATABASE {preparer.quote(database)}")
            )
        connection.close()
    if not bind:
        # Create the engine connecting to our selected database
        bind = create_engine(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port,
            user_cerberus_path=user_cerberus_path,
            password_cerberus_path=password_cerberus_path,
            host_cerberus_path=host_cerberus_path,
            port_cerberus_path=port_cerberus_path,
            database_cerberus_path=database_cerberus_path,
            connect_args=connect_args,
            echo=echo,
        )
    connection = bind if isinstance(bind, Connection) else bind.connect()
    # Attempt to install the "aws_s3" extension
    try:
        connection.execute(
            text("CREATE EXTENSION IF NOT EXISTS aws_s3 CASCADE")
        )
        connection.execute(
            text(
                "GRANT EXECUTE "
                "ON ALL FUNCTIONS IN SCHEMA aws_s3 to "
                f"{bind.engine.url.username}"
            )
        )
    except DBAPIError as error:
        if not isinstance(
            error.orig,
            (
                psycopg2.errors.UndefinedFile,
                psycopg2.errors.FeatureNotSupported,
            ),
        ):
            # `psycopg2.errors.UndefinedFile` is the error that is raised by
            # psycopg2 if no extension control file can be found for the
            # plugin. This error is expected for all PostgreSQL distributions
            # except for AWS RDS/Aurora, and should not be considered
            # fatal
            raise
    if views_only and not tables:
        # Create schemas and views
        declarative_base.metadata.create_views(  # type: ignore
            bind=bind, checkfirst=checkfirst
        )
    else:
        # Create schemas, tables, and views
        declarative_base.metadata.create_all(  # type: ignore
            bind=bind, checkfirst=checkfirst, tables=tables
        )
    return bind


def drop_all(
    declarative_base: Type[Base],
    user: str = "",
    password: str = "",
    host: str = "",
    port: int = DEFAULT_PORT,
    database: str = DEFAULT_DATABASE,
    user_cerberus_path: str = "",
    password_cerberus_path: str = "",
    host_cerberus_path: str = "",
    port_cerberus_path: str = "",
    database_cerberus_path: str = "",
    connect_args: Tuple[Tuple[str, str], ...] = (),
    echo: bool = False,
    checkfirst: bool = True,
    tables: Optional[Iterable[Table]] = None,
    views_only: bool = False,
    bind: Union[Engine, Connection, None] = None,
    undeclared: bool = True,
    undeclared_only: bool = False,
) -> Engine:
    """
    Drop all views and (optionally) tables in the database.

    Parameters:

    - **declarative_base** (type): A declarative base class created
      using `analytics_orm.declarative.declarative_base()`
      or a class decorated with
      `@analytics_orm.declarative.declarative_base()`.
    - **user** (str) = "postgres"
    - **password** (str) = ""
    - **host** (str) = "localhost"
    - **port** (int) = 5432
    - **database** (str) = ""
    - **echo** (bool)
    - **checkfirst** (bool) = True
    - **tables** ([sqlalchemy.Table])
    - **views_only** (bool) = False: If `True`, *only* views will be dropped.

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of Org's [vaults](https://prod.cerberus.orgcloud.com). For
    example: "app/division/postgres-prod/password".

    - **user_cerberus_path** (str) = ""
    - **password_cerberus_path** (str) = ""
    - **port_cerberus_path** (str) = ""
    - **database_cerberus_path** (str) = ""
    """
    if not bind:
        # Create the engine connecting to our selected database
        bind = create_engine(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port,
            user_cerberus_path=user_cerberus_path,
            password_cerberus_path=password_cerberus_path,
            host_cerberus_path=host_cerberus_path,
            port_cerberus_path=port_cerberus_path,
            database_cerberus_path=database_cerberus_path,
            connect_args=connect_args,
            echo=echo,
        )
    if undeclared or undeclared_only:
        declarative_base.metadata.drop_undeclared(bind=bind)  # type: ignore
        if undeclared_only:
            return bind
    if views_only and not tables:
        print("Dropping all views")
        # Drop views
        declarative_base.metadata.drop_views(  # type: ignore
            bind=bind, checkfirst=checkfirst
        )
    else:
        if tables:
            table: str
            print(
                "Dropping tables: "
                f"{', '.join(table.name for table in tables)}"
            )
        else:
            print("Dropping all tables")
        # Drop tables, and views
        declarative_base.metadata.drop_all(  # type: ignore
            bind=bind, checkfirst=checkfirst, tables=tables
        )
    return bind


@lru_cache()
def patch_dialect(
    postgresql_dialect_class: Type[PGDialect] = PGDialect,
) -> None:
    """
    This function patches a PostgreSQL dialect class in order to
    prevent errors from being raised when an empty statement is passed to
    the cursor.

    Note: This function is cached, intentionally, to prevent reuse
    (a dialect only needs patched once).
    """
    assert issubclass(postgresql_dialect_class, PGDialect)
    do_execute_: Callable[
        [PGDialect, Any, str, Dict[str, Any], Optional[PGExecutionContext]],
        None,
    ] = postgresql_dialect_class.do_execute
    do_execute_no_params_: Callable[
        [PGDialect, Any, str, Optional[PGExecutionContext]],
        None,
    ] = postgresql_dialect_class.do_execute_no_params

    @wraps(postgresql_dialect_class.do_execute)
    def do_execute(
        self: PGDialect,
        cursor: Any,
        statement: str,
        parameters: Dict[str, Any],
        context: Optional[PGExecutionContext] = None,
    ) -> None:
        if statement:
            do_execute_(self, cursor, statement, parameters, context)

    postgresql_dialect_class.do_execute = do_execute

    @wraps(postgresql_dialect_class.do_execute_no_params)
    def do_execute_no_params(
        self: PGDialect,
        cursor: Any,
        statement: str,
        context: Optional[PGExecutionContext] = None,
    ) -> None:
        if statement:
            do_execute_no_params_(self, cursor, statement, context)

    postgresql_dialect_class.do_execute_no_params = do_execute_no_params


UserPasswordHostPortDatabase: Type[tuple] = namedtuple(
    "UserPasswordHostPortDatabase",
    ("user", "password", "host", "port", "database"),
)


def _get_host_port(port_binding: Dict[str, Optional[str]]) -> Optional[str]:
    return port_binding.get("HostPort", None)


def _iter_docker_inspect_item_user_password_host_port_database(
    item: Dict[str, Any]
) -> Iterable[UserPasswordHostPortDatabase]:
    database: str = "postgres"
    user: str = ""
    password: str = ""
    port: int = 5432
    name: str
    value: str
    env_item: str
    for name, value in map(
        lambda env_item: env_item.split("=")[:2],
        item.get("Config", {}).get("Env", ()),
    ):
        name = name.upper().strip()
        if name == "POSTGRES_DB":
            database = value.partition(",")[0].strip()
        elif name == "POSTGRES_USER":
            user = value.strip()
        elif name == "POSTGRES_PASSWORD":
            password = value.strip()
    try:
        port = int(
            next(
                iter(
                    filter(
                        None,
                        map(
                            _get_host_port,
                            chain(
                                *filter(
                                    None,
                                    item.get("HostConfig", {})
                                    .get("PortBindings", {})
                                    .values(),
                                ),
                            ),
                        ),
                    )
                )
            )
        )
    except StopIteration:
        pass
    if "NetworkSettings" in item:
        network_settings: Dict[str, Any] = item["NetworkSettings"]
        host_port: Dict[str, str]
        for host_port in chain(
            *filter(None, network_settings["Ports"].values())
        ):
            yield UserPasswordHostPortDatabase(
                user,
                password,
                (
                    "localhost"
                    if host_port["HostIp"] == "::"  # type: ignore
                    else host_port["HostIp"]  # type: ignore
                ),
                port,
                database,
            )
        yield UserPasswordHostPortDatabase(
            user, password, network_settings["IPAddress"], port, database
        )
        network: Dict[str, str]
        for network in network_settings["Networks"].values():
            yield UserPasswordHostPortDatabase(
                user, password, network["IPAddress"], port, database
            )


def _iter_user_password_host_port_database(
    container_name: str = "postgres",
) -> Iterable[UserPasswordHostPortDatabase]:
    item: Dict[str, Any]
    for item in json.loads(run(("docker", "inspect", container_name))):
        yield from _iter_docker_inspect_item_user_password_host_port_database(
            item
        )


_get_local_docker_host_lru_cache: Callable[
    [Optional[int], bool],
    Callable[
        [Callable[..., UserPasswordHostPortDatabase]],
        Callable[..., UserPasswordHostPortDatabase],
    ],
] = functools.lru_cache  # type: ignore


@_get_local_docker_host_lru_cache(None, False)
def get_local_docker_user_password_host_port_database(
    container_name: str = "postgres",
) -> UserPasswordHostPortDatabase:
    """
    This function inspects a local postgres docker image named `container_name`
    and returns the user, password, host, port, and database name. This
    is intended for use with unit testing.

    Parameter:

    - container_name (str)
    """
    error: Optional[CalledProcessError] = None
    user: str = ""
    password: str = ""
    host: str = ""
    port: int = 5432
    database: str = "postgres"
    for user, password, host, port, database in unique_everseen(
        _iter_user_password_host_port_database(container_name)
    ):
        try:
            run(
                "psql postgres://"
                f"{user}:{password}@{host}:{port}/{database} -c '\\l'"
            )
            error = None
            break
        except CalledProcessError as error_:
            error = error_
    if error is not None:
        run(("psql", "-V"))
        raise error
    print(f"Host: {host}")
    return UserPasswordHostPortDatabase(user, password, host, port, database)


# region Dialect Patch

_original_postgresql_dialect_do_execute: Callable[
    [PGDialect, Any, str, Dict[str, Any], Optional[PGExecutionContext]],
    None,
] = PGDialect.do_execute
_original_postgresql_dialect_do_execute_no_params: Callable[
    [PGDialect, Any, str, Optional[PGExecutionContext]],
    None,
] = PGDialect.do_execute_no_params


@wraps(PGDialect.do_execute)
def _postgresql_dialect_do_execute(
    self: PGDialect,
    cursor: Any,
    statement: str,
    parameters: Dict[str, Any],
    context: Optional[PGExecutionContext] = None,
) -> None:
    if statement:
        _original_postgresql_dialect_do_execute(
            self, cursor, statement, parameters, context
        )


@wraps(PGDialect.do_execute_no_params)
def _postgresql_dialect_do_execute_no_params(
    self: PGDialect,
    cursor: Any,
    statement: str,
    context: Optional[PGExecutionContext] = None,
) -> None:
    if statement:
        _original_postgresql_dialect_do_execute_no_params(
            self, cursor, statement, context
        )


@lru_cache()
def patch_dialect() -> None:
    """
    This function patches the dialect class in order to
    prevent errors from being raised when an empty statement is passed to
    the cursor.

    Note: This function is cached, intentionally, to prevent reuse
    (a dialect only needs patched once).
    """
    PGDialect.do_execute_no_params = _postgresql_dialect_do_execute_no_params
    PGDialect.do_execute = _postgresql_dialect_do_execute


patch_dialect()

# endregion
