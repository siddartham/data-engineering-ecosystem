import logging
import os
from typing import IO, Type, Union
from urllib.parse import ParseResult, quote_plus, urlparse

from .local import Local

log: logging.Logger = logging.getLogger(__name__)


def _makedirs(name: str) -> None:
    """
    A drop-in replacement for `os.makedirs`, with exception handling suitable
    for DBFS.
    """
    head: str
    tail: str
    head, tail = os.path.split(name)
    if not tail:
        head, tail = os.path.split(head)
    if head and tail and not os.path.exists(head):
        try:
            _makedirs(head)
        except FileExistsError:
            # Defeats race condition when another thread created the path
            pass
        if tail == os.curdir:
            return
    try:
        os.mkdir(name)
    except PermissionError:
        # If we get a permission error, the directory exists
        pass
    except Exception:
        if not os.path.isdir(name):
            raise


class DatabricksFileSystem(Local):
    """
    This class serves as an abstraction for interacting with the DBFS file
    system on Databricks.
    """

    def get_url(self, path: str) -> str:
        """
        Get an absolute URL from an object key (`path`)
        """
        path = quote_plus(self.get_absolute_path(path), safe="/=")
        return f"dbfs://{path}"

    def get_absolute_path(self, path: str = "") -> str:
        """
        Get a DBFS file path from a URL.
        """
        path = path.replace("\\", "/")
        parse_result: ParseResult = urlparse(path)
        if parse_result.scheme:
            if parse_result.scheme.lower() != "dbfs":
                raise ValueError(
                    f'"{parse_result.scheme}://" is not a supported protocol'
                )
            path = f"{parse_result.netloc}{parse_result.path}"
        if not path.startswith("/"):
            path = f"/{path}"
        return super().get_absolute_path(path)

    def put(self, file: Union[IO[bytes], bytes], path: str) -> str:
        """
        Save a file to the specified path (relative to `self.root`).

        Parameters:

        - file (typing.IO[bytes]|bytes): Either a file-like object from which
          the `.read()` method returns `bytes`, or an instance of `bytes`.
        - path (str): A path, relative to `self.root`, to which the file object
          will be saved.
        """
        data: bytes
        if isinstance(file, bytes):
            data = file
        else:
            file.seek(0)
            data = file.read()
        path = self.get_absolute_path(path)
        # Make the parent directory, if it doesn't already exist
        _makedirs(os.path.dirname(os.path.normpath(path)))
        # Write the file
        with open(path, "wb") as file_io:
            file_io.write(data)
        return path


# Alias
DBFS: Type[Local] = DatabricksFileSystem


def from_url(url: str) -> Local:
    parse_result: ParseResult = urlparse(url)
    assert parse_result.scheme.lower() == "dbfs"
    path: str = f"{parse_result.netloc}{parse_result.path}"
    return DatabricksFileSystem(path)
