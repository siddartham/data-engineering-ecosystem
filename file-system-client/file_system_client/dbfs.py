import logging
import os
from io import BytesIO
from typing import IO, Any, BinaryIO, Iterable, Tuple, Type, Union, cast
from urllib.parse import ParseResult, quote_plus, urlparse

from cerberus_assistant.decorate import apply_cerberus_path_arguments

from ._utilities import cached_property, get_class_url_keyword_arguments
from .local import Local
from .utilities import FileSortKey

log: logging.Logger = logging.getLogger(__name__)

DEFAULT_HOST: str = "community.cloud.databricks.com"


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

    Parameters/Properties:

    - root (str): The base path for all file operations

    Optional, Remote-Access Parameters/Properties:

    - host (str): The URL of the Databricks workspace
    - token (str): The Databricks access toke
    - token_cerberus_path (str): The Cerberus path to the Databricks access
      token, include key. For example: `app/secure-drop-box/team-name/key`.
    """

    __slots__: Tuple[str, ...] = Local.__slots__ + (
        "host",
        "token",
    )

    @apply_cerberus_path_arguments(
        token="token_cerberus_path",
    )
    def __init__(
        self,
        root: str = "",
        host: str = DEFAULT_HOST,
        token: str = "",
        token_cerberus_path: str = "",
    ) -> None:
        self.host = host
        self.token = token
        super().__init__(root=root)

    @property
    def _is_remote(self) -> bool:
        """
        Return `True` if connecting to a remote DBFS
        """
        return True if self.host and self.token else False

    def get_url(self, path: str = "") -> str:
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

    @cached_property
    def _workspace_client(self) -> Any:
        from databricks.sdk import WorkspaceClient

        return WorkspaceClient(host=self.host, token=self.token)

    def put(self, file: Union[IO[bytes], bytes], path: str) -> str:
        """
        Save a file to the specified path (relative to `self.root`).

        Parameters:

        - file (typing.IO[bytes]|bytes): Either a file-like object from which
          the `.read()` method returns `bytes`, or an instance of `bytes`.
        - path (str): A path, relative to `self.root`, to which the file object
          will be saved.
        """
        log.info(f"Attempting to put: {path}")
        path = self.get_absolute_path(path)
        if self._is_remote:
            from databricks.sdk import WorkspaceClient

            if isinstance(file, bytes):
                file = BytesIO(file)
                file.seek(0)
            else:
                try:
                    file.seek(0)
                except (AttributeError, NotImplementedError):
                    pass
            workspace_client: WorkspaceClient = self._workspace_client
            assert workspace_client.files
            workspace_client.files.upload(
                path,
                contents=cast(
                    BinaryIO,
                    file,
                ),
                overwrite=True,
            )
        else:
            data: bytes
            if isinstance(file, bytes):
                data = file
            else:
                try:
                    file.seek(0)
                except (AttributeError, NotImplementedError):
                    pass
                data = file.read()
            # Make the parent directory, if it doesn't already exist
            _makedirs(os.path.dirname(os.path.normpath(path)))
            # Write the file
            with open(path, "wb") as file_io:
                file_io.write(data)
        log.info(f"Put successful: {path}")
        return path

    def delete(self, path: str) -> None:
        """
        Delete a file.

        Parameters:

        - path (str)
        """
        log.info(f"Deleting {path}")
        if path.endswith("/"):
            raise ValueError(path)
        if self._is_remote:
            from databricks.sdk import WorkspaceClient

            workspace_client: WorkspaceClient = self._workspace_client
            assert workspace_client.files
            workspace_client.files.delete(self.get_absolute_path(path))
        else:
            super().delete(path)

    def delete_directory(self, path: str) -> None:
        if self._is_remote:
            from databricks.sdk import WorkspaceClient

            workspace_client: WorkspaceClient = self._workspace_client
            assert workspace_client.files
            self.clear(path)
            workspace_client.files.delete_directory(
                self.get_absolute_path(path)
            )
        else:
            super().delete_directory(path)

    def get(self, path: str) -> IO[bytes]:
        """
        Retrieve a file.

        Parameters:

        - path (str): The path of a file relative to the root directory.
        """
        if self._is_remote:
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.service.files import DownloadResponse

            workspace_client: WorkspaceClient = self._workspace_client
            assert workspace_client.files
            response: DownloadResponse = workspace_client.files.download(
                self.get_absolute_path(path)
            )
            return cast(BinaryIO, response.contents)
        else:
            return super().get(path)

    def _iter_remote_entries(
        self,
        absolute_directory: str,
        recursive: bool = True,
        include_directories: bool = True,
        include_files: bool = True,
    ) -> Iterable[Any]:
        from databricks.sdk import WorkspaceClient
        from databricks.sdk.errors.platform import NotFound
        from databricks.sdk.service.files import DirectoryEntry

        workspace_client: WorkspaceClient = self._workspace_client
        entry: DirectoryEntry
        directory_contents: Tuple[DirectoryEntry, ...]
        try:
            directory_contents = tuple(
                workspace_client.files.list_directory_contents(
                    absolute_directory
                )
            )
        except NotFound:
            # The path does not exist
            return
        for entry in directory_contents:
            if entry.is_directory:
                if include_directories:
                    yield entry
                if recursive:
                    assert entry.path
                    yield from self._iter_remote_entries(
                        entry.path,
                        recursive=recursive,
                        include_directories=include_directories,
                        include_files=include_files,
                    )
            elif include_files:
                yield entry

    def _iter_remote_paths(
        self,
        absolute_directory: str,
        recursive: bool = True,
        sort_key: FileSortKey = FileSortKey.DEFAULT,
        sort_reverse: bool = False,
        include_directories: bool = True,
        include_files: bool = True,
    ) -> Iterable[str]:
        """
        Iterate over file paths in a directory on a remote DBFS file system.

        Parameters:

        - absolute_directory (str): The absolute path of the directory
        - recursive (bool)
        - sort_key (file_system_client.base.FileSortKey) =
          file_system_client.base.FileSortKey.DEFAULT: This parameter
          indicates what property of the files to use for sorting returned
          file paths. By default, the file system default behavior will be
          used. The other sorting options available are:
          - MODIFIED: The date on which the file was most recently modified.
          - NAME: Alphabetical sorting.
        - sort_reverse (bool) = False: By default, sorting is in ascending
          order. If `sort_reverse is True`, sorting will be the opposite
          (descending) order.
        """
        from databricks.sdk.service.files import DirectoryEntry

        iter_remote_entries: Iterable[DirectoryEntry] = (
            self._iter_remote_entries(
                absolute_directory,
                recursive=recursive,
                include_directories=include_directories,
                include_files=include_files,
            )
        )
        if sort_key == FileSortKey.DEFAULT:
            if sort_reverse:
                iter_remote_entries = tuple(
                    reversed(tuple(iter_remote_entries))
                )
        else:
            iter_remote_entries = sorted(
                iter_remote_entries,
                key=lambda entry: (
                    cast(int, entry.last_modified or 0)
                    if sort_key == FileSortKey.MODIFIED
                    else (
                        cast(str, entry.path)
                        if sort_key == FileSortKey.NAME
                        else None
                    )
                ),
                reverse=sort_reverse,
            )
        yield from map(
            lambda entry: cast(str, entry.path), iter_remote_entries
        )

    def iter_file_paths(
        self,
        directory: str = "",
        recursive: bool = True,
        sort_key: FileSortKey = FileSortKey.DEFAULT,
        sort_reverse: bool = False,
    ) -> Iterable[str]:
        """
        Iterate over file paths in a directory.

        Parameters:

        - directory (str)
        - recursive (bool)
        - sort_key (file_system_client.base.FileSortKey) =
          file_system_client.base.FileSortKey.DEFAULT: This parameter
          indicates what property of the files to use for sorting returned
          file paths. By default, the file system default behavior will be
          used. The other sorting options available are:
          - MODIFIED: The date on which the file was most recently modified.
          - NAME: Alphabetical sorting.
        - sort_reverse (bool) = False: By default, sorting is in ascending
          order. If `sort_reverse is True`, sorting will be the opposite
          (descending) order.

        Returns: An iterable of all files in `directory`.
        """
        if self._is_remote:
            yield from map(
                self.get_relative_path,
                self._iter_remote_paths(
                    self.get_absolute_path(directory),
                    recursive=recursive,
                    sort_key=sort_key,
                    sort_reverse=sort_reverse,
                    include_files=True,
                    include_directories=False,
                ),
            )
        else:
            yield from super().iter_file_paths(
                directory,
                recursive=recursive,
                sort_key=sort_key,
                sort_reverse=sort_reverse,
            )

    # For backwards compatibility
    get_file_paths = iter_file_paths

    def iter_sub_directories(
        self,
        directory: str = "",
        recursive: bool = False,
    ) -> Iterable[str]:
        """
        Iterate over all sub-directories of a specified directory.

        Parameters:

        - directory (str)
        - recursive (bool) = True: If `False`, only *direct* descendants of the
          specified `directory` will be included. If `True`, *all*
          sub-directories, including sub-directories of each sub-directory,
          etc., will be included.
        """
        if self._is_remote:
            yield from map(
                self.get_relative_path,
                self._iter_remote_paths(
                    self.get_absolute_path(directory),
                    recursive=recursive,
                    include_files=False,
                    include_directories=True,
                ),
            )
        else:
            yield from super().iter_sub_directories(
                directory=directory,
                recursive=recursive,
            )

    get_sub_directories = iter_sub_directories

    def is_file(self, path: str) -> bool:
        """
        Return `True` if a *file* exists at the specified `path`.

        Parameters:

        - path (str): A path, relative to the file system root, at which to
          look for a file.
        """
        if self._is_remote:
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.errors.platform import NotFound

            workspace_client: WorkspaceClient = self._workspace_client
            try:
                # If metadata can be retrieved, the file exists
                workspace_client.files.get_metadata(
                    self.get_absolute_path(path)
                )
                return True
            except NotFound:
                return False
        else:
            return super().is_file(path)

    def is_directory(self, path: str) -> bool:
        """
        Return `True` if a directory exists at the specified `path`.

        Parameters:

        - path (str): A path, relative to the file system root, at which to
          look for a directory.
        """
        if self._is_remote:
            from databricks.sdk import WorkspaceClient
            from databricks.sdk.errors.platform import NotFound

            workspace_client: WorkspaceClient = self._workspace_client
            try:
                # If metadata can be retrieved, the file exists
                workspace_client.files.get_directory_metadata(
                    self.get_absolute_path(path)
                )
                return True
            except NotFound:
                return False
        else:
            return super().is_directory(path)


# Alias
DBFS: Type[Local] = DatabricksFileSystem


def from_url(url: str) -> Local:
    parse_result: ParseResult = urlparse(url)
    assert parse_result.scheme.lower() == "dbfs"
    path: str = f"{parse_result.netloc}{parse_result.path}"
    return DatabricksFileSystem(
        path,
        **get_class_url_keyword_arguments(
            cls=DatabricksFileSystem,
            url=url,
        ),
    )
