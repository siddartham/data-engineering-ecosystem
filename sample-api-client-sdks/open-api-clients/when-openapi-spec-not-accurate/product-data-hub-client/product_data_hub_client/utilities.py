import functools
from typing import (
    Any,
    Callable,
    Iterable,
    List,
    Mapping,
    Optional,
    Tuple,
    Union,
)
from urllib.parse import urlencode as _urlencode

import sob

__all__: List[str] = ["lru_cache", "urlencode"]

lru_cache: Callable[..., Any] = functools.lru_cache


def _format_query_item(
    item: Tuple[
        str,
        Union[
            None,
            int,
            float,
            str,
            bool,
            Iterable[int],
            Iterable[str],
            Iterable[bool],
        ],
    ]
) -> Tuple[str, Optional[str]]:
    """
    This function formats a query string key/value pair for GET requests
    """
    key: str
    value: Union[
        None,
        int,
        float,
        str,
        bool,
        Iterable[int],
        Iterable[str],
        Iterable[bool],
    ]
    key, value = item
    return (
        (
            "_dataunits"
            if key == "dataunits"
            else f"_{sob.utilities.camel(key[1:])}"
            if key.startswith("_")
            else sob.utilities.camel(key)
        ),
        (
            ",".join(map(str, value))
            if ((not isinstance(value, str)) and isinstance(value, Iterable))
            else None
            if (value is None)
            else str(value)
        ),
    )


def _bool_item_value_is_not_none(item: Tuple[str, Any]) -> bool:
    """
    Returns `True` if the value for a key/item pair is not `None`
    """
    return item[-1] is not None


def _item_key_is_q(item: Tuple[str, Any]) -> bool:
    return item[0] == "q"


def urlencode(
    items: Union[
        Mapping[
            str,
            Union[
                None,
                int,
                float,
                str,
                bool,
                Iterable[int],
                Iterable[str],
                Iterable[bool],
            ],
        ],
        Iterable[
            Tuple[
                str,
                Union[
                    None,
                    int,
                    float,
                    str,
                    bool,
                    Iterable[int],
                    Iterable[str],
                    Iterable[bool],
                ],
            ]
        ],
    ],
    safe: str = ",",
) -> str:
    """
    This function wraps `urllib.parse.urlencode`, however ensures the result
    is formatted appropriately for use with Nike's material management API.
    """
    if isinstance(items, Mapping):
        items = items.items()
    items = tuple(
        filter(
            _bool_item_value_is_not_none,
            map(_format_query_item, items),
        )
    )
    # If there is no "q" argument in the query string items, add one
    if not any(map(_item_key_is_q, items)):
        items += (("q", ""),)
    return _urlencode(items, safe=safe)
