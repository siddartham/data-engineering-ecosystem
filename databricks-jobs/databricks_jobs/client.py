from functools import lru_cache

from databricks.sdk import WorkspaceClient
from cerberus_assistant.decorate import apply_cerberus_path_arguments

from ._utilities import apply_defaults
from .config import DEFAULT_HOST, get_pyproject_arguments


@lru_cache()
@apply_defaults(**get_pyproject_arguments())
@apply_cerberus_path_arguments(
    token="token_cerberus_path",
)
def get_workspace_client(
    host: str = DEFAULT_HOST,
    token: str = "",
    token_cerberus_path: str = "",
) -> WorkspaceClient:
    """
    This function retrieves and caches a workspace client.
    """
    assert host and token
    return WorkspaceClient(host=host, token=token)
