import builtins
import copyreg
import functools
import logging
import os
import re
import sys
from collections import defaultdict
from copy import deepcopy
from getpass import getuser
from inspect import Parameter, Signature, signature
from itertools import chain
from keyword import iskeyword
from shutil import which
from subprocess import CalledProcessError, check_output, list2cmdline
from typing import (
    IO,
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    Union,
)
from unicodedata import normalize
from urllib import parse
from warnings import warn

import sqlalchemy.engine.url  # type: ignore
from more_itertools import unique_everseen
from sqlalchemy import Table  # type: ignore
from sqlalchemy.engine.base import Connection, Engine  # type: ignore
from sqlalchemy.engine.interfaces import Dialect  # type: ignore
from sqlalchemy.engine.mock import MockConnection  # type: ignore
from sqlalchemy.engine.reflection import Inspector  # type: ignore
from sqlalchemy.exc import NoSuchModuleError  # type: ignore
from sqlalchemy.inspection import inspect  # type: ignore
from sqlalchemy.sql.compiler import IdentifierPreparer  # type: ignore

__all__: List[str] = [
    "lru_cache",
    "patch_urllib_parse_uses",
    "get_class_table_name",
    "get_class_qualified_name",
    "SUPPORTED_DIALECTS",
    "get_bind_dialect_name",
    "apply_conditional_defaults",
    "apply_environment_defaults",
    "apply_role_defaults",
    "update_all_dialects_construct_arguments",
    "update_dialect_construct_arguments",
    "is_jenkins_bmx",
    "is_ci",
    "is_current_user_human",
    "translate_all_bind_schemas_to",
    "translate_all_engine_schemas_to",
    "get_dialect_table_option",
    "get_dialect_table_name",
    "get_dialect_table_schema",
    "get_dialect_qualified_table_name",
    "iter_recursive_subclasses",
    "is_declared_view",
    "is_view",
    "get_bind_view_names",
    "get_bind_table_names",
    "apply_region_defaults",
    "filter_false_keyword_arguments",
]

SUPPORTED_DIALECTS: Set[str] = {
    "snowflake",
    "sqlite",
    "postgresql",
    "default",
    "databricks",
}

lru_cache: Callable[..., Any] = functools.lru_cache


def _patch_sqlalchemy_engine_url() -> None:
    # The following fixes an issue with snowflake-sqlalchemy caused by their
    # use of a sqlalchemy private function
    def _rfc_1738_quote(text: str) -> str:
        return re.sub(
            r"[:@/]",
            lambda matched: f"%{ord(matched.group(0))}X",
            text,
        )

    sqlalchemy.engine.url._rfc_1738_quote = _rfc_1738_quote
    # The following makes instances of `sqlalchemy.engine.url.URL` pickleable
    url: sqlalchemy.engine.url.URL
    copyreg.pickle(
        sqlalchemy.engine.url.URL,
        lambda url: (
            sqlalchemy.engine.url.make_url,
            (url.render_as_string(hide_password=False),),
        ),
    )


_patch_sqlalchemy_engine_url()


def patch_urllib_parse_uses(protocol: str) -> None:
    """
    This function add a schema/protocol to `urllib.parse.uses_relative`,
    `urllib.parse.uses_netloc`, and `urllib.parse.uses_params` in order to
    allow `urllib.parse.urljoin` to be used with URLs having this protocol.
    """
    uses: List[str]
    for uses in (parse.uses_relative, parse.uses_netloc, parse.uses_params):
        if protocol not in uses:
            uses.append(protocol)


def get_class_table_name(class_name: str) -> str:
    """
    Converts a CamelCasedClassName to an UNDERSCORE_SEPARATED_TABLE_NAME.

    >>> print(get_class_table_name('theBirdsAndTheBees'))
    the_birds_and_the_bees

    >>> print(get_class_table_name('FYIThisIsAnAcronym'))
    fyi_this_is_an_acronym

    >>> print(get_class_table_name('in'))
    in_

    >>> print(get_class_table_name('id'))
    id_

    >>> print(get_class_table_name('one2one'))  # No change needed
    one2one

    >>> print(get_class_table_name('One2One'))
    one_2_one

    >>> print(get_class_table_name('@One2One'))
    one_2_one
    """
    name: str = class_name
    # Replace accented and otherwise modified latin characters with their
    # basic latin equivalent
    name = normalize("NFKD", name)
    # Replace any remaining non-latin characters with underscores
    name = re.sub(r"([^\x20-\x7F]|\s)+", "_", name)
    # Insert underscores between lowercase and uppercase characters
    name = re.sub(r"([a-z])([A-Z])", r"\1_\2", name)
    # Insert underscores between uppercase characters and following uppercase
    # characters which are followed by lowercase characters (indicating the
    # latter uppercase character was intended as part of a capitalized word
    name = re.sub(r"([A-Z])([A-Z])([a-z])", r"\1_\2\3", name)
    # Replace any series of one or more non-alphanumeric characters remaining
    # with a single underscore
    name = re.sub(r"[^\w_]+", "_", name).upper()
    # Only insert underscores between letters and numbers if camelCasing is
    # found in the original string
    if class_name != class_name.lower() and class_name != class_name.upper():
        name = re.sub(r"([0-9])([a-zA-Z])", r"\1_\2", name)
        name = re.sub(r"([a-zA-Z])([0-9])", r"\1_\2", name)
    # Replace any two or more adjacent underscores with a single underscore
    name = re.sub(r"__+", "_", name).lstrip("_")
    # Append an underscore to the keyword until it does not conflict with any
    # python keywords or built-ins
    while iskeyword(name) or (name in builtins.__dict__):
        name += "_"
    return name


def get_class_qualified_name(cls: type) -> str:
    """
    >>> from analytics_orm import declarative
    >>> print(get_class_qualified_name(declarative.Base))
    analytics_orm.declarative.Base
    """
    assert isinstance(cls, type)
    type_name: str
    type_name = ".".join(
        name_part
        for name_part in getattr(
            cls, "__qualname__", getattr(cls, "__name__")
        ).split(".")
        if name_part[0] != "<"
    )
    if cls.__module__ not in (
        "builtins",
        "__builtin__",
        "__main__",
        "__init__",
    ):
        type_name = f"{cls.__module__}.{type_name}"
    return type_name


@lru_cache()
def is_jenkins_bmx() -> bool:
    if "HUDSON_URL" in os.environ and (
        "jenkins.personal-cloud.com" in os.environ["HUDSON_URL"]
    ):
        return True
    return False


@lru_cache()
def is_ci() -> bool:
    if "CI" in os.environ and (os.environ["CI"].lower() == "true"):
        return True
    return is_jenkins_bmx()


# For backwards compatibility
is_bmx = is_ci


_GID_AD_GROUP: str = "Company.Special.Accounts"


def _ldapsearch_result_line_indicates_is_gid(line: str) -> bool:
    return (
        line.startswith("memberOf:")
        and (f"cn={_GID_AD_GROUP.lower()}" in line[9:].lstrip().lower())
        or line.startswith("employeeType:")
        and ("special" in line[13:].lstrip().lower())
    )


@lru_cache()
def is_current_user_human() -> bool:
    """
    This function checks to see if the current user is human, as opposed
    to a GID (service account).
    """
    # Windows or Mac users are always assumed to be human
    if sys.platform.startswith("darwin") or os.name == "nt":
        return True
    user: str
    try:
        user = getuser()
    except KeyError:
        try:
            user = run(("whoami",), echo=False)
        except CalledProcessError:
            # If no username can be found, this is a service running
            # without a mapped name
            return False
    try:
        # Check LDAP (Active Directory) to see if the user is a GID
        return not any(
            map(
                _ldapsearch_result_line_indicates_is_gid,
                run(
                    (
                        "ldapsearch",
                        "-H",
                        "ldap://ad.company.com",
                        "-b",
                        "DC=ad,DC=company,DC=com",
                        f"(&(objectClass=person)(sAMAccountName={user}))",
                        "memberOf",
                        "employeeType",
                    ),
                    echo=False,
                ).split("\n"),
            )
        )
    except (CalledProcessError, FileNotFoundError):
        # If `ldapsearch` can't be used, we will assume the user is not human
        return False


def run(command: Sequence[str], echo: bool = True, input: str = "") -> str:
    """
    This function runs a shell command, raises an error if a non-zero
    exit code is returned, and echo's both the command and output *if*
    the `echo` parameter is `True`.

    Parameters:

    - command (str|[str]): A shell command
    - echo (bool) = True: If `True`, the command and the output from the
      command will be printed to stdout
    """
    if command and not isinstance(command, str):
        path: Optional[str] = which(command[0])
        if path:
            command = (path,) + tuple(command[1:])
    if echo:
        command_str: str
        if isinstance(command, str):
            command_str = command
        else:
            command_str = list2cmdline(command)
        print(command_str)
    output: str = check_output(
        command,
        encoding="utf-8",
        universal_newlines=True,
        shell=isinstance(command, str),
        **dict(filter(all, (("input", input),))),  # type: ignore
    ).strip()
    if echo:
        print(output)
    return output


@lru_cache()
def add_log_stream_handler(
    log: Optional[logging.Logger] = None,
    stream: IO[str] = sys.stdout,
    level: int = logging.INFO,
) -> logging.Logger:
    """
    This function adds a handler for printing logs to an input/output
    stream such as `sys.stdout` or `sys.stderror`.

    Parameters:

    - log (logging.Logger) = logging.getLogger():
      The logger to add the stream handler to.
    - stream (typing.IO[str]) = sys.stdout:
      The output stream.
    - level (int) = logging.INFO:
      The lowest log level to capture.
    """
    if log is None:
        log = logging.getLogger()
    if log.level > level:
        log.setLevel(level)
    if not log.handlers:
        handler = logging.StreamHandler(stream)
        handler.setLevel(level)
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
        )
        log.addHandler(handler)
    return log


# For compatibility
add_stdout_log_handler = add_stderr_log_handler = add_log_stream_handler


def get_bind_dialect_name(
    bind: Union[Engine, Connection, str, sqlalchemy.engine.url.URL]
) -> str:
    """
    Given a connectable `bind` (connection or engine) object, return the name
    of the dialect used (for example: "sqlite", "snowflake",
    or "postgresql").
    """
    dialect_name: Union[str, bytes] = "default"
    if isinstance(bind, sqlalchemy.engine.url.URL):
        drivername: Union[str, bytes] = bind.drivername
        if not isinstance(drivername, str):
            drivername = str(drivername, encoding="utf-8")
        dialect_name = drivername.split("+")[0].lower()
    elif isinstance(bind, str):
        dialect_name = bind.split("://")[0].split("+")[0].lower()
    else:
        if isinstance(bind, (Engine, Connection)):
            dialect_name = bind.engine.dialect.name
            if not isinstance(dialect_name, str):
                dialect_name = str(dialect_name, encoding="utf-8")
    assert isinstance(dialect_name, str)
    assert dialect_name in SUPPORTED_DIALECTS
    return dialect_name


def _get_function_argument(
    function: Callable[..., Any],
    parameter_name: str,
    *args: Any,
    **kwargs: Any,
) -> Any:
    """
    This function accepts a function and parameter name, and returns
    the argument or keyword argument value for that parameter, as determined
    by the function signature, or raises a `KeyError` if not found
    """
    # If the parameter name is found in the keyword arguments, return
    # the keyword argument value
    try:
        return kwargs[parameter_name]
    except KeyError:
        if args:
            # If the parameter name was not found in the keyword arguments,
            # look for it in the positional arguments
            function_signature: Signature = signature(function)
            parameter: Parameter
            value: Any
            if args:
                for parameter, value in zip(
                    function_signature.parameters.values(), args
                ):
                    if (
                        parameter.kind == Parameter.POSITIONAL_OR_KEYWORD
                        and parameter.name == parameter_name
                    ):
                        return value
        raise


def apply_environment_defaults(
    environment: str, **defaults: Any
) -> Callable[..., Callable[..., Any]]:
    """
    This function decorates another function in order to apply a set of
    *default* keyword or positional/keyword argument values when the value for
    the `environment` argument is equal to that passed to the decorator.

    For example:

    ```python
    from analytics_orm.utilities import apply_environment_defaults
    from analytics_orm.postgresql import get_connection_url


    @apply_environment_defaults(
        "qa",
        user="qa-user",
        password="qa-password",
        host="qa-host",
        database="qa"
    )
    def get_environment_connection_string(
        environment: str,
        user: str = "",
        password: str = "",
        host: str = "",
        port: int = 0,
        database: str = "",
        schema: str = ""
    ) -> str:
        return str(get_connection_url(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database,
            schema=schema
        ))
    ```

    For the above example, `get_environment_connection_string("qa")` would
    return "postgresql://qa-user:qa-password@qa-host:5432/qa?schema=public".

    This decorator can be chained in order to apply defaults for multiple
    environments.
    """
    environment = environment.lower()

    def is_environment(
        function: Callable[..., Any], *args: Any, **kwargs: Any
    ) -> bool:
        try:
            return (
                _get_function_argument(
                    function, "environment", *args, **kwargs
                )
                == environment
            )
        except KeyError:
            return False

    return apply_conditional_defaults(is_environment, **defaults)


def apply_region_defaults(
    region: str, **defaults: Any
) -> Callable[..., Callable[..., Any]]:
    """
    This function decorates another function in order to apply a set of
    *default* keyword or positional/keyword argument values when the value for
    the `region` argument is equal to that passed to the decorator.

    For example:

    ```python
    from analytics_orm.utilities import apply_region_defaults
    from analytics_orm.postgresql import get_connection_url


    @apply_region_defaults(
        "uw2",
        user="uw2-user",
        password="uw2-password",
        host="uw2-host",
        database="uw2_database"
    )
    def get_region_connection_string(
        region: str,
        user: str = "",
        password: str = "",
        host: str = "",
        port: int = 0,
        database: str = "",
        schema: str = ""
    ) -> str:
        return str(get_connection_url(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database,
            schema=schema
        ))
    ```

    For the above example, `get_region_connection_string("qa")` would return
    "postgresql://uw2-user:uw2-password@uw2-host:5432/dev?schema=public".

    This decorator can be chained in order to apply defaults for multiple
    regions.
    """
    region = region.lower()

    def is_region(
        function: Callable[..., Any], *args: Any, **kwargs: Any
    ) -> bool:
        try:
            return (
                _get_function_argument(function, "region", *args, **kwargs)
                == region
            )
        except KeyError:
            return False

    return apply_conditional_defaults(is_region, **defaults)


def apply_role_defaults(
    role: str, **defaults: Any
) -> Callable[..., Callable[..., Any]]:
    """
    This function decorates another function in order to apply a set of
    *default* keyword or positional/keyword argument values when the value for
    the `role` argument is equal to that passed to the decorator.

    For example:

    ```python
    from analytics_orm.utilities import apply_role_defaults
    from analytics_orm.postgresql import get_connection_url


    @apply_role_defaults(
        "default-role",
        user="qa-user",
        password="qa-password",
        host="qa-host",
        database="qa"
    )
    def get_role_connection_string(
        role: str = "",
        user: str = "",
        password: str = "",
        host: str = "",
        port: int = 0,
        database: str = "",
        schema: str = ""
    ) -> str:
        return str(get_connection_url(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database,
            schema=schema
        ))
    ```

    For the above example, `get_role_connection_string("qa-user")`
    would return
    "postgresql://qa-user:qa-password@qa-host:5432/qa?schema=public".

    This decorator can be chained in order to apply defaults for multiple
    users, environments, or other conditions.
    """

    def is_role(
        function: Callable[..., Any], *args: Any, **kwargs: Any
    ) -> bool:
        try:
            return (
                _get_function_argument(function, "role", *args, **kwargs)
                == role
            )
        except KeyError:
            try:
                # Attempt to infer a role from the connection/engine
                bind: Union[Engine, Connection] = _get_function_argument(
                    function, "bind", *args, **kwargs
                )
                if bind and not isinstance(bind, MockConnection):
                    url: sqlalchemy.engine.url.URL = bind.engine.url
                    bind_role: str = url.query.get("role", None)
                    return bind_role == role
                return False
            except KeyError:
                return False

    return apply_conditional_defaults(is_role, **defaults)


def _exclude_none_value_items(item: Tuple[str, Any]) -> bool:
    return bool(item[1] is not None)


def apply_conditional_defaults(
    condition: Callable[..., bool], **defaults: Any
) -> Callable[..., Callable[..., Any]]:
    """
    This function decorates another function in order to apply a set of
    *default* keyword or positional/keyword argument values based on the
    return of a `condition` function, which should accept the same parameters
    as the wrapped function.

    For example:

    ```python
    from typing import Any
    from analytics_orm.utilities import apply_conditional_defaults
    from analytics_orm.postgresql import get_connection_url


    def is_qa(
        environment: str, *args: Any, **kwargs: Any
    ) -> bool:
        return environment.lower() == "qa"


    @apply_conditional_defaults(
        is_qa,
        user="qa-user",
        password="qa-password",
        host="qa-host",
        database="qa"
    )
    def get_environment_connection_string(
        environment: str,
        user: str = "",
        password: str = "",
        host: str = "",
        port: int = 0,
        database: str = "",
        schema: str = ""
    ) -> str:
        return str(get_connection_url(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database,
            schema=schema
        ))
    ```

    For the above example, `get_environment_connection_string("qa")` would
    return "postgresql://qa-user:qa-password@qa-host:5432/qa?schema=public".

    This decorator can be chained in order to apply defaults for more than one
    condition.
    """

    def decorating_function(
        function: Callable[..., Any]
    ) -> Callable[..., Any]:
        function_signature: Signature = signature(function)

        @functools.wraps(function)
        def wrapper(*args: str, **kwargs: Any) -> Any:
            """
            This function wraps the original and applies defaults for
            any parameters for which an argument is not passed
            """
            key: str
            value: Any
            # Pass the arguments and keyword arguments provided to the
            # condition function to determine if we should apply these
            # defaults
            if condition(function, *args, **kwargs):
                defaults_or_kwargs: Dict[str, Any] = deepcopy(defaults)
                # First we get any arguments which are passed to parameters
                # which can be either positional *or* keyword arguments,
                # and were passed as positional arguments
                parameter: Parameter
                if args:
                    for parameter, value in zip(
                        function_signature.parameters.values(), args
                    ):
                        assert (
                            parameter.kind == Parameter.POSITIONAL_OR_KEYWORD
                        )
                        if (value is not None) or (
                            parameter.name not in defaults_or_kwargs
                        ):
                            defaults_or_kwargs[parameter.name] = value
                defaults_or_kwargs.update(
                    **{
                        key: value
                        for key, value in filter(  # type: ignore
                            _exclude_none_value_items, kwargs.items()
                        )
                    }
                )
                # Remove arguments which do not correspond to
                # any of the function's parameter names

                def get_parameter_name(parameter_: Parameter) -> str:
                    return parameter_.name

                for key in set(defaults_or_kwargs.keys()) - set(
                    map(
                        get_parameter_name,
                        function_signature.parameters.values(),
                    )
                ):
                    del defaults_or_kwargs[key]
                # Execute the wrapped function
                return function(**defaults_or_kwargs)
            else:
                return function(*args, **kwargs)

        return wrapper

    return decorating_function


def filter_false_keyword_arguments(
    function: Callable[..., Any],
) -> Any:
    """
    This is a decorator causing keyword parameters having values which, when
    cast as a boolean value, evaluate to `False`, to not be included in
    function parameters when the call stack is inspected.
    """

    @functools.wraps(function)
    def wrapper(*args: str, **kwargs: Any) -> Any:
        """
        This function wraps the original
        """
        return function(*args, **dict(filter(all, kwargs.items())))

    return wrapper


def update_all_dialects_construct_arguments(
    construct: type, **kwargs: Any
) -> None:
    """
    Update the `.construct_arguments` property for all supported dialects.
    """
    dialect_name: str
    for dialect_name in SUPPORTED_DIALECTS:
        try:
            update_dialect_construct_arguments(
                dialect_name, construct, **kwargs
            )
        except NoSuchModuleError:
            pass


@lru_cache()
def update_dialect_construct_arguments(
    dialect_name: str, construct: type, **kwargs: Any
) -> None:
    """
    This function updates construct arguments for the specified `dialect`,
    or raises a `sqlalchemy.exc.NoSuchModuleError`.
    """
    dialect_class: Type[Dialect] = get_dialect(dialect_name)
    if dialect_class.construct_arguments is None:
        dialect_class.construct_arguments = []
    arguments: Optional[Dict[str, Any]] = None
    key: type
    value: Dict[str, Any]
    for key, value in dialect_class.construct_arguments:
        if key is construct:
            arguments = value
            break
    if arguments is None:
        arguments = {}
        dialect_class.construct_arguments.append((construct, arguments))
    arguments.update(**kwargs)


class _OmniscientDefaultDict(defaultdict):
    """
    This is a default dictionary which purports to be all encompassing
    """

    def __contains__(self, item: object) -> bool:
        return True


def get_bind_schema(bind: Union[Connection, Engine]) -> Optional[str]:
    """
    Returns the schema name from an engine or connection
    """
    url: sqlalchemy.engine.url.URL = (
        bind.engine.url if isinstance(bind, Connection) else bind.url
    )
    dialect_name: str = get_bind_dialect_name(bind)
    if dialect_name == "snowflake":
        # Snowflake appends the schema to the database name
        return (url.database or "").partition("/")[2] or None
    elif dialect_name == "sqlite":
        return None
    return url.query.get("schema", None)


def get_bind_database(bind: Union[Connection, Engine]) -> Optional[str]:
    """
    Returns the database name for an engine or connection
    """
    url: sqlalchemy.engine.url.URL = (
        bind.engine.url if isinstance(bind, Connection) else bind.url
    )
    if get_bind_dialect_name(bind) == "snowflake":
        # Snowflake appends the schema to the database name
        return (url.database or "").partition("/")[0] or None
    return url.database


def translate_all_bind_schemas_to(
    bind: Union[Engine, Connection], schema: Optional[str] = None
) -> Union[Engine, Connection]:
    """
    This function causes all schemas to be translated as the value
    provided for `schema`, for a given engine or connection, and
    returns the same connection or engine.

    Parameters:

    - **engine** (sqlalchemy.engine.interfaces.Connectable)
    - **schema** (str)
    """
    # This causes all schema names to be translated as `None`
    bind.execution_options(
        schema_translate_map=_OmniscientDefaultDict(lambda: schema)
    )
    return bind


def translate_all_engine_schemas_to(
    engine: Engine, schema: Optional[str] = None
) -> Engine:
    """
    This function causes all schemas to be translated as the value
    provided for `schema`, for a given engine, and  returns the same
    engine.

    Parameters:

    - **engine** (sqlalchemy.engine.Engine)
    - **schema** (str)
    """
    bind: Union[Engine, Connection] = translate_all_bind_schemas_to(
        engine, schema
    )
    assert isinstance(bind, Engine)
    return bind


def get_dialect_table_option(
    dialect: Union[str, bytes, Dialect, Type[Dialect]],
    table: Table,
    key: str,
    default: Union[str, Dict[str, str], None] = None,
) -> Union[str, Dict[str, str], None]:
    return table.dialect_options.get(get_dialect_name(dialect), {}).get(
        key, default
    )


def get_dialect_name(
    dialect: Union[str, bytes, Dialect, Type[Dialect]]
) -> str:
    if isinstance(dialect, bytes):
        dialect = str(dialect, encoding="utf-8")
    elif not isinstance(dialect, str):
        assert isinstance(dialect, Dialect) or (
            isinstance(dialect, type) and issubclass(dialect, Dialect)
        )
        dialect = dialect.name  # type: ignore
        if isinstance(dialect, bytes):
            dialect = str(dialect, encoding="utf-8")
    if dialect and ("+" in dialect):
        dialect = dialect.split("+")[0]
    return dialect


def get_dialect(dialect_name: str) -> Type[Dialect]:
    """
    >>> print(get_dialect("sqlite").name)
    sqlite
    """
    return sqlalchemy.engine.url.URL.create(
        drivername=dialect_name
    ).get_dialect()


@lru_cache()
def get_dialect_identifier_preparer(
    dialect: Union[str, bytes, Dialect, Type[Dialect]]
) -> IdentifierPreparer:
    """
    Get a dialect's identifier preparer.

    >>> preparer = get_dialect_identifier_preparer("sqlite")
    preparer.quote()
    """
    dialect_class: Type[Dialect]
    if isinstance(dialect, bytes):
        dialect = str(dialect, encoding="utf-8")
    if isinstance(dialect, str):
        dialect = get_dialect(dialect)
    if isinstance(dialect, type):
        assert issubclass(dialect, Dialect)
        dialect_class = dialect
        dialect = dialect_class()
    else:
        dialect_class = type(dialect)
    preparer_class: Type[IdentifierPreparer] = IdentifierPreparer
    if hasattr(dialect, "preparer"):
        preparer_class = dialect.preparer
    return preparer_class(dialect=dialect)


def _default_quote(ident: str) -> str:
    return ident


def get_dialect_table_name(
    dialect: Union[str, bytes, Dialect, Type[Dialect]],
    table: Table,
    quote: Callable[[str], str] = _default_quote,
) -> str:
    """
    Get a (potentially dialect-specific) table name.
    """
    table_name: Union[str, Dict[str, str], None] = get_dialect_table_option(
        dialect, table, "table_name", table.name or ""
    )
    assert isinstance(table_name, str)
    return quote(table_name) if table_name else table_name


def get_dialect_table_schema(
    dialect: Union[str, bytes, Dialect, Type[Dialect]],
    table: Table,
    quote: Callable[[str], str] = _default_quote,
) -> str:
    """
    Get a (potentially dialect-specific) schema name.
    """
    schema_name: Union[str, Dict[str, str], None] = get_dialect_table_option(
        dialect, table, "schema_name", table.schema or ""
    )
    assert isinstance(schema_name, str)
    return quote(schema_name) if schema_name else schema_name


def get_dialect_qualified_table_name(
    dialect: Union[str, bytes, Dialect, Type[Dialect]],
    table: Table,
    quote: Callable[[str], str] = _default_quote,
) -> str:
    """
    Get a fully qualified table name, including the schema if needed for
    the specified dialect.
    """
    table_name: str = get_dialect_table_name(dialect, table, quote=quote)
    schema_name: str = get_dialect_table_schema(dialect, table, quote=quote)
    return f"{schema_name}.{table_name}" if schema_name else table_name


def is_declared_view(table: Table) -> bool:
    return table.info and table.info.get("is_view", False)


def get_bind_view_names(
    bind: Union[Engine, Connection],
    schema: Optional[str] = None,
) -> Set[str]:
    inspector: Inspector = inspect(bind)
    return set(map(str, inspector.get_view_names(schema=schema)))


def get_bind_table_names(
    bind: Union[Engine, Connection],
    schema: Optional[str] = None,
) -> Set[str]:
    inspector: Inspector = inspect(bind)
    return set(map(str, inspector.get_table_names(schema=schema)))


def is_view(
    table: Table, bind: Union[Engine, Connection, None] = None
) -> bool:
    """
    Determine if the provided table is actually a view
    """
    bind = bind or table.bind or table.metadata.bind
    if bind:
        return str(table.name) in get_bind_view_names(
            bind, schema=table.schema
        )
    else:
        if is_declared_view(table):
            print(f"Inferring {table.name} is a view from its ORM declaration")
            return True
        warn(
            "No bind could be inferred from the metadata for "
            f"{table.name}, so we will assume this is a table "
            "(as opposed to a view)"
        )
        return False


def iter_recursive_subclasses(cls: type) -> Iterable[type]:
    """
    Iterate over all subclasses of a type, recursively

    >>> class A:
    ...     pass
    ... class B(A):
    ...     pass
    ... class C(A):
    ...     pass
    ... print(
    ...     ",".join(
    ...         map(lambda cls: cls.__name__, iter_recursive_subclasses(A)
    ...     )
    ... )
    B,C
    """
    sub_classes: List[type] = cls.__subclasses__()
    yield from unique_everseen(
        chain(sub_classes, *map(iter_recursive_subclasses, sub_classes))
        if sub_classes
        else sub_classes
    )
