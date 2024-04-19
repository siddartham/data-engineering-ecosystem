from typing import Any, Callable, Dict, List, Union
from urllib import parse

import pyhive.presto  # type: ignore
from cerberus_assistant.get import get_secrets

__all__: List[str] = ["get_connection_string"]

# Modify the presto cursor to *not* verify SSL certificates
_cursor_init: Callable = pyhive.presto.Cursor.__init__


def _cursor_init_ssl_verify_false(*args: Any, **kwargs: Any) -> None:
    if "requests_kwargs" not in kwargs:
        kwargs["requests_kwargs"] = {}
    kwargs["requests_kwargs"]["verify"] = False
    _cursor_init(*args, **kwargs)


_cursor_init_ssl_verify_false.__name__ = _cursor_init.__name__
pyhive.presto.Cursor.__init__ = _cursor_init_ssl_verify_false


def get_connection_string(
    user: str = "",
    password: str = "",
    password_cerberus_path: str = "",
    host: str = "",
    region: str = "us-west-2",
    catalog: str = "ngap_hive",
    database: str = "default",
) -> str:
    """
    This function assembles and returns a connection string.

    Parameters:

    - user (str) = "": A username with which to connect to the hive server,
      if applicable.
    - password (str) = "": A password with which to connect to the hive server,
      if applicable.
    - host (str) = "": The IP or hostname of a server running
      `hiveserver2`, or "" if running hive locally.
    - database (str) = "default": The database name.
    """
    login: str = ""
    query_string: str = ""
    if password_cerberus_path and not password:
        cerberus_secrets: Union[str, Dict[str, str]] = get_secrets(
            password_cerberus_path
        )
        if isinstance(cerberus_secrets, str):
            if not user:
                user = password_cerberus_path.split("/")[-1]
            password = cerberus_secrets
        else:
            password = cerberus_secrets[user]
    if password:
        assert user
        login = f"{parse.quote(user)}:{parse.quote(password)}@"
        query_string = "?protocol=https"
    if not host:
        host = f"adapt-prd-presto-1.{region}.adapt.org.com:8443"
    connection_string: str = (
        f"presto://{login}{host}/{catalog}/{database}{query_string}"
    )
    return connection_string
