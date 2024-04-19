import argparse
import logging
from typing import (
    Any,
    Callable,
    Collection,
    Dict,
    Iterable,
    List,
    Sequence,
    Tuple,
    Union,
)

from analytics_orm.snowflake import COMMANDS
from analytics_orm.snowflake import DEFAULT_ENVIRONMENTS as ENVIRONMENTS
from analytics_orm.snowflake import (
    DEFAULT_ROLE,
    DEFAULT_SCHEMA,
    DEFAULT_STAGE_FILE_FORMAT,
    CreateStageArguments,
    create_all,
    create_engine,
    create_stage,
    drop_all,
    get_connection_url,
    parse_arguments,
)
from analytics_orm.utilities import (
    apply_environment_defaults,
    apply_role_defaults,
)
from analytics_orm.validation import validate
from sqlalchemy.engine.base import Connection, Engine  # type: ignore
from sqlalchemy.engine.mock import MockConnection  # type: ignore
from sqlalchemy.engine.result import Result  # type: ignore
from sqlalchemy.engine.row import Row  # type: ignore
from sqlalchemy.engine.url import URL, make_url  # type: ignore
from sqlalchemy.sql.schema import ForeignKeyConstraint, Table  # type: ignore

from ..base import Base
from .s3 import BUCKET_NAME, ENVIRONMENTS_URLS, SEMANTIC_PATH

__all__: List[str] = [
    "get_environment_connection_url",
    "create_environment_engine",
    "create_environment_stage",
    "create_environment",
    "ENVIRONMENTS",
    "ROLES",
    "STAGE_NAME",
    "SCHEMAS",
    "get_bind_environment",
]

SCHEMAS: Tuple[str, ...] = (
    "COMMON_DIMENSION",
    "FND_SAMPLE",
    "STAGE",
)
ADMIN_ROLES: Tuple[str, ...] = (
    "APP_SNOWFLAKE_DEV_SDF_FOUNDATION_ADMIN",
    "APP_SNOWFLAKE_QA_SDF_FOUNDATION_ADMIN",
    "APP_SNOWFLAKE_PROD_SDF_FOUNDATION_ADMIN",
)
ROLES: Tuple[str, ...] = ADMIN_ROLES + (
    "APP_SNOWFLAKE_DEV_SDF_FOUNDATION_READWRITE",
    "APP_SNOWFLAKE_DEV_SDF_FOUNDATION_READ",
    "APP_SNOWFLAKE_QA_SDF_FOUNDATION_READWRITE",
    "APP_SNOWFLAKE_QA_SDF_FOUNDATION_READ",
    "APP_SNOWFLAKE_PROD_SDF_FOUNDATION_READWRITE",
    "APP_SNOWFLAKE_PROD_SDF_FOUNDATION_READ",
)
# Default stage name
STAGE_NAME: str = "STAGE.S3"
PERMISSION_GROUPS_VIEW_NAMES: Dict[str, Tuple[str, ...]] = {}

LEGACY_VIEWS: Dict[str, str] = {}
DEFAULTS: Dict[str, Any] = dict(
    schema=DEFAULT_SCHEMA,
    stage_name=STAGE_NAME,
    stage_file_format=DEFAULT_STAGE_FILE_FORMAT,
    checkfirst=True,
)
DEV_DEFAULTS: Dict[str, Any] = dict(
    database="SDF_FOUNDATION_DEV",
    warehouse="SDF_FOUNDATION_PREPROD",
    stage_storage_integration="S3_SF_SDF_DEV_INTEGRATION",
    stage_url=f"s3://{BUCKET_NAME}/dev/{SEMANTIC_PATH}",
    create_stage_arguments=(
        CreateStageArguments(
            name="STAGE.S3_SUSTAINABILITY_FOUNDATION",
            file_format=DEFAULT_STAGE_FILE_FORMAT,
            storage_integration=("S3_SF_SDF_DEV_INTEGRATION"),
            url=ENVIRONMENTS_URLS["dev"],
        ),
    ),
    **DEFAULTS,
)
QA_DEFAULTS: Dict[str, Any] = dict(
    database="SDF_FOUNDATION_QA",
    warehouse="SDF_FOUNDATION_PREPROD",
    stage_storage_integration="NGAP_SF_SUSTAINABILITY_QA_INTEGRATION",
    stage_url=f"s3://{BUCKET_NAME}/qa/{SEMANTIC_PATH}",
    create_stage_arguments=(
        CreateStageArguments(
            name="STAGE.S3_SUSTAINABILITY_FOUNDATION",
            file_format=DEFAULT_STAGE_FILE_FORMAT,
            storage_integration=("S3_SF_SDF_QA_INTEGRATION"),
            url=ENVIRONMENTS_URLS["qa"],
        ),
    ),
    **DEFAULTS,
)
PROD_DEFAULTS: Dict[str, Any] = dict(
    database="SDF_FOUNDATION_PROD",
    warehouse="SDF_FOUNDATION_PROD",
    stage_storage_integration="NGAP_SF_SUSTAINABILITY_PROD_INTEGRATION",
    stage_url=f"s3://{BUCKET_NAME}/prod/{SEMANTIC_PATH}",
    create_stage_arguments=(
        CreateStageArguments(
            name="STAGE.S3_SUSTAINABILITY_FOUNDATION",
            file_format=DEFAULT_STAGE_FILE_FORMAT,
            storage_integration=("S3_SF_SDF_PROD_INTEGRATION"),
            url=ENVIRONMENTS_URLS["prod"],
        ),
    ),
    **DEFAULTS,
)
# Admin defaults
ADMIN_DEV_DEFAULTS: Dict[str, Any] = dict(
    password_cerberus_path="app/sustainability/snowflake/a.SF.D.SDF.A",
    **DEV_DEFAULTS,
)
ADMIN_QA_DEFAULTS: Dict[str, Any] = dict(
    password_cerberus_path="app/sustainability/snowflake/a.SF.Q.SDF.A",
    **QA_DEFAULTS,
)
ADMIN_PROD_DEFAULTS: Dict[str, Any] = dict(
    password_cerberus_path="app/sustainability/snowflake/a.SF.P.SDF.A",
    **PROD_DEFAULTS,
)
# Read/Write defaults
READWRITE_DEV_DEFAULTS: Dict[str, Any] = dict(
    password_cerberus_path="app/sustainability/snowflake/a.SF.D.SDF.RW",
    **DEV_DEFAULTS,
)
READWRITE_QA_DEFAULTS: Dict[str, Any] = dict(
    password_cerberus_path="app/sustainability/snowflake/a.SF.Q.SDF.RW",
    **QA_DEFAULTS,
)
READWRITE_PROD_DEFAULTS: Dict[str, Any] = dict(
    password_cerberus_path="app/sustainability/snowflake/a.SF.P.SDF.RW",
    **PROD_DEFAULTS,
)
# Read defaults

READ_DEV_DEFAULTS: Dict[str, Any] = dict(
    password_cerberus_path="app/sustainability/snowflake/a.SF.D.SDF.RW",
    **DEV_DEFAULTS,
)
READ_QA_DEFAULTS: Dict[str, Any] = dict(
    password_cerberus_path="app/sustainability/snowflake/a.SF.Q.SDF.RW",
    **QA_DEFAULTS,
)
READ_PROD_DEFAULTS: Dict[str, Any] = dict(
    password_cerberus_path="app/sustainability/snowflake/a.SF.P.SDF.RW",
    **PROD_DEFAULTS,
)

# default number of days of data retention
DATA_RETENTION_TIME_IN_DAYS: int = 7

BI_DATA_WAREHOUSE = "SDF_FOUNDATION_PROD"


def _iter_environment_grants(
    environment: str, warehouse: str
) -> Iterable[str]:
    """
    Yield statements establishing suitable grants for an environment
    """
    environment = environment.upper()
    warehouse = warehouse.upper()
    yield from (
        f"USE ROLE APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_ADMIN",
        # Warehouse
        f"GRANT OPERATE,USAGE,MONITOR ON WAREHOUSE {warehouse} "
        f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_ADMIN",
        f"GRANT OPERATE,USAGE,MONITOR ON WAREHOUSE {warehouse} "
        f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_READ",
        f"GRANT OPERATE,USAGE,MONITOR ON WAREHOUSE {warehouse} "
        f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_READWRITE",
        # Database
        f"GRANT USAGE,MONITOR ON DATABASE SDF_FOUNDATION_{environment} "
        f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_READ",
        f"GRANT USAGE,MONITOR ON DATABASE SDF_FOUNDATION_{environment} "
        f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_READWRITE",
        f"GRANT OWNERSHIP ON DATABASE SDF_FOUNDATION_{environment} "
        f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_ADMIN",
        # Schemas
        "GRANT USAGE,MONITOR ON ALL SCHEMAS IN DATABASE "
        f"SDF_FOUNDATION_{environment} "
        f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_READ",
        "GRANT USAGE,MONITOR ON ALL SCHEMAS IN DATABASE "
        f"SDF_FOUNDATION_{environment} "
        f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_READWRITE",
        "GRANT OWNERSHIP ON ALL SCHEMAS IN DATABASE "
        f"SDF_FOUNDATION_{environment} "
        f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_ADMIN",
        # Stage
        f"GRANT READ,USAGE ON ALL STAGES IN SCHEMA "
        f"SDF_FOUNDATION_{environment}.STAGE "
        f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_READ",
        "GRANT ALL ON ALL STAGES IN SCHEMA "
        f"SDF_FOUNDATION_{environment}.STAGE "
        f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_READWRITE",
        f"GRANT OWNERSHIP ON ALL STAGES IN SCHEMA "
        f"SDF_FOUNDATION_{environment}.STAGE "
        f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_ADMIN",
    )
    # Display roles only apply to PROD
    if environment == "PROD":
        yield from (
            f"GRANT USAGE,MONITOR ON DATABASE SDF_FOUNDATION_{environment} "
            f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_DISPLAY",
            f"GRANT USAGE,MONITOR ON ALL SCHEMAS IN DATABASE "
            f"SDF_FOUNDATION_{environment} "
            f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_DISPLAY",
            f"GRANT READ,USAGE ON ALL STAGES IN SCHEMA "
            f"SDF_FOUNDATION_{environment}.STAGE "
            f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_DISPLAY",
        )
    schema: str
    for schema in filter(lambda schema: schema != "STAGE", SCHEMAS):
        # Display roles only apply to PROD
        if environment == "PROD":
            yield (
                "GRANT SELECT ON ALL TABLES IN SCHEMA "
                f"SDF_FOUNDATION_{environment}.{schema} TO "
                f"APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_DISPLAY"
            )
        yield from (
            # Tables/Views
            # READ
            "GRANT SELECT ON ALL TABLES IN SCHEMA "
            f"SDF_FOUNDATION_{environment}.{schema} "
            f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_READ",
            "GRANT SELECT ON ALL VIEWS IN SCHEMA "
            f"SDF_FOUNDATION_{environment}.{schema} "
            f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_READ",
            # READWRITE
            "GRANT ALL ON ALL TABLES IN SCHEMA "
            f"SDF_FOUNDATION_{environment}.{schema} "
            f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_READWRITE",
            "GRANT ALL ON ALL VIEWS IN SCHEMA "
            f"SDF_FOUNDATION_{environment}.{schema} "
            f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_READWRITE",
            # ADMIN
            "GRANT OWNERSHIP ON ALL TABLES IN SCHEMA "
            f"SDF_FOUNDATION_{environment}.{schema} "
            f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_ADMIN",
            "GRANT OWNERSHIP ON ALL VIEWS IN SCHEMA "
            f"SDF_FOUNDATION_{environment}.{schema} "
            f"TO APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_ADMIN",
        )


@apply_role_defaults("GSA_FOUNDATION_ADMIN_DEV", **ADMIN_DEV_DEFAULTS)
@apply_role_defaults("GSA_FOUNDATION_ADMIN_QA", **ADMIN_QA_DEFAULTS)
@apply_role_defaults("GSA_FOUNDATION_ADMIN_PROD", **ADMIN_PROD_DEFAULTS)
@apply_role_defaults("GSA_FOUNDATION_READWRITE_DEV", **READWRITE_DEV_DEFAULTS)
@apply_role_defaults("GSA_FOUNDATION_READWRITE_QA", **READWRITE_QA_DEFAULTS)
@apply_role_defaults(
    "APP_SNOWFLAKE_DEV_SDF_FOUNDATION_ADMIN", **ADMIN_DEV_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_QA_SDF_FOUNDATION_ADMIN", **ADMIN_QA_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_PROD_SDF_FOUNDATION_ADMIN", **ADMIN_PROD_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_DEV_SDF_FOUNDATION_READWRITE", **READWRITE_DEV_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_QA_SDF_FOUNDATION_READWRITE", **READWRITE_QA_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_PROD_SDF_FOUNDATION_READWRITE", **READWRITE_PROD_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_DEV_SDF_FOUNDATION_READ", **READ_DEV_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_QA_SDF_FOUNDATION_READ", **READ_QA_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_PROD_SDF_FOUNDATION_READ", **READ_PROD_DEFAULTS
)
@apply_environment_defaults(
    "dev", role="APP_SNOWFLAKE_DEV_SDF_FOUNDATION_READ", **READ_DEV_DEFAULTS
)
@apply_environment_defaults(
    "qa", role="APP_SNOWFLAKE_QA_SDF_FOUNDATION_READ", **READ_QA_DEFAULTS
)
@apply_environment_defaults(
    "prod", role="APP_SNOWFLAKE_PROD_SDF_FOUNDATION_READ", **READ_PROD_DEFAULTS
)
def get_environment_connection_url(
    environment: str = "",
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
    This function assembles and returns a snowflake bind string,
    with defaults determined by either the environment or the role which is
    provided.

    Parameters:

    - *environment* (str) = ""
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

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of Org's [vaults](https://prod.cerberus.mycloud.com). For
    example: "app/sustainability/snowlake-prod/password".

    - user_cerberus_path (str) = ""
    - password_cerberus_path (str) = ""
    - database_cerberus_path (str) = ""
    - warehouse_cerberus_path (str) = ""
    - schema_cerberus_path (str) = ""
    - role_cerberus_path (str) = ""
    - authenticator_cerberus_path (str) = ""
    """
    if environment:
        assert environment in ENVIRONMENTS
    return get_connection_url(
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
    )


# For backwards compatibility
get_environment_connection_string: Callable = get_environment_connection_url


@apply_role_defaults(
    "APP_SNOWFLAKE_DEV_SDF_FOUNDATION_ADMIN", **ADMIN_DEV_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_QA_SDF_FOUNDATION_ADMIN", **ADMIN_QA_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_PROD_SDF_FOUNDATION_ADMIN", **ADMIN_PROD_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_DEV_SDF_FOUNDATION_READWRITE", **READWRITE_DEV_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_QA_SDF_FOUNDATION_READWRITE", **READWRITE_QA_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_PROD_SDF_FOUNDATION_READWRITE", **READWRITE_PROD_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_DEV_SDF_FOUNDATION_READ", **READ_DEV_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_QA_SDF_FOUNDATION_READ", **READ_QA_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_PROD_SDF_FOUNDATION_READ", **READ_PROD_DEFAULTS
)
@apply_environment_defaults(
    "dev", role="APP_SNOWFLAKE_DEV_SDF_FOUNDATION_READ", **READ_DEV_DEFAULTS
)
@apply_environment_defaults(
    "qa", role="APP_SNOWFLAKE_QA_SDF_FOUNDATION_READ", **READ_QA_DEFAULTS
)
@apply_environment_defaults(
    "prod", role="APP_SNOWFLAKE_PROD_SDF_FOUNDATION_READ", **READ_PROD_DEFAULTS
)
def create_environment_engine(
    environment: str = "",
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
) -> URL:
    """
    This function create a SQLAlchemy bind engine,
    with defaults determined by either the `environment` or the `role`
    provided.

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

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of Org's [vaults](https://prod.cerberus.mycloud.com). For
    example: "app/sustainability/snowlake-prod/password".

    - user_cerberus_path (str) = ""
    - password_cerberus_path (str) = ""
    - database_cerberus_path (str) = ""
    - warehouse_cerberus_path (str) = ""
    - schema_cerberus_path (str) = ""
    - role_cerberus_path (str) = ""
    - authenticator_cerberus_path (str) = ""
    """
    if environment:
        assert environment in ENVIRONMENTS
    if role:
        assert role in ROLES
    return create_engine(
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
        echo=echo,
        use_secondary_roles=use_secondary_roles,
    )


@apply_role_defaults(
    "APP_SNOWFLAKE_DEV_SDF_FOUNDATION_ADMIN", **ADMIN_DEV_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_QA_SDF_FOUNDATION_ADMIN", **ADMIN_QA_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_PROD_SDF_FOUNDATION_ADMIN", **ADMIN_PROD_DEFAULTS
)
@apply_environment_defaults(
    "dev", role="APP_SNOWFLAKE_DEV_SDF_FOUNDATION_ADMIN", **ADMIN_DEV_DEFAULTS
)
@apply_environment_defaults(
    "qa", role="APP_SNOWFLAKE_QA_SDF_FOUNDATION_ADMIN", **ADMIN_QA_DEFAULTS
)
@apply_environment_defaults(
    "prod",
    role="APP_SNOWFLAKE_PROD_SDF_FOUNDATION_ADMIN",
    **ADMIN_PROD_DEFAULTS,
)
def create_environment_stage(
    environment: str = "",
    user: str = "",
    password: str = "",
    database: str = "",
    warehouse: str = "",
    schema: str = DEFAULT_SCHEMA,
    role: str = DEFAULT_ROLE,
    authenticator: str = "",
    echo: bool = False,
    stage_name: str = STAGE_NAME,
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
    create_stage_arguments: Tuple[CreateStageArguments, ...] = (),
) -> URL:
    """
    This function creates the stage for data to land in Snowflake from S3
    with defaults determined by either the environment or the role
    which is provided.

    Parameters:

    - *environment* (str) = ""
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
    - stage_file_format (str)
    - stage_url (str)
    - stage_storage_integration (str)

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of Org's [vaults](https://prod.cerberus.mycloud.com). For
    example: "app/sustainability/snowlake-prod/password".

    - user_cerberus_path (str) = ""
    - password_cerberus_path (str) = ""
    - database_cerberus_path (str) = ""
    - warehouse_cerberus_path (str) = ""
    - schema_cerberus_path (str) = ""
    - role_cerberus_path (str) = ""
    - authenticator_cerberus_path (str) = ""
    """
    if role and not bind:
        assert role in ADMIN_ROLES
    if environment:
        assert environment in ENVIRONMENTS
    return create_stage(
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
        create_stage_arguments=create_stage_arguments,
    )


@apply_role_defaults(
    "APP_SNOWFLAKE_DEV_SDF_FOUNDATION_ADMIN", **ADMIN_DEV_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_QA_SDF_FOUNDATION_ADMIN", **ADMIN_QA_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_PROD_SDF_FOUNDATION_ADMIN", **ADMIN_PROD_DEFAULTS
)
@apply_environment_defaults(
    "dev", role="APP_SNOWFLAKE_DEV_SDF_FOUNDATION_ADMIN", **ADMIN_DEV_DEFAULTS
)
@apply_environment_defaults(
    "qa", role="APP_SNOWFLAKE_QA_SDF_FOUNDATION_ADMIN", **ADMIN_QA_DEFAULTS
)
@apply_environment_defaults(
    "prod",
    role="APP_SNOWFLAKE_PROD_SDF_FOUNDATION_ADMIN",
    **ADMIN_PROD_DEFAULTS,
)
def create_environment(
    environment: str = "",
    user: str = "",
    password: str = "",
    database: str = "",
    warehouse: str = "",
    schema: str = DEFAULT_SCHEMA,
    role: str = DEFAULT_ROLE,
    authenticator: str = "",
    checkfirst: bool = False,
    echo: bool = False,
    stage_name: str = STAGE_NAME,
    stage_file_format: str = DEFAULT_STAGE_FILE_FORMAT,
    stage_url: str = "",
    stage_storage_integration: str = "",
    views_only: bool = False,
    bind: Union[Engine, Connection, None] = None,
    user_cerberus_path: str = "",
    password_cerberus_path: str = "",
    database_cerberus_path: str = "",
    warehouse_cerberus_path: str = "",
    schema_cerberus_path: str = "",
    role_cerberus_path: str = "",
    authenticator_cerberus_path: str = "",
    use_secondary_roles: bool = True,
    create_stage_arguments: Tuple[CreateStageArguments, ...] = (),
) -> URL:
    """
    This function creates views, tables, and schemas

    Parameters:

    - *environment* (str) = ""
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
    - checkfirst (bool) = False
    - echo (bool) = False
    - views_only (bool) = False: If `True`, only views and their schemas
      are created (tables are not).

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of Org's [vaults](https://prod.cerberus.mycloud.com). For
    example: "app/sustainability/snowflake-prod/password".

    - user_cerberus_path (str) = ""
    - password_cerberus_path (str) = ""
    - database_cerberus_path (str) = ""
    - warehouse_cerberus_path (str) = ""
    - schema_cerberus_path (str) = ""
    - role_cerberus_path (str) = ""
    - authenticator_cerberus_path (str) = ""
    - use_secondary_roles (bool) = True
    """
    if role and not bind:
        assert role in ADMIN_ROLES, f"{role} is not an admin role"
    if environment:
        assert environment in ENVIRONMENTS
    bind = create_engine(
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
        echo=echo,
        use_secondary_roles=use_secondary_roles,
    )
    for new_views in LEGACY_VIEWS.values():
        bind.execute(f"DROP VIEW IF EXISTS {new_views}")
    # Create schemas that don't have any tables
    _create_bind_schemas(bind=bind, database=database, checkfirst=checkfirst)
    print("_create_bind_schemas")
    bind = create_all(
        Base,
        user=user,
        password=password,
        database=database,
        warehouse=warehouse,
        schema=schema,
        role=role,
        authenticator=authenticator,
        checkfirst=checkfirst,
        echo=echo,
        stage_name=stage_name,
        stage_file_format=stage_file_format,
        stage_url=stage_url,
        stage_storage_integration=stage_storage_integration,
        views_only=views_only,
        user_cerberus_path=user_cerberus_path,
        password_cerberus_path=password_cerberus_path,
        database_cerberus_path=database_cerberus_path,
        warehouse_cerberus_path=warehouse_cerberus_path,
        schema_cerberus_path=schema_cerberus_path,
        role_cerberus_path=role_cerberus_path,
        authenticator_cerberus_path=authenticator_cerberus_path,
        bind=bind,
        use_secondary_roles=use_secondary_roles,
        create_stage_arguments=create_stage_arguments,
    )
    for legacy_view, new_view in LEGACY_VIEWS.items():
        bind.execute(
            f"CREATE OR REPLACE VIEW {legacy_view} AS SELECT * FROM {new_view}"
        )
    # Setup permissions
    _grant_bind_permissions(
        bind=bind, environment=environment, warehouse=warehouse
    )
    _set_database_parameters(bind=bind, environment=environment)
    return bind


@apply_role_defaults(
    "APP_SNOWFLAKE_DEV_SDF_FOUNDATION_ADMIN", **ADMIN_DEV_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_QA_SDF_FOUNDATION_ADMIN", **ADMIN_QA_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_PROD_SDF_FOUNDATION_ADMIN", **ADMIN_PROD_DEFAULTS
)
@apply_environment_defaults(
    "dev", role="APP_SNOWFLAKE_DEV_SDF_FOUNDATION_ADMIN", **ADMIN_DEV_DEFAULTS
)
@apply_environment_defaults(
    "qa", role="APP_SNOWFLAKE_QA_SDF_FOUNDATION_ADMIN", **ADMIN_QA_DEFAULTS
)
@apply_environment_defaults(
    "prod",
    role="APP_SNOWFLAKE_PROD_SDF_FOUNDATION_ADMIN",
    **ADMIN_PROD_DEFAULTS,
)
def drop_environment(
    environment: str = "",
    user: str = "",
    password: str = "",
    database: str = "",
    warehouse: str = "",
    schema: str = DEFAULT_SCHEMA,
    role: str = DEFAULT_ROLE,
    authenticator: str = "",
    checkfirst: bool = False,
    echo: bool = False,
    views_only: bool = False,
    user_cerberus_path: str = "",
    password_cerberus_path: str = "",
    database_cerberus_path: str = "",
    warehouse_cerberus_path: str = "",
    schema_cerberus_path: str = "",
    role_cerberus_path: str = "",
    authenticator_cerberus_path: str = "",
    bind: Union[Engine, Connection, None] = None,
    undeclared: bool = False,
    undeclared_only: bool = False,
    use_secondary_roles: bool = True,
) -> URL:
    """
    This function drop views and (optionally) tables in the target database

    Parameters:

    - *environment* (str) = ""
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
    - checkfirst (bool) = False
    - echo (bool) = False
    - views_only (bool) = False: If `True`, only views and their schemas
      are created (tables are not).

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of Org's [vaults](https://prod.cerberus.mycloud.com). For
    example: "app/sustainability/snowlake-prod/password".

    - user_cerberus_path (str) = ""
    - password_cerberus_path (str) = ""
    - database_cerberus_path (str) = ""
    - warehouse_cerberus_path (str) = ""
    - schema_cerberus_path (str) = ""
    - role_cerberus_path (str) = ""
    - authenticator_cerberus_path (str) = ""
    """
    if role and not bind:
        assert role in ADMIN_ROLES
    if environment:
        assert environment in ENVIRONMENTS
    return drop_all(
        Base,
        user=user,
        password=password,
        database=database,
        warehouse=warehouse,
        schema=schema,
        role=role,
        authenticator=authenticator,
        checkfirst=checkfirst,
        echo=echo,
        views_only=views_only,
        user_cerberus_path=user_cerberus_path,
        password_cerberus_path=password_cerberus_path,
        database_cerberus_path=database_cerberus_path,
        warehouse_cerberus_path=warehouse_cerberus_path,
        schema_cerberus_path=schema_cerberus_path,
        role_cerberus_path=role_cerberus_path,
        authenticator_cerberus_path=authenticator_cerberus_path,
        bind=bind,
        undeclared=undeclared,
        undeclared_only=undeclared_only,
        use_secondary_roles=use_secondary_roles,
    )


@apply_role_defaults(
    "APP_SNOWFLAKE_DEV_SDF_FOUNDATION_ADMIN", **ADMIN_DEV_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_QA_SDF_FOUNDATION_ADMIN", **ADMIN_QA_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_PROD_SDF_FOUNDATION_ADMIN", **ADMIN_PROD_DEFAULTS
)
@apply_environment_defaults(
    "dev", role="APP_SNOWFLAKE_DEV_SDF_FOUNDATION_ADMIN", **ADMIN_DEV_DEFAULTS
)
@apply_environment_defaults(
    "qa", role="APP_SNOWFLAKE_QA_SDF_FOUNDATION_ADMIN", **ADMIN_QA_DEFAULTS
)
@apply_environment_defaults(
    "prod",
    role="APP_SNOWFLAKE_PROD_SDF_FOUNDATION_ADMIN",
    **ADMIN_PROD_DEFAULTS,
)
def grant_environment_permissions(
    environment: str = "",
    user: str = "",
    password: str = "",
    database: str = "",
    warehouse: str = "",
    schema: str = DEFAULT_SCHEMA,
    role: str = DEFAULT_ROLE,
    authenticator: str = "",
    echo: bool = False,
    user_cerberus_path: str = "",
    password_cerberus_path: str = "",
    database_cerberus_path: str = "",
    warehouse_cerberus_path: str = "",
    schema_cerberus_path: str = "",
    role_cerberus_path: str = "",
    authenticator_cerberus_path: str = "",
    bind: Union[Engine, Connection, None] = None,
    use_secondary_roles: bool = True,
) -> URL:
    """
    This function grants appropriate permissions for the specified environment.

    Parameters:

    - *environment* (str) = ""
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
    - echo (bool) = False
    - views_only (bool) = False: If `True`, only views and their schemas
      are created (tables are not).

    ...the following parameters are a path + key to a cerberus secret stored
    in a one of Org's [vaults](https://prod.cerberus.mycloud.com). For
    example: "app/sustainability/snowlake-prod/password".

    - user_cerberus_path (str) = ""
    - password_cerberus_path (str) = ""
    - database_cerberus_path (str) = ""
    - warehouse_cerberus_path (str) = ""
    - schema_cerberus_path (str) = ""
    - role_cerberus_path (str) = ""
    - authenticator_cerberus_path (str) = ""
    """
    if role and not bind:
        assert role in ADMIN_ROLES
    if environment:
        assert environment in ENVIRONMENTS, environment
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
    _grant_bind_permissions(
        bind=bind, environment=environment, warehouse=warehouse
    )
    return bind


def _create_bind_schemas(
    bind: Union[Engine, Connection], database: str, checkfirst: bool
) -> None:
    if bind and not database:
        database = _get_bind_database(bind)
    if_not_exists: str = "IF NOT EXISTS " if checkfirst else ""
    schema_name: str
    for schema_name in SCHEMAS:
        bind.execute(f"CREATE SCHEMA {if_not_exists} {database}.{schema_name}")


def _get_bind_database(bind: Union[Engine, Connection]) -> str:
    if isinstance(bind, MockConnection):
        return ""
    engine: Engine = bind.engine
    url: URL = engine.url
    return url.database.split("/")[0]


def _get_bind_warehouse(bind: Union[Engine, Connection]) -> str:
    engine: Engine = bind.engine
    url: URL = engine.url
    return url.query["warehouse"]


def _grant_bind_permissions(
    bind: Union[Engine, Connection], environment: str = "", warehouse: str = ""
) -> None:
    if not environment:
        environment = _get_bind_database(bind).split("_")[-1].lower()
    # If the bind is a mock connection there will be no environment
    if not environment:
        return
    assert environment in ENVIRONMENTS, environment
    if not warehouse:
        warehouse = _get_bind_warehouse(bind)
    # Grant sustainability role privileges
    statement: str
    for statement in _iter_environment_grants(environment, warehouse):
        logging.info(statement)
        result: Result = bind.execute(statement)
        logging.info(repr(result))
    # Grant Third-party role privileges
    if environment == "prod":
        _bind_environment_grant_display_read_roles(
            bind, environment, warehouse
        )
        _bind_environment_grant_display_read_roles(
            bind, environment, BI_DATA_WAREHOUSE
        )


def _set_database_parameters(
    bind: Union[Engine, Connection], environment: str = ""
) -> None:
    if environment == "prod":
        bind.execute("COMMIT")
        bind.execute(
            f"ALTER DATABASE SDF_FOUNDATION_{environment.upper()} "
            f"SET DATA_RETENTION_TIME_IN_DAYS={DATA_RETENTION_TIME_IN_DAYS}"
        )


def _iter_role_read_views_grants(
    role: str,
    view_names: Collection[str],
    environment: str,
    warehouse: str = "",
) -> Iterable[str]:
    """
    This function accepts a role, collection of qualified view names
    (view names which include the schema), environment name, and warehouse
    name, then yields GRANT statements for applying permissions for
    the role.
    """
    assert environment in ENVIRONMENTS
    environment = environment.upper()
    yield f"USE ROLE APP_SNOWFLAKE_{environment}_SDF_FOUNDATION_ADMIN"
    if warehouse:
        yield f"GRANT OPERATE,USAGE,MONITOR ON WAREHOUSE {warehouse} TO {role}"
    yield (
        f"GRANT USAGE,MONITOR ON DATABASE SDF_FOUNDATION_"
        f"{environment} TO {role}"
    )
    view_name: str
    schema: str
    for schema in map(
        lambda view_name: view_name.partition(".")[0], view_names
    ):
        yield (
            "GRANT USAGE,MONITOR ON SCHEMA "
            f"SDF_FOUNDATION_{environment}.{schema} TO {role}"
        )
    for view_name in view_names:
        # First ensure the view name is fully qualified (includes a schema)
        assert "." in view_name
        yield (
            "GRANT SELECT ON TABLE "
            f"SDF_FOUNDATION_{environment}.{view_name} "
            f"TO {role}"
        )


def _bind_environment_grant_display_read_roles(
    bind: Union[Engine, Connection], environment: str, warehouse: str
) -> None:
    role_warehouse: str
    role_type: str
    uppercase_environment: str = environment.upper()
    for role_type, role_warehouse in (("DISPLAY", ""), ("READ", warehouse)):
        group: str
        views: Tuple[str, ...]
        for group, views in PERMISSION_GROUPS_VIEW_NAMES.items():
            row: Row
            for statement in _iter_role_read_views_grants(
                role=(
                    f"APP_SNOWFLAKE_{uppercase_environment}_"
                    f"SDF_FOUNDATION_{group}_{role_type}"
                ),
                view_names=views,
                environment=environment,
                warehouse=role_warehouse,
            ):
                logging.info(statement)
                for row in bind.execute(statement):
                    logging.info(repr(row))


@apply_role_defaults(
    "APP_SNOWFLAKE_DEV_SDF_FOUNDATION_ADMIN", **ADMIN_DEV_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_QA_SDF_FOUNDATION_ADMIN", **ADMIN_QA_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_PROD_SDF_FOUNDATION_ADMIN", **ADMIN_PROD_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_DEV_SDF_FOUNDATION_READWRITE", **READWRITE_DEV_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_QA_SDF_FOUNDATION_READWRITE", **READWRITE_QA_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_PROD_SDF_FOUNDATION_READWRITE", **READWRITE_PROD_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_DEV_SDF_FOUNDATION_READ", **READ_DEV_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_QA_SDF_FOUNDATION_READ", **READ_QA_DEFAULTS
)
@apply_role_defaults(
    "APP_SNOWFLAKE_PROD_SDF_FOUNDATION_READ", **READ_PROD_DEFAULTS
)
@apply_environment_defaults(
    "dev", role="APP_SNOWFLAKE_DEV_SDF_FOUNDATION_READ", **READ_DEV_DEFAULTS
)
@apply_environment_defaults(
    "qa", role="APP_SNOWFLAKE_QA_SDF_FOUNDATION_READ", **READ_QA_DEFAULTS
)
@apply_environment_defaults(
    "prod", role="APP_SNOWFLAKE_PROD_SDF_FOUNDATION_READ", **READ_PROD_DEFAULTS
)
def validate_environment(
    environment: str = "",
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
    bind: Union[Engine, Connection, None] = None,
    use_secondary_roles: bool = True,
    only: Sequence[str] = (),
    ignore_foreign_keys: Union[
        Iterable[str], Callable[[ForeignKeyConstraint], bool], None
    ] = None,
    exclude_from_cache_validation: Union[
        Iterable[str], Callable[[Table], bool], None
    ] = None,
) -> Engine:
    """
    Validate the specified `environment` or `bind` against sub-classes of
    `my_database_orm.base.Base`.

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
    in a one of Org's [vaults](https://prod.cerberus.mycloud.com). For
    example: "app/sustainability/snowlake-prod/password".

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
    )
    return bind


def main() -> None:
    """
    This function is the entry point for the
    `my-datastore-orm snowflake` command.
    """
    arguments: argparse.Namespace = parse_arguments(
        "my-datastore-orm snowflake",
        environments=ENVIRONMENTS,
        roles=ROLES,
    )
    if arguments.command in COMMANDS:
        if arguments.command == "create":
            create_environment(
                environment=arguments.environment,
                user=arguments.user,
                password=arguments.password,
                database=arguments.database,
                schema=arguments.schema,
                warehouse=arguments.warehouse,
                role=arguments.role,
                authenticator=arguments.authenticator,
                stage_name=arguments.stage_name,
                stage_file_format=arguments.stage_file_format,
                stage_url=arguments.stage_url,
                stage_storage_integration=arguments.stage_storage_integration,
                echo=arguments.echo,
                views_only=arguments.views_only,
                checkfirst=arguments.checkfirst,
                user_cerberus_path=arguments.user_cerberus_path,
                password_cerberus_path=arguments.password_cerberus_path,
                schema_cerberus_path=arguments.schema_cerberus_path,
                database_cerberus_path=arguments.database_cerberus_path,
                warehouse_cerberus_path=arguments.warehouse_cerberus_path,
                authenticator_cerberus_path=(
                    arguments.authenticator_cerberus_path
                ),
                role_cerberus_path=arguments.role_cerberus_path,
                use_secondary_roles=(not arguments.dont_use_secondary_roles),
            )
        elif arguments.command == "drop":
            drop_environment(
                environment=arguments.environment,
                user=arguments.user,
                password=arguments.password,
                database=arguments.database,
                schema=arguments.schema,
                warehouse=arguments.warehouse,
                role=arguments.role,
                authenticator=arguments.authenticator,
                echo=arguments.echo,
                views_only=arguments.views_only,
                checkfirst=arguments.checkfirst,
                user_cerberus_path=arguments.user_cerberus_path,
                password_cerberus_path=arguments.password_cerberus_path,
                schema_cerberus_path=arguments.schema_cerberus_path,
                database_cerberus_path=arguments.database_cerberus_path,
                warehouse_cerberus_path=arguments.warehouse_cerberus_path,
                authenticator_cerberus_path=(
                    arguments.authenticator_cerberus_path
                ),
                role_cerberus_path=arguments.role_cerberus_path,
                undeclared=arguments.undeclared,
                undeclared_only=arguments.undeclared_only,
                use_secondary_roles=(not arguments.dont_use_secondary_roles),
            )
        elif arguments.command == "validate":
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
                authenticator_cerberus_path=(
                    arguments.authenticator_cerberus_path
                ),
                role_cerberus_path=arguments.role_cerberus_path,
                use_secondary_roles=(not arguments.dont_use_secondary_roles),
                only=arguments.only_validate,
                ignore_foreign_keys=arguments.ignore_foreign_key,
                exclude_from_cache_validation=(
                    arguments.exclude_from_cache_validation
                ),
            )


def get_bind_environment(bind: Union[Engine, Connection, URL, str]) -> str:
    """
    Get the name of the environment associated with a bind:
    dev | qa | prod
    """
    url: Union[URL, str] = ""
    if isinstance(bind, Connection):
        url = bind.engine.url
    elif isinstance(bind, Engine):
        url = bind.url
    elif isinstance(bind, (URL, str)):
        url = bind
    if url and isinstance(url, str):
        url = make_url(url)
    if url and url.drivername.split("+")[0] == "snowflake":
        database: str = url.database.split("/")[0]
        if database == DEV_DEFAULTS["database"]:
            return "dev"
        elif database == QA_DEFAULTS["database"]:
            return "qa"
        elif database == PROD_DEFAULTS["database"]:
            return "prod"
    return ""


if __name__ == "__main__":
    main()
