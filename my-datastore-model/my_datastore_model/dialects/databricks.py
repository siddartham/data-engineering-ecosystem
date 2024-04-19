import argparse
from typing import Any, Callable, Dict, Iterable, List, Sequence, Tuple, Union

from analytics_orm.databricks import (
    COMMANDS,
    DEFAULT_CATALOG,
    DEFAULT_HOSTNAME,
)
from analytics_orm.databricks import ENVIRONMENTS as _ENVIRONMENTS
from analytics_orm.databricks import (
    create_all,
    create_engine,
    drop_all,
    get_connection_url,
    parse_arguments,
)
from analytics_orm.utilities import apply_environment_defaults
from analytics_orm.validation import validate
from sqlalchemy import ForeignKeyConstraint, Table  # type: ignore
from sqlalchemy.engine.base import Connection, Engine  # type: ignore
from sqlalchemy.engine.url import URL  # type: ignore

from ..base import Base

__all__: List[str] = [
    "get_environment_connection_url",
    "create_environment_engine",
    "create_environment",
    "drop_environment",
    "ENVIRONMENTS",
]

ENVIRONMENTS: Tuple[str, ...] = _ENVIRONMENTS + ("test",)
ACCESS_TOKEN_CERBERUS_PATH_DEV: str = (
    "app/org/sdb/ServicePrincipal."
    "cloud.databricks.com_App.community.my_org.Developer"
)

ACCESS_TOKEN_CERBERUS_PATH_PROD: str = (
    "app/org/sdb/ServicePrincipal."
    "cloud.databricks.com_App.community.my_org.DataAdmin"
)

DEFAULTS: Dict[str, Any] = dict(
    http_path="/sql/1.0/warehouses/12324255235"
)
TEST_DEFAULTS: Dict[str, Any] = dict(
    hostname=DEFAULT_HOSTNAME,
    catalog="development",
    schema="sustainability_test",
    access_token_cerberus_path=ACCESS_TOKEN_CERBERUS_PATH_DEV,
    **DEFAULTS,
)
DEV_DEFAULTS: Dict[str, Any] = dict(
    hostname=DEFAULT_HOSTNAME,
    catalog="development",
    schema="sustainability_dev",
    access_token_cerberus_path=ACCESS_TOKEN_CERBERUS_PATH_DEV,
    **DEFAULTS,
)
QA_DEFAULTS: Dict[str, Any] = dict(
    hostname=DEFAULT_HOSTNAME,
    catalog="development",
    schema="sustainability_qa",
    access_token_cerberus_path=ACCESS_TOKEN_CERBERUS_PATH_DEV,
    **DEFAULTS,
)
PROD_DEFAULTS: Dict[str, Any] = dict(
    hostname=DEFAULT_HOSTNAME,
    catalog="non_published_domain",
    schema="sustainability_prod",
    access_token_cerberus_path=ACCESS_TOKEN_CERBERUS_PATH_PROD,
    **DEFAULTS,
)
PUBLISHED_DEFAULTS: Dict[str, Any] = dict(
    PROD_DEFAULTS,
    **{"catalog": "published_domain"},
)


@apply_environment_defaults("test", **TEST_DEFAULTS)
@apply_environment_defaults("dev", **DEV_DEFAULTS)
@apply_environment_defaults("qa", **QA_DEFAULTS)
@apply_environment_defaults("prod", **PROD_DEFAULTS)
@apply_environment_defaults("published", **PUBLISHED_DEFAULTS)
def get_environment_connection_url(
    environment: str = "",
    http_path: str = "",
    hostname: str = DEFAULT_HOSTNAME,
    access_token: str = "",
    catalog: str = DEFAULT_CATALOG,
    schema: str = "",
    access_token_cerberus_path: str = "",
) -> URL:
    """
    This function assembles and returns a databricks bind string,
    with defaults determined by the environment which is provided.
    Parameters:

    - *environment* (str) = ""
    - http_path (str) = "A cluster's HTTP path"
    - hostname (str)  = "The Databricks hostname"
    - access_token (str) = "A token with which to authenticate"
    - catalog (str) = "The catalog name"
    - schema (str) = "The schema name"

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of My Valuts [vaults](https://prod.cerberus.mycloud.com). For
    example: "app/sustainability/..."

    - access_token_cerberus_path (str)
    """
    if environment:
        assert environment in ENVIRONMENTS
    return get_connection_url(
        http_path=http_path,
        hostname=hostname,
        access_token=access_token,
        catalog=catalog,
        schema=schema,
        access_token_cerberus_path=access_token_cerberus_path,
    )


@apply_environment_defaults("test", **TEST_DEFAULTS)
@apply_environment_defaults("dev", **DEV_DEFAULTS)
@apply_environment_defaults("qa", **QA_DEFAULTS)
@apply_environment_defaults("prod", **PROD_DEFAULTS)
@apply_environment_defaults("published", **PUBLISHED_DEFAULTS)
def create_environment_engine(
    environment: str = "",
    http_path: str = "",
    hostname: str = DEFAULT_HOSTNAME,
    access_token: str = "",
    catalog: str = DEFAULT_CATALOG,
    schema: str = "",
    access_token_cerberus_path: str = "",
    echo: bool = False,
) -> Engine:
    if environment:
        assert environment in ENVIRONMENTS
    return create_engine(
        http_path=http_path,
        hostname=hostname,
        access_token=access_token,
        catalog=catalog,
        schema=schema,
        access_token_cerberus_path=access_token_cerberus_path,
        echo=echo,
    )


@apply_environment_defaults("test", **TEST_DEFAULTS)
@apply_environment_defaults("dev", **DEV_DEFAULTS)
@apply_environment_defaults("qa", **QA_DEFAULTS)
@apply_environment_defaults("prod", **PROD_DEFAULTS)
@apply_environment_defaults("published", **PUBLISHED_DEFAULTS)
def create_environment(
    environment: str = "",
    http_path: str = "",
    hostname: str = DEFAULT_HOSTNAME,
    access_token: str = "",
    catalog: str = DEFAULT_CATALOG,
    schema: str = "",
    access_token_cerberus_path: str = "",
    checkfirst: bool = False,
    bind: Union[Engine, Connection, None] = None,
    views_only: bool = False,
    echo: bool = False,
) -> Any:
    if environment:
        assert environment in ENVIRONMENTS
        if environment == "published":
            # TODO: Implement published environment proxy view creation
            raise NotImplementedError(
                "The published environment is not yet supported."
            )
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
    bind = create_all(
        Base,
        http_path=http_path,
        hostname=hostname,
        access_token=access_token,
        catalog=catalog,
        checkfirst=checkfirst,
        schema=schema,
        access_token_cerberus_path=access_token_cerberus_path,
        echo=echo,
        views_only=views_only,
    )
    return bind


@apply_environment_defaults("test", **TEST_DEFAULTS)
@apply_environment_defaults("dev", **DEV_DEFAULTS)
@apply_environment_defaults("qa", **QA_DEFAULTS)
@apply_environment_defaults("prod", **PROD_DEFAULTS)
@apply_environment_defaults("published", **PUBLISHED_DEFAULTS)
def drop_environment(
    environment: str,
    http_path: str = "",
    hostname: str = DEFAULT_HOSTNAME,
    access_token: str = "",
    catalog: str = DEFAULT_CATALOG,
    schema: str = "",
    access_token_cerberus_path: str = "",
    checkfirst: bool = False,
    bind: Union[Engine, Connection, None] = None,
    undeclared: bool = False,
    undeclared_only: bool = False,
    views_only: bool = False,
    echo: bool = False,
) -> Any:
    if environment:
        assert environment in ENVIRONMENTS
        if environment == "published":
            # TODO: Implement published environment proxy view deletion
            raise NotImplementedError(
                "The published environment is not yet supported."
            )
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
    bind = drop_all(
        Base,
        http_path=http_path,
        hostname=hostname,
        access_token=access_token,
        catalog=catalog,
        schema=schema,
        access_token_cerberus_path=access_token_cerberus_path,
        checkfirst=checkfirst,
        echo=echo,
        undeclared=undeclared,
        undeclared_only=undeclared_only,
        views_only=views_only,
    )

    return bind


@apply_environment_defaults("test", **TEST_DEFAULTS)
@apply_environment_defaults("dev", **DEV_DEFAULTS)
@apply_environment_defaults("qa", **QA_DEFAULTS)
@apply_environment_defaults("prod", **PROD_DEFAULTS)
@apply_environment_defaults("published", **PUBLISHED_DEFAULTS)
def validate_environment(
    environment: str,
    http_path: str = "",
    hostname: str = DEFAULT_HOSTNAME,
    access_token: str = "",
    catalog: str = DEFAULT_CATALOG,
    schema: str = "",
    access_token_cerberus_path: str = "",
    bind: Union[Engine, Connection, None] = None,
    echo: bool = False,
    only: Sequence[str] = (),
    ignore_foreign_keys: Union[
        Iterable[str], Callable[[ForeignKeyConstraint], bool], None
    ] = None,
    exclude_from_cache_validation: Union[
        Iterable[str], Callable[[Table], bool], None
    ] = None,
) -> Engine:
    if environment:
        assert environment in ENVIRONMENTS
        if environment == "published":
            # TODO: Implement published environment proxy view validation
            raise NotImplementedError(
                "The published environment is not yet supported."
            )
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

        validate(
            Base,
            bind,
            only=only,
            ignore_foreign_keys=ignore_foreign_keys,
            exclude_from_cache_validation=exclude_from_cache_validation,
        )
        return bind


def main() -> None:
    """
    This function is the entry point for the
    `my-datastore-model databricks` command.
    """
    arguments: argparse.Namespace = parse_arguments(
        "my-datastore-model databricks",
        environments=ENVIRONMENTS,
    )

    if arguments.command in COMMANDS:
        if arguments.command == "create":
            create_environment(
                environment=arguments.environment,
                access_token=arguments.access_token,
                http_path=arguments.http_path,
                catalog=arguments.catalog,
                schema=arguments.schema,
                echo=arguments.echo,
                views_only=arguments.views_only,
                checkfirst=arguments.checkfirst,
                access_token_cerberus_path=(
                    arguments.access_token_cerberus_path
                ),
            )
        elif arguments.command == "drop":
            drop_environment(
                environment=arguments.environment,
                access_token=arguments.access_token,
                http_path=arguments.http_path,
                catalog=arguments.catalog,
                schema=arguments.schema,
                echo=arguments.echo,
                views_only=arguments.views_only,
                checkfirst=arguments.checkfirst,
                access_token_cerberus_path=(
                    arguments.access_token_cerberus_path
                ),
                undeclared=arguments.undeclared,
                undeclared_only=arguments.undeclared_only,
            )
        elif arguments.command == "validate":
            validate_environment(
                environment=arguments.environment,
                access_token=arguments.access_token,
                http_path=arguments.http_path,
                catalog=arguments.catalog,
                schema=arguments.schema,
                echo=arguments.echo,
                access_token_cerberus_path=(
                    arguments.access_token_cerberus_path
                ),
                only=arguments.only_validate,
                ignore_foreign_keys=arguments.ignore_foreign_key,
                exclude_from_cache_validation=(
                    arguments.exclude_from_cache_validation
                ),
            )


if __name__ == "__main__":
    main()
