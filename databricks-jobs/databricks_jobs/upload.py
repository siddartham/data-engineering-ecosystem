import argparse
import re
from base64 import b64encode
from typing import Dict, Iterable, Tuple, Union

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.workspace import ImportFormat

from ._utilities import apply_defaults
from .client import get_workspace_client
from .config import DEFAULT_HOST, get_pyproject_arguments


@apply_defaults(**get_pyproject_arguments())
def upload(
    files: Union[Iterable[Tuple[str, str]], Dict[str, str]],
    host: str = DEFAULT_HOST,
    token: str = "",
    token_cerberus_path: str = "",
    overwrite: bool = True,
) -> None:
    """
    This function uploads files to your Databricks workspace.

    Parameters:

    - files ([(str, str)]|{str: str}): A mapping of local file paths to
      the workspace paths to which you wish to upload.
    - host (str): The databricks API host.
    - token (str): An authentication token.
    - token_cerberus_path (str): A Cerberus secure drop box path from
      which an authentication token can be retrieved.
    """
    if not isinstance(files, Dict):
        files = dict(files)
    client: WorkspaceClient = get_workspace_client(
        **({"host": host} if host else {}),
        **({"token": token} if token else {}),
        **(
            {"token_cerberus_path": token_cerberus_path}
            if token_cerberus_path
            else {}
        ),
    )
    local_file_path: str
    workspace_path: str
    for local_file_path, workspace_path in files.items():
        with open(local_file_path, "rb") as file_io:
            client.workspace.import_(
                path=workspace_path,
                content=b64encode(file_io.read()).decode("ascii"),
                format=ImportFormat.AUTO,
                overwrite=overwrite,
            )


class _HelpFormatter(argparse.HelpFormatter):

    def format_help(self) -> str:
        return re.sub(
            r"(\bFILE\b) (\1)",
            r"LOCAL_FILE_PATH WORKSPACE_PATH",
            super().format_help(),
        )


def main() -> None:
    """
    This function is the entry point for using this script as a CLI.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="databricks-jobs upload",
        description=(
            "This command uploads a file to your Databricks workspace."
        ),
        formatter_class=_HelpFormatter,
    )
    parser.add_argument(
        "--host",
        type=str,
        default="",
        help="The databricks API host.",
    )
    parser.add_argument(
        "-t",
        "--token",
        type=str,
        default="",
        help="An authentication token.",
    )
    parser.add_argument(
        "-tcp",
        "--token-cerberus-path",
        type=str,
        default="",
        help="An authentication token.",
    )
    parser.add_argument(
        "-f",
        "--file",
        default=[],
        type=str,
        nargs=2,
        action="append",
    )
    namespace: argparse.Namespace
    namespace = parser.parse_args()
    files: Tuple[str, ...] = tuple(namespace.file)
    upload(
        **({"files": files} if files else {}),
        **({"host": namespace.host} if namespace.host else {}),
        **({"token": namespace.token} if namespace.token else {}),
        **(
            {"token_cerberus_path": namespace.token_cerberus_path}
            if namespace.token_cerberus_path
            else {}
        ),
    )


if __name__ == "__main__":
    main()
