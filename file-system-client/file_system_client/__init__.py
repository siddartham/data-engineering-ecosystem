from typing import Any, List, Optional

from . import base, dbfs, local

s3: Any
Config: Any
try:
    from botocore.config import Config  # type: ignore

    from . import s3
except ImportError:
    s3 = None
    Config = None
box: Any
try:
    from . import box
except ImportError:
    box = None

__all__: List[str] = [
    "base",
    "local",
    "dbfs",
    "s3",
    "box",
    "from_url",
]


def from_url(
    url: str,
    arn: str = "",
    profile_name: str = "",
    endpoint_url: str = "",
    config: Optional[Config] = None,
    region_name: str = "",
) -> base.FileSystem:
    """
    Get a file system object from a URL.

    Parameters:

    - url (str)

    S3 Parameters:

    - arn (str) = ""
    - profile_name (str) = ""
    - endpoint_url (str) = ""
    - config (botocore.config.Config|None) = None
    - region_name (str) = ""
    """
    if url.startswith("s3://"):
        if s3 is None:
            raise ValueError(
                "Use of the S3 file system requires installing "
                'file-system-client with the "s3" extra: '
                "`pip install file-system-client[s3]`"
            )
        return s3.from_url(url)
    elif url.startswith("dbfs://"):
        return dbfs.from_url(url)
    elif url.startswith("http://"):
        if box is None:
            raise ValueError(
                "Use of the Box file system requires installing "
                'file-system-client with the "box" extra: '
                "`pip install file-system-client[box]`"
            )
        return box.from_url(url)
    else:
        return local.from_url(url)
