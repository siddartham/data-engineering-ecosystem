import logging
from datetime import datetime
from io import BytesIO
from operator import itemgetter
from typing import IO, Iterable, Tuple, Union, cast
from urllib.parse import ParseResult, urlparse

import boxsdk
import boxsdk.pagination
import boxsdk.pagination.limit_offset_based_object_collection
from cerberus_assistant.decorate import apply_cerberus_path_arguments

from file_system_client.errors import append_exception_text

from ._utilities import (
    FileBytesIO,
    cached_property,
    get_class_url_keyword_arguments,
)
from .base import FileSystem
from .utilities import FileSortKey

log: logging.Logger = logging.getLogger(__name__)


class Box(FileSystem):
    """
    Parameters/Properties:

    - root (str): The URL or ID of the Box folder that will be used as the root
    - client_id (str): Your Box app OAuth client ID
    - client_secret (str): Your Box app OAuth client secret
    - public_key_id (str): Your Box app public key ID
    - private_key (str): Your Box app private key
    - passphrase (str): Your Box app private key passphrase
    - enterprise_id (str): Your Box app enterprise ID
    """

    __slots__: Tuple[str, ...] = (
        "_root",
        "client_id",
        "client_secret",
        "public_key_id",
        "private_key",
        "passphrase",
        "enterprise_id",
        "_root_folder_id",
        "_root_url",
    )

    @apply_cerberus_path_arguments(
        {
            "client_id": "client_id_cerberus_path",
            "client_secret": "client_secret_cerberus_path",
            "public_key_id": "public_key_id_cerberus_path",
            "private_key": "private_key_cerberus_path",
            "passphrase": "passphrase_cerberus_path",
            "enterprise_id": "enterprise_id_cerberus_path",
        }
    )
    def __init__(
        self,
        root: str = "",
        client_id: str = "",
        client_secret: str = "",
        public_key_id: str = "",
        private_key: str = "",
        passphrase: str = "",
        enterprise_id: str = "",
        client_id_cerberus_path: str = "",
        client_secret_cerberus_path: str = "",
        public_key_id_cerberus_path: str = "",
        private_key_cerberus_path: str = "",
        passphrase_cerberus_path: str = "",
        enterprise_id_cerberus_path: str = "",
    ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.public_key_id = public_key_id
        self.private_key = private_key
        self.passphrase = passphrase
        self.enterprise_id = enterprise_id
        self._root_folder_id: str = ""
        self._root_url: str = ""
        super().__init__(root=root)

    @cached_property
    def _root_folder(self) -> boxsdk.object.folder.Folder:
        """
        The root folder can be cached because it will not (should not) be
        deleted or moved during by any client operation.
        """
        item: boxsdk.object.item.Item
        if self._root_folder_id:
            return self._client.folder(self._root_folder_id)
        elif self._root_url:
            item = self._client.get_shared_item(self._root_url)
            assert isinstance(item, boxsdk.object.folder.Folder), (
                "The root URL must be for a folder, not a file: "
                f"{self._root_url}"
            )
            return item
        elif self._root:
            item = self._get_folder_path_item(
                self._client.root_folder(), self._root, create_folder=True
            )
            assert isinstance(item, boxsdk.object.folder.Folder), (
                "The root path must be to a folder, not a file: "
                f"{self._root}"
            )
            self._root_folder_id = item.object_id
            return item
        else:
            item = self._client.root_folder()
            self._root_folder_id = item.object_id
            return cast(boxsdk.object.folder.Folder, item)

    def _get_folder_path_item(
        self,
        folder: boxsdk.object.folder.Folder,
        path: str,
        create_folder: bool = False,
    ) -> boxsdk.object.item.Item:
        """
        Get an item at a specified path relative to a folder
        """
        path = path.strip("/")
        if not path:
            # The folder itself is being requested
            return folder
        name: str
        name, path = path.partition("/")[::2]
        if path:
            # There is more traversal to do, so we only need folder
            sub_folder: boxsdk.object.folder.Folder
            for sub_folder in cast(
                Iterable[boxsdk.object.folder.Folder],
                map(
                    itemgetter(1),
                    self._iter_folder_items(
                        "",
                        folder,
                        recursive=False,
                        include_files=False,
                        include_folders=True,
                    ),
                ),
            ):
                if sub_folder["name"] == name:
                    return self._get_folder_path_item(
                        sub_folder, path, create_folder=create_folder
                    )
        else:
            item: boxsdk.object.item.Item
            # This is the final part of the path, so we will return the item
            for item in map(
                itemgetter(1),
                self._iter_folder_items("", folder, recursive=False),
            ):
                if item["name"] == name:
                    return item
        if create_folder:
            return folder.create_subfolder(name)
        raise FileNotFoundError(
            f'No item named "{name}" was found under folder ID: '
            f"{folder.object_id}"
        )

    @property
    def root(self) -> str:
        return self._root

    @root.setter
    def root(self, root: str) -> None:
        """
        Set the root folder using a path relative to the user's home,
        """
        if root:
            parse_result: ParseResult = urlparse(root)
            if parse_result.scheme:
                # This is a directory share URL
                self._root_url = root
                self._root = ""
                item: boxsdk.object.item.Item = self._client.get_shared_item(
                    self._root_url
                )
                assert isinstance(item, boxsdk.object.folder.Folder), (
                    "The root URL must point to a folder, not a file: "
                    f"{self._root_url}"
                )
                self._root_folder_id = item.object_id
            else:
                # This is relative to the user's root directory
                # Note: There is no root URL to set, it remains ""
                self._root = root.lstrip("/")
                # The root folder ID will be set when root folder is first
                # accessed
                self._root_folder_id = ""
                self._root_url = ""
        else:
            # Use the user's root directory
            self._root_folder_id = "0"
            self._root_url = ""
            self._root = ""

    @cached_property
    def _client(self) -> boxsdk.Client:
        """
        This property exposes the underlying Box SDK client object
        """
        return boxsdk.Client(
            boxsdk.JWTAuth(
                client_id=self.client_id,
                client_secret=self.client_secret,
                enterprise_id=self.enterprise_id,
                jwt_key_id=self.public_key_id,
                rsa_private_key_data=self.private_key.encode("ascii"),
                rsa_private_key_passphrase=self.passphrase,
            )
        )

    def put(self, file: Union[IO[bytes], bytes], path: str) -> str:
        """
        Save a file to the specified path (relative to `self.root`).

        Parameters:

        - file (typing.IO[bytes]|bytes): Either a file-like object from which
          the `.read()` method returns `bytes`, or an instance of `bytes`.
        - path (str): A path, relative to `self.root`, to which the file object
          will be saved.
        """
        directory: str
        name: str
        directory, name = path.rpartition("/")[::2]
        # Get (and create if needed) the parent folder
        folder: boxsdk.object.item.Item = self._get_item(
            directory, create_folder=True
        )
        assert isinstance(folder, boxsdk.object.folder.Folder)
        if isinstance(file, bytes):
            file = BytesIO(file)
            file.seek(0)
        else:
            try:
                file.seek(0)
            except (AttributeError, NotImplementedError):
                pass
        folder.upload_stream(file_stream=file, file_name=name)
        return path

    def delete(self, path: str) -> None:
        """
        Delete a file.

        Parameters:

        - path (str)
        """
        try:
            item: boxsdk.object.item.Item = self._get_item(path)
        except FileNotFoundError as error:
            append_exception_text(error, f'\n"{path}" does not exist')
            raise error
        if not isinstance(item, boxsdk.object.file.File):
            raise FileNotFoundError(f'"{path}" is not a file')
        item.delete()

    def delete_directory(self, path: str) -> None:
        """
        Delete a directory.

        Parameters:

        - path (str)
        """
        item: boxsdk.object.item.Item = self._get_item(path)
        if not isinstance(item, boxsdk.object.folder.Folder):
            raise FileNotFoundError(f'"{path}" is not a directory/folder')
        # Deleting the root directory would cause problems, so we disallow this
        if item.object_id == self._root_folder.object_id:
            raise PermissionError(
                "You are not permitted to delete the root directory"
            )
        item.delete()

    def _get_item(
        self, path: str, create_folder: bool = False
    ) -> boxsdk.object.item.Item:
        """
        Retrieve an item.

        Parameters:

        - path (str): The path of a file relative to the root directory,
          or a URL.
        """
        parse_result: ParseResult = urlparse(path)
        if parse_result.scheme:
            # This is a URL
            return self._client.get_shared_item(path)
        else:
            # This is a path
            return self._get_folder_path_item(
                self._root_folder, path=path, create_folder=create_folder
            )

    def get(self, path: str) -> IO[bytes]:
        """
        Retrieve a file.

        Parameters:

        - path (str): The path of a file relative to the root directory,
          or the URL of a shared file.
        """
        item: boxsdk.object.item.Item = self._get_item(path)
        file_io: IO[bytes] = FileBytesIO(
            name=item["name"],
            modified=datetime.fromisoformat(item["modified_at"]),
        )
        assert isinstance(
            item, boxsdk.object.file.File
        ), f'"{path}" is not a file'
        file_io.write(item.content())
        file_io.seek(0)
        return file_io

    def get_url(self, path: str = "") -> str:
        """
        Get an absolute URL from a relative path.

        Parameters:

        - path (str): A file path relative to `self.root`.

        Returns a shareable URL.
        """
        return self._get_item(path).get_shared_link()

    def _iter_folder_items(
        self,
        path: str,
        folder: boxsdk.object.folder.Folder,
        recursive: bool = True,
        sort_key: FileSortKey = FileSortKey.DEFAULT,
        sort_reverse: bool = False,
        include_files: bool = True,
        include_folders: bool = True,
    ) -> Iterable[Tuple[str, boxsdk.object.item.Item]]:
        """
        Iterate over all files and/or folder in a folder.

        Parameters:

        - folder (boxsdk.object.folder.Folder)
        - recursive (bool)
        - sort_key (file_system_client.base.FileSortKey)
          = file_system_client.base.FileSortKey.DEFAULT
        - sort_reverse (bool) = False
        - include_files (bool) = True
        - include_folders (bool) = True
        """
        assert (not path) or path.endswith(
            "/"
        ), f'"{path}" does not end with "/"'
        item: boxsdk.object.item.Item
        for item in folder.get_items(
            **({"direction": "desc"} if sort_reverse else {}),
            **({"sort": "name"} if sort_key == FileSortKey.NAME else {}),
            **({"sort": "date"} if sort_key == FileSortKey.MODIFIED else {}),
            fields=("name", "modified_at"),
        ):
            if (
                isinstance(item, boxsdk.object.folder.Folder)
                and include_folders
            ):
                yield f"{path}{item['name']}/", item
            elif isinstance(item, boxsdk.object.file.File) and include_files:
                yield f"{path}{item['name']}", item
            if recursive and isinstance(item, boxsdk.object.folder.Folder):
                yield from self._iter_folder_items(
                    f"{path}{item['name']}/",
                    item,
                    recursive=recursive,
                    sort_reverse=sort_reverse,
                    include_files=include_files,
                    include_folders=include_folders,
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
        folder: boxsdk.object.item.Item = self._get_folder_path_item(
            self._root_folder, directory
        )
        if directory and not directory.endswith("/"):
            directory = f"{directory}/"
        assert isinstance(
            folder, boxsdk.object.folder.Folder
        ), f'"{directory}" is a file, not a directory/folder'
        yield from map(
            itemgetter(0),
            self._iter_folder_items(
                directory,
                folder,
                recursive=recursive,
                sort_key=sort_key,
                sort_reverse=sort_reverse,
                include_files=True,
                include_folders=False,
            ),
        )

    def iter_sub_directories(
        self,
        directory: str = "",
        recursive: bool = False,
        sort_key: FileSortKey = FileSortKey.DEFAULT,
        sort_reverse: bool = False,
    ) -> Iterable[str]:
        """
        Iterate over all sub-directories of a specified directory.

        Parameters:

        - directory (str)
        - recursive (bool) = True: If `False`, only *direct* descendants of the
          specified `directory` will be included. If `True`, *all*
          sub-directories, including sub-directories of each sub-directory,
          etc., will be included.
        - sort_key (file_system_client.base.FileSortKey)
          = file_system_client.base.FileSortKey.DEFAULT
        - sort_reverse (bool) = False
        """
        if directory.endswith("/"):
            directory = directory.rstrip("/")
        folder: boxsdk.object.item.Item = self._get_folder_path_item(
            self._root_folder, directory
        )
        assert isinstance(
            folder, boxsdk.object.folder.Folder
        ), f'"{directory}" is a file, not a directory/folder'
        yield from map(
            itemgetter(0),
            self._iter_folder_items(
                directory,
                folder,
                recursive=recursive,
                sort_key=sort_key,
                sort_reverse=sort_reverse,
                include_files=False,
                include_folders=True,
            ),
        )

    def is_file(self, path: str) -> bool:
        """
        Return `True` if a *file* exists at the specified `path`.

        Parameters:

        - path (str): A path, relative to the file system root, at which to
          look for a file.
        """
        try:
            return isinstance(
                self._get_item(path),
                boxsdk.object.file.File,
            )
        except FileNotFoundError:
            return False

    def is_directory(self, path: str) -> bool:
        """
        Return `True` if a directory exists at the specified `path`.

        Parameters:

        - path (str): A path, relative to the file system root, at which to
          look for a directory.
        """
        try:
            return isinstance(
                self._get_item(path),
                boxsdk.object.folder.Folder,
            )
        except FileNotFoundError:
            return False

    def get_absolute_path(self, path: str = "") -> str:
        """
        Get an "absolute" file path from a relative path.
        """
        # No Box-specific logic is known to be needed here...
        return super().get_absolute_path(path)

    # For backwards compatibility
    get_file_paths = iter_file_paths
    get_sub_directories = iter_sub_directories


def from_url(url: str) -> Box:
    parse_result: ParseResult = urlparse(url)
    assert (parse_result.scheme or "http").lower() == "http"
    path: str = f"{parse_result.netloc}{parse_result.path}"
    return Box(
        path,
        **get_class_url_keyword_arguments(
            cls=Box,
            url=url,
        ),
    )
