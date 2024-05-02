from functools import lru_cache
from typing import Any, Dict

import tomli

DEFAULT_HOST: str = "community.cloud.databricks.com"


@lru_cache()
def get_pyproject_arguments() -> Dict[str, Any]:
    """
    Get arguments from pyproject.toml
    """
    with open("pyproject.toml", "rb") as pyproject_io:
        pyproject: Dict[str, Any] = tomli.load(pyproject_io)
    arguments: Dict[str, Any] = pyproject.get("tool", {}).get(
        "databricks-jobs", {}
    )
    # Replace hyphens with underscores
    key: str
    value: Any
    for key, value in tuple(arguments.items()):
        if isinstance(value, list):
            arguments[key] = tuple(value)
        if "-" in key:
            arguments[key.replace("-", "_")] = arguments.pop(key)
    if "host" not in arguments:
        arguments["host"] = DEFAULT_HOST
    if "token" in arguments:
        raise ValueError(
            "No `token` should not be in your pyproject.toml file."
            "Use `token_cerberus_path` instead."
        )
    return arguments
