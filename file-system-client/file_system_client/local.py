import logging
import os
import shutil
from typing import IO, Iterable, List, Union
from urllib.parse import ParseResult, quote_plus, urlparse

from .base import FileSystem
from .utilities import FileSortKey

log: logging.Logger = logging.getLogger(__name__)


class Local(FileSystem):
    """
    This class serves as an abstraction for interacting with a local file
    system using this common interface.
    """

    def __init__(self, root: str) -> None:
        super().__init__(root=root)

    def get_url(self, path: str = "") -> str:
        """
        Get an absolute URL from an object key (`path`)
        """
        path = quote_plus(self.get_absolute_path(path), safe="/=")
        return f"file://{path}"

    def get_absolute_path(self, path: str = "") -> str:
        """
        Get a local file path from a URL.
        """
        path = path.replace("\\", "/")
        parse_result: ParseResult = urlparse(path)
        if parse_result.scheme:
            if parse_result.scheme.lower() != "file":
                raise ValueError(
                    f'"{parse_result.scheme}://" is not a supported protocol'
                )
            path = f"{parse_result.netloc}{parse_result.path}"
        if not path.startswith("/"):
            path = f"/{path}"
        return super().get_absolute_path(path)

    def iter_file_paths(
        self,
        directory: str = "",
        recursive: bool = True,
        sort_key: FileSortKey = FileSortKey.DEFAULT,
        sort_reverse: bool = False,
    ) -> Iterable[str]:
        """
        Yield all files in a directory
        """
        if sort_key != FileSortKey.DEFAULT or sort_reverse:
            raise NotImplementedError(
                "File path sorting has not yet been implemented "
                "for local file systems"
            )
        directory = self.get_absolute_path(directory)
        root: str
        directories: Iterable[str]
        files: Iterable[str]
        for root, directories, files in os.walk(directory):
            name: str
            for name in files:
                if name and name[0] != ".":
                    yield self.get_relative_path(
                        os.path.join(root, name).replace("\\", "/")
                    )
            if not recursive:
                break

    # For backwards compatibility
    get_file_paths = iter_file_paths

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
        os.makedirs(os.path.dirname(os.path.normpath(path)), exist_ok=True)
        # Write the file
        with open(path, "wb") as file_io:
            file_io.write(data)
        return path

    def get(self, path: str) -> IO[bytes]:
        """
        Retrieve a file object.

        Parameters:

        - key (str)
        """
        assert path and isinstance(path, str)
        path = self.get_absolute_path(path)
        return open(path, "rb")

    def iter_sub_directories(
        self, directory: str = "", recursive: bool = False
    ) -> Iterable[str]:
        path: str = self.get_absolute_path(directory)
        listed: List[str]
        try:
            listed = os.listdir(path)
        except FileNotFoundError:
            return
        directories: Iterable[str] = filter(
            lambda dir: os.path.isdir(os.path.join(path, dir)),
            listed,
        )
        sub_directory_name: str
        yield from map(
            lambda sub_directory_name: self.get_relative_path(
                "{}/".format(
                    os.path.join(os.path.normpath(path), sub_directory_name)
                    .replace("\\", "/")
                    .rstrip("/ ")
                )
            ),
            directories,
        )

    get_sub_directories = iter_sub_directories

    def delete(self, path: str) -> None:
        """
        Delete a file.

        Parameters:

        - path (str)
        """
        absolute_path: str = self.get_absolute_path(path)
        log.info(f"Deleting file: {absolute_path}")
        os.remove(absolute_path)

    def delete_directory(self, path: str) -> None:
        absolute_path: str = os.path.normpath(self.get_absolute_path(path))
        log.info(f"Deleting directory: {absolute_path}")
        if os.path.isdir(absolute_path):
            shutil.rmtree(absolute_path)

    def is_file(self, path: str) -> bool:
        """
        Return `True` if a *file* exists at the specified `path`.

        Parameters:

        - path (str): A path, relative to the file system root, at which to
          look for a file.
        """
        return os.path.isfile(os.path.normpath(self.get_absolute_path(path)))

    def is_directory(self, path: str) -> bool:
        """
        Return `True` if a directory exists at the specified `path`.

        Parameters:

        - path (str): A path, relative to the file system root, at which to
          look for a directory.
        """
        return os.path.isdir(os.path.normpath(self.get_absolute_path(path)))


def from_url(url: str) -> Local:
    parse_result: ParseResult = urlparse(url)
    assert parse_result.scheme.lower() == "file"
    path: str = f"{parse_result.netloc}{parse_result.path}"
    return Local(path)
