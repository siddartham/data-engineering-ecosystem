import inspect
from datetime import datetime
from io import BytesIO
from operator import itemgetter
from typing import Any, Callable, Dict, Iterable, Optional, Set, Tuple
from urllib.parse import ParseResult, parse_qs, urlparse

cache: Any
try:
    from functools import cache  # type: ignore
except ImportError:
    from functools import lru_cache

    cache = lru_cache(maxsize=None)


def cached_property(function: Callable[..., Any]) -> Any:
    return property(cache(function))


class FileBytesIO(BytesIO):
    """
    This class adds file metadata to the BytesIO class
    """

    name: Optional[str]
    modified: Optional[datetime]
    created: Optional[datetime]

    def __init__(
        self,
        initial_bytes: bytes = b"",
        name: Optional[str] = None,
        modified: Optional[datetime] = None,
        created: Optional[datetime] = None,
    ) -> None:
        super().__init__(initial_bytes)
        self.name = name
        self.modified = modified
        self.created = created


def get_class_url_keyword_arguments(cls: type, url: str) -> Dict[str, Any]:
    """
    Assemble arguments from query string, if present
    """
    parameters: Iterable[Tuple[str, inspect.Parameter]] = inspect.signature(
        cls.__init__  # type: ignore
    ).parameters.items()
    parameter_names: Set[str] = set(
        map(
            itemgetter(0),
            filter(
                lambda item: item[1].kind
                not in (
                    inspect.Parameter.VAR_POSITIONAL,
                    inspect.Parameter.POSITIONAL_ONLY,
                ),
                tuple(parameters)[1:],
            ),
        )
    )
    parse_result: ParseResult = urlparse(url)
    kwargs: Dict[str, str] = {}
    if parse_result.query:
        for key, value in parse_qs(parse_result.query).items():
            key = key.lower().replace("-", "_")
            if key in parameter_names:
                kwargs[key.lower().replace("-", "_")] = value[0]
            else:
                raise ValueError(f"Unrecognized paramter: {key}")
    return kwargs
