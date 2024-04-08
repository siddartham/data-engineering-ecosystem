import argparse
from .config import DOCKER, SERVER
from cerberus_assistant.decorate import apply_cerberus_path_arguments
from ._utilities import check_output
from .login import login


@apply_cerberus_path_arguments(
    user="user_cerberus_path",
    password="password_cerberus_path",
    server="server_cerberus_path",
)
def exists(
    uri: str,
    user: str = "",
    password: str = "",
    server: str = SERVER,
    user_cerberus_path: str = "",
    password_cerberus_path: str = "",
    server_cerberus_path: str = "",
    echo: bool = True,
) -> bool:
    if user and password and server:
        login(user=user, password=password, server=server, echo=echo)
    try:
        check_output(
            [
                DOCKER,
                "manifest",
                "inspect",
                uri,
            ],
            echo=echo,
        )
        return True
    except Exception:
        try:
            check_output(
                [
                    DOCKER,
                    "pull",
                    uri,
                ],
                echo=echo,
            )
            return True
        except Exception:
            return False


def main() -> None:
    """
    This function is the entry point for using this script as a CLI.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="docker-utilities exists",
        description="Check to see if a Docker image exists on a remote server",
    )
    parser.add_argument(
        "uri",
        type=str,
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
    image_exists: bool = False
    namespace: argparse.Namespace = parser.parse_args()
    image_exists = exists(
        uri=namespace.uri,
        echo=False,
        **dict(
            filter(
                all,
                (
                    ("user", namespace.user),
                    ("password", namespace.password),
                    ("server", namespace.server),
                    (
                        "user_cerberus_path",
                        namespace.user_cerberus_path,
                    ),
                    (
                        "password_cerberus_path",
                        namespace.password_cerberus_path,
                    ),
                    (
                        "server_cerberus_path",
                        namespace.server_cerberus_path,
                    ),
                ),
            )
        ),
    )
    print("true" if image_exists else "false")


if __name__ == "__main__":
    main()
