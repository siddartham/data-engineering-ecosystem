import os
from typing import Any, Dict, Iterable

from airflow import DAG  # type: ignore

from .config import DEFAULT_DAG_DIRECTORY


def iter_dag_ids(dag_source: str) -> Iterable[str]:
    """
    Given the source code for a DAG file, iterate over all DAG IDs.
    """
    namespace: Dict[str, Any] = {}
    exec(dag_source, namespace)
    for dag in filter(
        lambda value: isinstance(value, DAG), namespace.values()
    ):
        yield dag.dag_id


def iter_dags_ids(directory: str = DEFAULT_DAG_DIRECTORY) -> Iterable[str]:
    """
    Iterate over all DAG IDs.
    """
    file_name: str
    for file_name in os.listdir(directory):
        if file_name.endswith(".py"):
            path: str = os.path.join(directory, file_name)
            dag_id: str
            for dag_id in iter_dag_ids(open(path).read()):
                yield dag_id
