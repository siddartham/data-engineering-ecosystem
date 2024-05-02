import argparse
from typing import (
    Any,
    Callable,
    Dict,
    FrozenSet,
    Iterable,
    Sequence,
    Tuple,
    Union,
)

import psycopg2.errors  # type: ignore
from analytics_orm.postgresql import (
    DEFAULT_DATABASE,
    DEFAULT_HOST,
    DEFAULT_PORT,
    DEFAULT_USER,
    create_all,
    create_engine,
    drop_all,
    get_connection_string,
    parse_arguments,
)
from analytics_orm.utilities import apply_environment_defaults
from analytics_orm.validation import validate
from sqlalchemy import text  # type: ignore
from sqlalchemy.engine import URL, Connection, Engine  # type: ignore
from sqlalchemy.exc import DBAPIError  # type: ignore
from sqlalchemy.schema import ForeignKeyConstraint  # type: ignore

from ..base import Base

ENVIRONMENTS: FrozenSet[str] = frozenset(("dev", "qa", "prod"))
CERBERUS_PATH_DEV: str = "app/sustainability/postgres-psdata-dev"
CERBERUS_PATH_QA: str = "app/sustainability/postgres-psdata-qa"
CERBERUS_PATH_PROD: str = "app/sustainability/postgres-psdata-prod"

_ROLES: Tuple[str, ...] = ("reader",)
_GRANTS: Tuple[str, ...] = (
    "GRANT SELECT ON ALL TABLES IN SCHEMA public TO reader",
)
_DEV_DEFAULTS: Dict[str, Any] = dict(
    user_cerberus_path=f"{CERBERUS_PATH_DEV}/user",
    password_cerberus_path=f"{CERBERUS_PATH_DEV}/password",
    host_cerberus_path=f"{CERBERUS_PATH_DEV}/host",
    port_cerberus_path=f"{CERBERUS_PATH_DEV}/port",
    database_cerberus_path=f"{CERBERUS_PATH_DEV}/database",
    checkfirst=True,
)
_QA_DEFAULTS: Dict[str, Any] = dict(
    user_cerberus_path=f"{CERBERUS_PATH_QA}/user",
    password_cerberus_path=f"{CERBERUS_PATH_QA}/password",
    host_cerberus_path=f"{CERBERUS_PATH_QA}/host",
    port_cerberus_path=f"{CERBERUS_PATH_QA}/port",
    database_cerberus_path=f"{CERBERUS_PATH_QA}/database",
    checkfirst=True,
)
_PROD_DEFAULTS: Dict[str, Any] = dict(
    user_cerberus_path=f"{CERBERUS_PATH_PROD}/user",
    password_cerberus_path=f"{CERBERUS_PATH_PROD}/password",
    host_cerberus_path=f"{CERBERUS_PATH_PROD}/host",
    port_cerberus_path=f"{CERBERUS_PATH_PROD}/port",
    database_cerberus_path=f"{CERBERUS_PATH_PROD}/database",
    checkfirst=True,
)


@apply_environment_defaults("dev", **_DEV_DEFAULTS)
@apply_environment_defaults("qa", **_QA_DEFAULTS)
@apply_environment_defaults("prod", **_PROD_DEFAULTS)
def get_environment_connection_string(
    environment: str = "",
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
    This function assembles a connection string, inferring default values
    based on the specified `environment`.

    Required Parameters:

    - environment (str): "dev", "qa" or "prod"

    Optional Parameters:

    - user (str) = "postgres"
    - password (str) = ""
    - host (str) = "localhost"
    - port (int) = 5432
    - database (str) = "postgres"

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of My [vaults](https://prod.cerberus.mycloud.com). For
    example: "app/sustainability/postgres-prod/password". For these parameters,
    defaults will vary by `environment`.

    - user_cerberus_path (str) = ""
    - password_cerberus_path (str) = ""
    - port_cerberus_path (str) = ""
    - database_cerberus_path (str) = ""
    """
    if environment:
        assert environment in ENVIRONMENTS
    return get_connection_string(
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
    )


@apply_environment_defaults("dev", **_DEV_DEFAULTS)
@apply_environment_defaults("qa", **_QA_DEFAULTS)
@apply_environment_defaults("prod", **_PROD_DEFAULTS)
def create_environment_engine(
    environment: str = "",
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
    This function creates a SQLAlchemy database connection engine, inferring
    default values based on the specified `environment`.

    Required Parameters:

    - environment (str): "dev", "qa" or "prod"

    Optional Parameters:

    - user (str) = "postgres"
    - password (str) = ""
    - host (str) = "localhost"
    - port (int) = 5432
    - database (str) = "postgres"

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of My [vaults](https://prod.cerberus.mycloud.com). For
    example: "app/sustainability/postgres-prod/password". For these parameters,
    defaults will vary by `environment`.

    - user_cerberus_path (str)
    - password_cerberus_path (str)
    - port_cerberus_path (str)
    - database_cerberus_path (str)
    """
    if environment:
        assert environment in ENVIRONMENTS
    return create_engine(
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
        connect_args=connect_args,
        echo=echo,
    )


@apply_environment_defaults("dev", **_DEV_DEFAULTS)
@apply_environment_defaults("qa", **_QA_DEFAULTS)
@apply_environment_defaults("prod", **_PROD_DEFAULTS)
def grant_environment_permissions(
    environment: str = "",
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
    bind: Union[Engine, Connection, None] = None,
) -> Engine:
    """
    This function applies permissions for an environment's database.

    Required Parameters:

    - environment (str): "dev", "qa" or "prod"

    Optional Parameters:

    - user (str) = "postgres"
    - password (str) = ""
    - host (str) = "localhost"
    - port (int) = 5432
    - database (str) = "postgres"

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of My [vaults](https://prod.cerberus.mycloud.com). For
    example: "app/sustainability/postgres-prod/password". For these parameters,
    defaults will vary by `environment`.

    - user_cerberus_path (str)
    - password_cerberus_path (str)
    - port_cerberus_path (str)
    - database_cerberus_path (str)
    """
    if environment and not bind:
        assert environment in ENVIRONMENTS
    if bind is None:
        bind = create_engine(
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
            connect_args=connect_args,
            echo=echo,
        )
    connection = bind if isinstance(bind, Connection) else bind.connect()
    role: str
    for role in _ROLES:
        try:
            connection.execute(text("COMMIT"))
            connection.execute(text(f"CREATE ROLE {role}"))
        except DBAPIError as error:
            if not isinstance(
                error.orig,
                (
                    psycopg2.errors.UndefinedObject,
                    psycopg2.errors.DuplicateObject,
                ),
            ):
                raise
    statement: str
    try:
        for statement in _GRANTS:
            connection.execute(text(statement), ())
    except Exception as error:  # noqa
        raise
    return bind.engine if isinstance(bind, Connection) else bind


@apply_environment_defaults("dev", **_DEV_DEFAULTS)
@apply_environment_defaults("qa", **_QA_DEFAULTS)
@apply_environment_defaults("prod", **_PROD_DEFAULTS)
def create_environment(
    environment: str = "",
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
    checkfirst: bool = False,
    echo: bool = False,
    views_only: bool = False,
    bind: Union[Engine, Connection, None] = None,
) -> Engine:
    """
    This function creates the database, schemas, and tables.

    Required Parameters:

    - environment (str): "dev", "qa" or "prod"

    Optional Parameters:

    - user (str) = "postgres"
    - password (str) = ""
    - host (str) = "localhost"
    - port (int) = 5432
    - database (str) = "postgres"
    - echo (bool) = False: If `True`, all compiled statements will be
      printed to `sys.stdout` prior to execution.
    - views_only (bool) = False

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of My [vaults](https://prod.cerberus.mycloud.com). For
    example: "app/sustainability/postgres-prod/password". For these parameters,
    defaults will vary by `environment`.

    - user_cerberus_path (str)
    - password_cerberus_path (str)
    - port_cerberus_path (str)
    - database_cerberus_path (str)
    """
    if environment:
        assert environment in ENVIRONMENTS
    return grant_environment_permissions(
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
        echo=echo,
        bind=create_all(
            declarative_base=Base,
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
            checkfirst=checkfirst,
            echo=echo,
            views_only=views_only,
            bind=bind,
            connect_args=connect_args,
        ),
        connect_args=connect_args,
    )


@apply_environment_defaults("dev", **_DEV_DEFAULTS)
@apply_environment_defaults("qa", **_QA_DEFAULTS)
@apply_environment_defaults("prod", **_PROD_DEFAULTS)
def drop_environment(
    environment: str = "",
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
    checkfirst: bool = False,
    echo: bool = False,
    views_only: bool = False,
    undeclared: bool = False,
    undeclared_only: bool = False,
    bind: Union[Engine, Connection, None] = None,
    connect_args: Tuple[Tuple[str, str], ...] = (),
) -> Engine:
    """
    This function drops all tables/views in the database.

    Parameters:

    - environment (str): "dev", "qa" or "prod"
    - user (str) = "postgres"
    - password (str) = ""
    - host (str) = "localhost"
    - port (int) = 5432
    - database (str) = "postgres"
    - echo (bool) = False: If `True`, all compiled statements will be
      printed to `sys.stdout` prior to execution.
    - views_only (bool) = False

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of Nike's [vaults](https://prod.cerberus.mycloud.com). For
    example: "app/sustainability/postgres-prod/password". For these parameters,
    defaults will vary by `environment`.

    - user_cerberus_path (str)
    - password_cerberus_path (str)
    - port_cerberus_path (str)
    - database_cerberus_path (str)
    """
    if environment:
        assert environment in ENVIRONMENTS
    return drop_all(
        declarative_base=Base,
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
        checkfirst=checkfirst,
        echo=echo,
        views_only=views_only,
        bind=bind,
        connect_args=connect_args,
        undeclared=undeclared,
        undeclared_only=undeclared_only,
    )


@apply_environment_defaults("dev", **_DEV_DEFAULTS)
@apply_environment_defaults("qa", **_QA_DEFAULTS)
@apply_environment_defaults("prod", **_PROD_DEFAULTS)
def validate_environment(
    environment: str = "",
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
    only: Sequence[str] = (),
    ignore_foreign_keys: Union[
        Iterable[str], Callable[[ForeignKeyConstraint], bool], None
    ] = None,
) -> Engine:
    """
    This function validates all tables/views in the database.

    Parameters:

    - environment (str): "dev", "qa" or "prod"
    - user (str) = "postgres"
    - password (str) = ""
    - host (str) = "localhost"
    - port (int) = 5432
    - database (str) = "postgres"
    - echo (bool) = False: If `True`, all compiled statements will be
      printed to `sys.stdout` prior to execution.
    - views_only (bool) = False

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of Nike's [vaults](https://prod.cerberus.mycloud.com). For
    example: "app/sustainability/postgres-prod/password". For these parameters,
    defaults will vary by `environment`.

    - user_cerberus_path (str)
    - password_cerberus_path (str)
    - port_cerberus_path (str)
    - database_cerberus_path (str)
    """
    bind = create_environment_engine(
        environment=environment,
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
        echo=echo,
        connect_args=connect_args,
    )
    validate(Base, bind, only=only, ignore_foreign_keys=ignore_foreign_keys)
    return bind


def main() -> None:
    """
    This function is the entry point for the
    `my-api-model postgresql` command.
    """
    arguments: argparse.Namespace = parse_arguments(
        "my-api-model postgresql"
    )
    if arguments.command == "create":
        create_environment(
            arguments.environment,
            user=arguments.user,
            password=arguments.password,
            host=arguments.host,
            port=arguments.port,
            database=arguments.database,
            user_cerberus_path=arguments.user_cerberus_path,
            password_cerberus_path=arguments.password_cerberus_path,
            host_cerberus_path=arguments.host_cerberus_path,
            port_cerberus_path=arguments.port_cerberus_path,
            database_cerberus_path=arguments.database_cerberus_path,
            views_only=arguments.views_only,
            echo=arguments.echo,
            checkfirst=arguments.checkfirst,
        )
    elif arguments.command == "drop":
        drop_environment(
            arguments.environment,
            user=arguments.user,
            password=arguments.password,
            host=arguments.host,
            port=arguments.port,
            database=arguments.database,
            user_cerberus_path=arguments.user_cerberus_path,
            password_cerberus_path=arguments.password_cerberus_path,
            host_cerberus_path=arguments.host_cerberus_path,
            port_cerberus_path=arguments.port_cerberus_path,
            database_cerberus_path=arguments.database_cerberus_path,
            checkfirst=arguments.checkfirst,
            echo=arguments.echo,
            views_only=arguments.views_only,
            undeclared=arguments.undeclared,
            undeclared_only=arguments.undeclared_only,
        )
    elif arguments.command == "validate":
        validate_environment(
            environment=arguments.environment,
            user=arguments.user,
            password=arguments.password,
            database=arguments.database,
            echo=arguments.echo,
            user_cerberus_path=arguments.user_cerberus_path,
            password_cerberus_path=arguments.password_cerberus_path,
            database_cerberus_path=arguments.database_cerberus_path,
            only=arguments.only_validate,
            ignore_foreign_keys=arguments.ignore_foreign_key,
        )
