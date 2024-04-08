import json
import logging
import os
from argparse import ArgumentParser, Namespace
from tempfile import gettempdir
from typing import Any, FrozenSet, Iterable, Sequence, Tuple

COMMANDS: Tuple[str, ...] = ("create", "drop", "validate")
ENVIRONMENTS: Tuple[str, str, str] = ("dev", "qa", "prod")


def _normalize_included_parameter_name(name: str) -> str:
    return name.strip("- ").replace("-", "_")


def _normalize_include_argument(include: Iterable[str]) -> FrozenSet[str]:
    if isinstance(include, str):
        include = (include,)
    return frozenset(map(_normalize_included_parameter_name, include))


def parse_arguments(
    prog: str = "",
    environments: Sequence[str] = ENVIRONMENTS,
    roles: Sequence[str] = (),
    commands: Sequence[str] = COMMANDS,
    include: Iterable[str] = (),
) -> Namespace:
    """
    Parse CLI arguments and return the resulting instance of
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
    - include ({str}): A `frozenset` of all parameters to include. If not
      provided, all parameters are used.

    This function returns a `Namespace` object with the following
    properties:

    - command (str): The sub-sub-command to perform (create|drop|validate).
    - environments ([str]): A list of one or more environments.
    - echo (bool): If `True`, sqlalchemy statements should be printed
      to `sys.stdout` on statement compilation.
    """
    parser: ArgumentParser = ArgumentParser(prog)
    include_: FrozenSet[str] = _normalize_include_argument(include)

    def add_argument(*args: str, **kwargs: Any) -> None:
        if (not include) or any(
            map(
                include_.__contains__,
                map(_normalize_included_parameter_name, args),
            )
        ):
            parser.add_argument(*args, **kwargs)

    if commands:
        add_argument("command", help=f"{'|'.join(commands)}")
    add_argument(
        "environment",
        type=str,
        default=None,
        help=f"{'|'.join(environments)}",
    )
    # Only applicable for SQLite
    add_argument(
        "path",
        type=str,
        nargs="?",
        default=os.path.join(gettempdir(), f"{prog.replace(' ', '-')}.sqlite"),
        help="The file path where this database will be created",
    )
    add_argument(
        "-u",
        "--user",
        type=str,
        default=None,
        help=(
            "\na username with which to authenticate the database connection"
        ),
    )
    add_argument(
        "-p",
        "--password",
        type=str,
        default=None,
        help=(
            "\na password with which to authenticate the database connection"
        ),
    )
    add_argument(
        "-d",
        "--database",
        type=str,
        default=None,
        help="\nthe name of a database with which to connect",
    )
    add_argument(
        "-c",
        "--catalog",
        type=str,
        default=None,
        help="\nthe name of a catalog with which to connect",
    )
    add_argument(
        "-w",
        "--warehouse",
        type=str,
        default=None,
        help="\nthe warehouse with which to execute queries",
    )
    add_argument(
        "-s",
        "--schema",
        type=str,
        default=None,
        help="\nthe name of a schema to use as the default schema",
    )
    add_argument(
        "-r",
        "--role",
        type=str,
        default=None,
        help="\nthe name of a role to be assumed",
    )
    add_argument(
        "-a",
        "--authenticator",
        type=str,
        default=None,
        help=(
            '\n"externalbrowser" or "https://org.okta.com"'
            'if no authenticator is specified, "externalbrowser" will '
            'be inferred for human users, and "https://org.okta.com" for '
            "applications"
        ),
    )
    add_argument(
        "-sn",
        "--stage-name",
        type=str,
        default=None,
        help=(
            "\nThe (schema-qualified) name of the stage from which S3 objects "
            "are loaded"
        ),
    )
    add_argument(
        "-sff",
        "--stage-file-format",
        type=str,
        default=None,
        help=(
            "\nThe file format name to use as the default for for the S3 stage"
        ),
    )
    add_argument(
        "-su",
        "--stage-url",
        type=str,
        default=None,
        help="\nThe base URL for staging of S3 objects",
    )
    add_argument(
        "-ssi",
        "--stage-storage-integration",
        type=str,
        default=None,
        help="\nThe name of the integration to use for staged S3 objects",
    )
    add_argument(
        "-cf",
        "--checkfirst",
        action="store_const",
        const=True,
        default=False,
        help=(
            "\nthis flag causes `create database`, `create schema`, "
            "`create view`, and `create table` statements to only be executed "
            "for databases/schemas/tables/views which do not yet exist"
        ),
    )
    add_argument(
        "-e",
        "--echo",
        action="store_const",
        const=True,
        default=False,
        help=(
            "\nthis flag causes all sqlalchemy statements to be printed "
            "to `sys.stdout` following compilation"
        ),
    )
    add_argument(
        "-vo",
        "--views-only",
        action="store_const",
        const=True,
        default=False,
        help=(
            "\nthis flag causes `create database`, `create schema`, and "
            "`create view` statements to be executed, but *not* "
            "`create table` statements"
        ),
    )
    add_argument(
        "-ucp",
        "--user-cerberus-path",
        type=str,
        default=None,
        help=(
            "\na Cerberus secure data path and key (in the format "
            '"secure/data/path/key") pointing to a username with '
            "which to authenticate this connection"
        ),
    )
    add_argument(
        "-pcp",
        "--password-cerberus-path",
        type=str,
        default=None,
        help=(
            "\na Cerberus secure data path and key (in the format "
            '"secure/data/path/key") pointing to a password with '
            "which to authenticate this connection"
        ),
    )
    add_argument(
        "-wcp",
        "--warehouse-cerberus-path",
        type=str,
        default=None,
        help=(
            "\na Cerberus secure data path and key (in the format "
            '"secure/data/path/key") pointing to the name of a warehouse '
            "with which to execute queries"
        ),
    )
    add_argument(
        "-scp",
        "--schema-cerberus-path",
        type=str,
        default=None,
        help=(
            "\na Cerberus secure data path and key (in the format "
            '"secure/data/path/key") pointing to a schema name'
        ),
    )
    add_argument(
        "-rcp",
        "--role-cerberus-path",
        type=str,
        default=None,
        help=(
            "\na Cerberus secure data path and key (in the format "
            '"secure/data/path/key") pointing to the name of a role to assume'
        ),
    )
    add_argument(
        "-dcp",
        "--database-cerberus-path",
        type=str,
        default=None,
        help=(
            "\na Cerberus secure data path and key (in the format "
            '"secure/data/path/key") pointing to the database name'
        ),
    )
    add_argument(
        "-ccp",
        "--catalog-cerberus-path",
        type=str,
        default=None,
        help=(
            "\na Cerberus secure data path and key (in the format "
            '"secure/data/path/key") pointing to the catalog name'
        ),
    )
    add_argument(
        "-acp",
        "--authenticator-cerberus-path",
        type=str,
        default=None,
        help=(
            "\na Cerberus secure data path and key (in the format "
            '"secure/data/path/key") pointing to the authenticator name'
        ),
    )
    add_argument(
        "-ud",
        "--undeclared",
        action="store_const",
        const=True,
        default=True,
        help=(
            "\nthis flag causes tables/views which are undeclared to be "
            'dropped (only applicable with the "drop" command)'
        ),
    )
    add_argument(
        "-udo",
        "--undeclared-only",
        action="store_const",
        const=True,
        default=False,
        help=(
            "\nthis flag causes *only* tables/views which are undeclared to "
            'be dropped (only applicable with the "drop" command)'
        ),
    )
    add_argument(
        "-dusr",
        "--dont-use-secondary-roles",
        action="store_const",
        const=True,
        default=False,
        help=("\nthis flag prevents use of secondary roles"),
    )
    add_argument(
        "--log",
        action="store",
        type=str,
        default=None,
        help="Log output path",
    )
    add_argument(
        "-ov",
        "--only-validate",
        default=[],
        type=str,
        action="append",
        help=(
            "If provided, only the specified view/table name(s) will be "
            "validated"
        ),
    )
    add_argument(
        "-ifk",
        "--ignore-foreign-key",
        default=[],
        type=str,
        action="append",
        help=(
            "The name of a foreign key to ignore for validation purposes only "
            '(only applicable for the "validation" command)'
        ),
    )
    add_argument(
        "-efcv",
        "--exclude-from-cache-validation",
        default=[],
        type=str,
        action="append",
        help=(
            "The name of one or more tables/views to exclude from "
            'query result cache validation, or "*" to exclude all'
        ),
    )

    # Databricks only
    add_argument(
        "--access-token",
        type=str,
        default=None,
        help=(
            "\nAn access token (Personal Access Token) or service principal "
            "credential with which to authenticate"
        ),
    )
    add_argument(
        "--access-token-cerberus-path",
        type=str,
        default=None,
        help=(
            "\nA cerberus secret path containing the access token with which "
            "to authenticate"
        ),
    )
    add_argument(
        "--http-path",
        type=str,
        default=None,
        help=(
            "\nAn HTTP path for a Databricks cluster to connect to in the "
            "format of /sql/protocolv1/o/<ORG_ID>/<CLUSTER_ID>"
        ),
    )
    # Hive Only
    add_argument(
        "--host",
        type=str,
        default=None,
        help="\nthe hostname of the database server",
    )
    add_argument(
        "-hcp",
        "--host-cerberus-path",
        type=str,
        default=None,
        help=(
            "\na Cerberus secure data path and key (in the format "
            '"secure/data/path/key") pointing to the hostname of the database '
            "server"
        ),
    )
    add_argument(
        "--port",
        type=int,
        default=None,
        help="\nthe port on which the database is being served",
    )
    add_argument(
        "--port-cerberus-path",
        type=int,
        default=None,
        help=(
            "\na Cerberus secure data path and key (in the format "
            '"secure/data/path/key") pointing to the port on which the '
            "database is served"
        ),
    )
    add_argument(
        "-l",
        "--location",
        type=str,
        default=None,
        help="The root S3 URL for hive external tables",
    )
    add_argument(
        "-sa",
        "--stored-as",
        type=str,
        default=None,
        help=(
            "A default value indicating what hive external tables are "
            '"STORED AS"'
        ),
    )
    add_argument(
        "-tp",
        "--tblproperties",
        type=str,
        default=None,
        help=(
            'A JSON dictionary representing default "TBLPROPERTIES" for '
            "hive external tables"
        ),
    )
    arguments: Namespace = parser.parse_args()
    if arguments.log:
        logging.basicConfig(filename=arguments.log, level=logging.INFO)
    if commands:
        assert arguments.command in commands
    if ("environment" in include) and environments and arguments.environment:
        assert arguments.environment in environments
    if ("role" in include) and roles and arguments.role:
        assert arguments.role in roles
    if (
        (not include) or ("tblproperties" in include)
    ) and arguments.tblproperties:
        # Parse TBLPROPERTIES as JSON, if provided
        arguments.tblproperties = json.loads(arguments.tblproperties)
        assert isinstance(arguments.tblproperties, dict)
    return arguments
