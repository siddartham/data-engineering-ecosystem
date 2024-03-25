import json
import logging
import re
from argparse import Namespace
from subprocess import CalledProcessError
from typing import (
    Any,
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
from sqlalchemy import Table  # type: ignore
from sqlalchemy.engine.base import Connection, Engine  # type: ignore
from sqlalchemy.engine.create import (
    create_engine as _create_engine,  # type: ignore
)
from sqlalchemy.engine.interfaces import Dialect  # type: ignore
from sqlalchemy.engine.row import Row  # type: ignore
from sqlalchemy.engine.url import URL  # type: ignore
from sqlalchemy.sql.compiler import IdentifierPreparer  # type: ignore

from .cli import parse_arguments as _parse_arguments
from .utilities import lru_cache, run, translate_all_engine_schemas_to

__all__: List[str] = [
    "get_connection_string",
    "create_engine",
    "create_all",
    "drop_all",
    "parse_arguments",
]
DEFAULT_DATABASE: str = "default"
DEFAULT_PORT: int = 10000
DEFAULT_STORED_AS: str = "PARQUET"
DEFAULT_TBLPROPERTIES: Tuple[Tuple[str, str], ...] = (
    ("has_encrypted_data", "false"),
    ("classification", "parquet"),
)
COMMANDS: Tuple[str, ...] = ("create", "drop", "validate")
DEFAULT_ENVIRONMENTS: Tuple[str, ...] = ("dev", "qa", "prod")


def _get_spark_session() -> Any:
    """
    If pyspark is installed, initialize and return a Spark Session,
    otherwise return `None`.
    """
    try:
        from pyspark.sql import SparkSession  # type: ignore

        return SparkSession.builder.enableHiveSupport().getOrCreate()
    except Exception:  # noqa
        # We must allow for overly broad exceptions here because
        # that is what pyspark raises when it fails to launch a java
        # gateway
        return None


def _get_emr_master_private_dns_name() -> str:
    command: str = (
        "jq .masterPrivateDnsName "
        "/emr/instance-controller/lib/info/job-flow.json"
    )
    logging.info(command)
    return json.loads(run(command))


def _get_yarn_resource_manager_ip() -> str:
    command: str = "yarn node -list"
    logging.info(command)
    output: str = run(command)
    return next(re.finditer(r"\d+\.\d+\.\d+\.\d+", output)).group()


@lru_cache()
def _get_host() -> str:
    host: str = "127.0.0.1"
    try:
        host = _get_emr_master_private_dns_name()
    except CalledProcessError:
        try:
            host = _get_yarn_resource_manager_ip()
        except (CalledProcessError, StopIteration):
            pass
    return host


def _get_connection_string_query(
    password: str = "",
) -> Dict[str, Union[str, Sequence[str]]]:
    query: Dict[str, Union[str, Sequence[str]]] = {}
    if password:
        query["auth"] = "LDAP"
    return query


def get_connection_string(
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
) -> URL:
    """
    This function assembles and returns a hive connection string.

    Parameters:

    - **user** (str) = "": A username with which to connect to the hive
      server, if applicable.
    - **password** (str) = "": A password with which to connect to the hive
      server, if applicable.
    - **host** (str) = "": The IP or hostname of a server running
      `hiveserver2`, or "" (the default) if running hive locally.
    - **port** (int) = 5432: The port number on which `hiveserver2` is
      exposed.
    - **database** (str) = "default": The database name.

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of Org's [vaults](https://prod.cerberus.orgcloud.com). For
    example: "app/division/postgres-prod/password".

    - **user_cerberus_path** (str) = ""
    - **password_cerberus_path** (str) = ""
    - **host_cerberus_path** (str) = ""
    - **port_cerberus_path** (str) = ""
    - **database_cerberus_path** (str) = ""
    """
    # Retrieve Cerberus secrets
    key: str
    if user_cerberus_path and not user:
        user = get_secret(user_cerberus_path)
    if password_cerberus_path and not password:
        key = password_cerberus_path.rpartition("/")[-1]
        password = get_secret(password_cerberus_path)
        if not user:
            user = key
    if host_cerberus_path and not host:
        host = get_secret(host_cerberus_path)[1]
    if port_cerberus_path and ((not port) or port == DEFAULT_PORT):
        port = int(get_secret(port_cerberus_path))
    if database_cerberus_path and (
        (not database) or database == DEFAULT_DATABASE
    ):
        database = get_secret(database_cerberus_path)[1]
    if not host:
        host = _get_host()
    if ":" in host:
        host_port: str
        host, host_port = host.split(":")
        if (not port) or port == DEFAULT_PORT:
            port = int(host_port)
    return URL.create(
        drivername="hive",
        username=user or None,
        password=password or None,
        host=host,
        port=port or None,
        database=database or None,
        query=_get_connection_string_query(password=password),
    )


@lru_cache()
def create_engine(
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
    echo: bool = False,
) -> Engine:
    """
    This function assembles and returns a SQLAlchemy connection engine.

    Parameters:

    - **user** (str) = "": A username with which to connect to the hive
      server, if applicable.
    - **password** (str) = "": A password with which to connect to the hive
      server, if applicable.
    - **host** (str) = "": The IP or hostname of a server running
      `hiveserver2`, or "" (the default) if running hive locally.
    - **port** (int) = 5432: The port number on which `hiveserver2` is
      exposed.
    - **database** (str) = "default": The database name.

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of Org's [vaults](https://prod.cerberus.orgcloud.com). For
    example: "app/division/postgres-prod/password".

    - **user_cerberus_path** (str) = ""
    - **password_cerberus_path** (str) = ""
    - **host_cerberus_path** (str) = ""
    - **port_cerberus_path** (str) = ""
    - **database_cerberus_path** (str) = ""
    """
    return translate_all_engine_schemas_to(
        _create_engine(
            get_connection_string(
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
        ),
        None,
    )


def create_all(
    declarative_base: type,
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
    echo: bool = False,
    checkfirst: bool = True,
    tables: Optional[Iterable[Table]] = None,
    views_only: bool = False,
    location: str = "",
    stored_as: str = DEFAULT_STORED_AS,
    tblproperties: Union[
        Dict[str, str], Sequence[Tuple[str, str]]
    ] = DEFAULT_TBLPROPERTIES,
    bind: Union[Connection, Engine, None] = None,
) -> Engine:
    """
    Create the database, schemas, views and tables.

    Parameters:

    - **declarative_base** (type): A declarative base class created
      using `org.orm_framework.declarative.declarative_base()`
      or a class decorated with
      `@org.orm_framework.declarative.declarative_base()`.
    - **user** (str) = "postgres"
    - **password** (str) = ""
    - **host** (str) = "localhost"
    - **port** (int) = 5432
    - **database** (str) = ""
    - **echo** (bool)
    - **checkfirst** (bool) = True
    - **tables** ([sqlalchemy.Table])
    - **views_only** (bool): If `True`, *only* views will be created.
    - **location** (str) = "": An S3 URL to a bucket + object-prefix
      serving as the root "directory" to which each table's relative path
      will be appended
    - **stored_as** (str) = "PARQUET"
    - **tblproperties** ({str: str}) = {
        "has_encrypted_data": "false",
        "classification": "parquet"
      }

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of Org's [vaults](https://prod.cerberus.orgcloud.com). For
    example: "app/division/postgres-prod/password".

    - **user_cerberus_path** (str) = ""
    - **password_cerberus_path** (str) = ""
    - **port_cerberus_path** (str) = ""
    - **database_cerberus_path** (str) = ""
    """
    # If this is being performed on a Spark Cluster, we need
    # to initialize Spark in order to avoid errors (even though we
    # won't use it)
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
            echo=echo,
        ).connect()
        # Get the database name that will actually be used
        if database_cerberus_path and database == DEFAULT_DATABASE:
            database = get_secret(database_cerberus_path)

        def get_first_row_value(row: Row) -> str:
            return row[0].lower()

        if database.lower() not in map(
            get_first_row_value,
            connection.execute("SHOW DATABASES"),
        ):
            dialect: Dialect = connection.dialect
            preparer_class: Type[IdentifierPreparer] = getattr(
                dialect, "preparer"
            )
            preparer: IdentifierPreparer = preparer_class(dialect=dialect)
            connection.execute("COMMIT")
            connection.execute(f"CREATE DATABASE {preparer.quote(database)}")
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
            echo=echo,
        )
    if views_only:
        # Create schemas and views
        declarative_base.metadata.create_views(  # type: ignore
            bind=bind,
            checkfirst=checkfirst,
            tables=tables,
        )
    else:
        # Create schemas, tables, and views
        declarative_base.metadata.create_all(  # type: ignore
            bind=bind,
            checkfirst=checkfirst,
            tables=tables,
            hive_location=location,
            hive_stored_as=stored_as,
            hive_tblproperties=tblproperties,
        )
    return bind


def drop_all(
    declarative_base: type,
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
    echo: bool = False,
    checkfirst: bool = True,
    tables: Optional[Iterable[Table]] = None,
    views_only: bool = False,
    bind: Union[Connection, Engine, None] = None,
    undeclared: bool = False,
    undeclared_only: bool = False,
) -> Engine:
    """
    Drop all views and (optionally) tables in the database.

    Parameters:

    - **declarative_base** (type): A declarative base class created
      using `org.orm_framework.declarative.declarative_base()`
      or a class decorated with
      `@org.orm_framework.declarative.declarative_base()`.
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
    # If this is being performed on a Spark Cluster, we need
    # to initialize Spark in order to avoid errors (even though we
    # won't use it)
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
            echo=echo,
        )
    if undeclared or undeclared_only:
        declarative_base.metadata.drop_undeclared(bind=bind)  # type: ignore
        if undeclared_only:
            return bind
    if views_only:
        # Drop views
        declarative_base.metadata.drop_views(  # type: ignore
            bind=bind, checkfirst=checkfirst
        )
    else:
        # Drop tables, and views
        declarative_base.metadata.drop_all(  # type: ignore
            bind=bind, checkfirst=checkfirst, tables=tables
        )
    return bind


def parse_arguments(
    prog: str = "",
    environments: Sequence[str] = DEFAULT_ENVIRONMENTS,
    commands: Sequence[str] = COMMANDS,
    include: Iterable[str] = (
        "command",
        "environment",
        "checkfirst",
        "database_cerberus_path",
        "database",
        "echo",
        "help",
        "host_cerberus_path",
        "host",
        "ignore_foreign_key",
        "location",
        "log",
        "only_validate",
        "password_cerberus_path",
        "password",
        "port_cerberus_path",
        "port",
        "stored_as",
        "tblproperties",
        "undeclared_only",
        "undeclared",
        "user_cerberus_path",
        "user",
        "views_only",
    ),
) -> Namespace:
    """
    Parse hive CLI arguments and return the resulting instance of
    `argparse.Namespace`.

    Parameters:

    - prog (str): The CLI command or command + sub-command
      triggering this function. For example:
      "org-division-model hive".
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
    # If this is being performed on a Spark Cluster, we need
    # to initialize Spark in order to avoid errors (even though we
    # won't use it), and putting this here ensures this will occur at the
    # very start of a program
    _get_spark_session()
    return _parse_arguments(
        prog=prog,
        environments=environments,
        commands=commands,
        include=include,
    )
