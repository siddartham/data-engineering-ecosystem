from typing import Iterable, Tuple

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.jobs import BaseJob

from ._utilities import apply_defaults, as_tuple
from .client import get_workspace_client
from .config import DEFAULT_HOST, get_pyproject_arguments


@as_tuple
@apply_defaults(**get_pyproject_arguments())
def list_jobs(
    names: Tuple[str, ...] = (),
    host: str = DEFAULT_HOST,
    token: str = "",
    token_cerberus_path: str = "",
    expand_tasks: bool = True,
) -> Iterable[BaseJob]:
    """
    Yield all jobs in the workspace, and cache the results
    """
    client: WorkspaceClient = get_workspace_client(
        **({"host": host} if host else {}),
        **({"token": token} if token else {}),
        **(
            {"token_cerberus_path": token_cerberus_path}
            if token_cerberus_path
            else {}
        ),
    )
    if names:
        name: str
        for name in names:
            yield from client.jobs.list(name=name, expand_tasks=expand_tasks)
    else:
        yield from client.jobs.list(expand_tasks=expand_tasks)
