from argparse import Namespace
from typing import TYPE_CHECKING, Callable, Optional, Sequence, Union

from analytics_orm.snowflake import parse_arguments
from analytics_orm.utilities import (
    apply_environment_defaults,
    apply_role_defaults,
)
from my_datastore_model.base import Base
from my_datastore_model.dialects.snowflake import (
    DEFAULT_ROLE,
    DEFAULT_SCHEMA,
    ENVIRONMENTS,
    READ_DEV_DEFAULTS,
    READ_PROD_DEFAULTS,
    READ_QA_DEFAULTS,
    ROLES,
    create_environment_engine,
)
from sqlalchemy.engine.base import Connection, Engine  # type: ignore
from sqlalchemy.sql.schema import ForeignKeyConstraint, Table  # type: ignore

from ..base import validate


@apply_role_defaults("SNOWFLAKE_READ_DEV", **READ_DEV_DEFAULTS)
@apply_role_defaults("SNOWFLAKE_READ_QA", **READ_QA_DEFAULTS)
@apply_role_defaults("SNOWFLAKE_READ_PROD", **READ_PROD_DEFAULTS)
@apply_environment_defaults(
    "dev", role="SNOWFLAKE_READ_DEV", **READ_DEV_DEFAULTS
)
@apply_environment_defaults(
    "qa", role="SNOWFLAKE_READ_QA", **READ_QA_DEFAULTS
)
@apply_environment_defaults(
    "prod", role="SNOWFLAKE_READ_PROD", **READ_PROD_DEFAULTS
)
def validate_environment(
    environment: str = "",
    user: str = "",
    password: Optional[str] = None,
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
    bind: Union[Engine, Connection, None] = None,
    use_secondary_roles: bool = True,
    only: Sequence[str] = (),
    ignore_foreign_keys: Union[
        Sequence[str], Callable[[ForeignKeyConstraint], bool], None
    ] = None,
    exclude_from_cache_validation: Union[
        Sequence[str], Callable[[Table], bool], None
    ] = "*",
) -> Engine:
    """
    Validate the specified `environment` or `bind` against sub-classes of
    `my_datastore_model.base.Base`.

    Parameters:

    - environment (str) = ""
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
    - use_secondary_roles (bool)
    - ignore_foreign_keys ([str])
    - exclude_from_cache_validation ([str])

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of the [vaults](https://prod.cerberus.orgcloud.com). For
    example: "app/org/snowlake-prod/password".

    - user_cerberus_path (str) = ""
    - password_cerberus_path (str) = ""
    - database_cerberus_path (str) = ""
    - warehouse_cerberus_path (str) = ""
    - schema_cerberus_path (str) = ""
    - role_cerberus_path (str) = ""
    - authenticator_cerberus_path (str) = ""
    """
    if not bind:
        bind = create_environment_engine(
            environment=environment,
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
    validate(
        Base,
        bind,
        only=only,
        ignore_foreign_keys=ignore_foreign_keys,
        exclude_from_cache_validation=exclude_from_cache_validation,
        echo=echo,
    )
    if isinstance(bind, Engine):
        return bind
    else:
        if TYPE_CHECKING:
            assert bind and isinstance(bind.engine, Engine)
        return bind.engine


def main() -> None:
    """
    This function is the entry point for the
    `my-datastore-model snowflake` command.
    """
    arguments: Namespace = parse_arguments(
        "my-datastore-validation snowflake",
        environments=ENVIRONMENTS,
        roles=ROLES,
        commands=(),
        include=(
            "authenticator_cerberus_path",
            "authenticator",
            "database_cerberus_path",
            "database",
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
            "user_cerberus_path",
            "user",
            "warehouse_cerberus_path",
            "warehouse",
        ),
    )
    validate_environment(
        environment=arguments.environment,
        user=arguments.user,
        password=arguments.password,
        database=arguments.database,
        schema=arguments.schema,
        warehouse=arguments.warehouse,
        role=arguments.role,
        authenticator=arguments.authenticator,
        echo=arguments.echo,
        user_cerberus_path=arguments.user_cerberus_path,
        password_cerberus_path=arguments.password_cerberus_path,
        schema_cerberus_path=arguments.schema_cerberus_path,
        database_cerberus_path=arguments.database_cerberus_path,
        warehouse_cerberus_path=arguments.warehouse_cerberus_path,
        authenticator_cerberus_path=arguments.authenticator_cerberus_path,
        role_cerberus_path=arguments.role_cerberus_path,
        only=arguments.only_validate,
        ignore_foreign_keys=arguments.ignore_foreign_key,
        exclude_from_cache_validation=(
            arguments.exclude_from_cache_validation
        ),
    )
