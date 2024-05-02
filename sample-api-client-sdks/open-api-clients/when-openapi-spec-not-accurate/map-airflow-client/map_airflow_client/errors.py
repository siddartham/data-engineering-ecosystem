from typing import Any, Tuple, Union

from .experimental.model import DagRun as ExpirimentalDagRun
from .v1.model import DAGRun


class DAGRunError(Exception):
    args: Tuple[Any, ...]

    def __init__(
        self, dag_run: Union[DAGRun, ExpirimentalDagRun], *args: Any
    ) -> None:
        self.dag_run: Union[DAGRun, ExpirimentalDagRun] = dag_run
        super().__init__(self.message, *args)

    @property
    def message(self) -> str:
        return str(self.dag_run)
