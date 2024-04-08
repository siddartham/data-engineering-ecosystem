"""
This module is only for backwards compatibility. Please reference `.spark`
instead.
"""

from typing import List

from .spark import (
    get_data_frame_with_unique_primary_keys,
    get_struct_type_from_mapping,
)

__all__: List[str] = [
    "get_struct_type_from_mapping",
    "get_data_frame_with_unique_primary_keys",
]
