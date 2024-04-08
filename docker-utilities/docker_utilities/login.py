import argparse
import functools
from cerberus_assistant.decorate import apply_cerberus_path_arguments
from ._utilities import check_output
from .config import SERVER, DOCKER


@apply_cerberus_path_arguments(
    user="user_cerberus_path",
    password="password_cerberus_path",
    server="server_cerberus_path",
)
def login(
    *,
    user: str = "",
    password: str = "",
    server: str = SERVER,
    user_cerberus_path: str = "",
    password_cerberus_path: str = "",
    server_cerberus_path: str = "",
    echo: bool = True,
) -> None:
    """
    Login to a Docker server.

    Parameter:

    - user (str) = "": A GID username with which to authenticate.
    - password (str) = "": A GID password with which to authenticate.
    - server (str) = "": A server hostname or hostname:port.
    - user_cerberus_path (str) = "": A Cerberus secure data path (including /
      key) wherein a GID username with which to authenticate can be found.
    - password_cerberus_path (str) = "": A Cerberus secure data path (including
      /key) wherein a GID password with which to authenticate can be found.
    - server_cerberus_path (str) = "": A Cerberus secure data path (including
      /key) wherein the server URI (host|host:port) can be found.
    - echo (bool) = True: If `True`, show docker commands and output
    """
    _login(user=user, password=password, server=server, echo=echo)


@functools.lru_cache()
def _login(
    user: str = "",
    password: str = "",
    server: str = "",
    echo: bool = True,
) -> None:
    check_output(
        [
            DOCKER,
            "login",
            "--username",
            user,
            "--password",
            password,
            server,
        ],
        echo=echo,
    )


def main() -> None:
    """
    This function is the entry point for using this script as a CLI.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="docker-utilities login",
        description="Login to a Docker server",
    )
    parser.add_argument(
        "--user",
        "-u",
        type=str,
        default="",
    )
    parser.add_argument(
        "--password",
        "-p",
        type=str,
        default="",
    )
    parser.add_argument(
        "--server",
        "-s",
        type=str,
        default="",
    )
    parser.add_argument(
        "--user-cerberus-path",
        "-ucp",
        type=str,
        default="",
    )
    parser.add_argument(
        "--password-cerberus-path",
        "-pcp",
        type=str,
        default="",
    )
    parser.add_argument(
        "--server-cerberus-path",
        "-scp",
        type=str,
        default="",
    )
    namespace: argparse.Namespace = parser.parse_args()
    login(
        **dict(
            filter(
                all,
                (
                    ("user", namespace.user),
                    ("password", namespace.password),
                    ("server", namespace.server),
                    ("user_cerberus_path", namespace.user_cerberus_path),
                    (
                        "password_cerberus_path",
                        namespace.password_cerberus_path,
                    ),
                    ("server_cerberus_path", namespace.server_cerberus_path),
                ),
            )
        ),
    )


if __name__ == "__main__":
    main()
