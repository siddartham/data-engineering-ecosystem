import logging
from abc import ABC, abstractmethod
from collections import namedtuple
from datetime import date, datetime
from io import BytesIO
from typing import IO, Iterable, List, Optional, Tuple, Type, Union

from .utilities import (
    SUCCESS,
    SUCCESS_FILE_NAME,
    FileSortKey,
    get_date_directory_name,
    get_path_datetime_and_index,
    is_date_partition_directory,
)

# The following line is needed for backwards-compatibility
assert get_date_directory_name  # type: ignore
log: logging.Logger = logging.getLogger(__name__)


LatestDirectoryFiles: Type[tuple] = namedtuple(
    "LatestDirectoryFiles", ("directory", "files")
)
LatestDirectorySubDirectories: Type[tuple] = namedtuple(
    "LatestDirectorySubDirectories", ("directory", "sub_directories")
)


class FileSystem(ABC):
    """
    This class defines a common interface for file system clients
    """

    def __init__(self, root: str = "") -> None:
        self._root: str = ""
        self.root: str = root

    @property
    def root(self) -> str:
        return self._root

    @root.setter
    def root(self, root: str) -> None:
        assert isinstance(root, str)
        self._root = root.strip()

    @abstractmethod
    def put(self, file: Union[IO[bytes], bytes], path: str) -> str:
        """
        Save a file to the specified path (relative to `self.root`).

        Parameters:

        - file (typing.IO[bytes]|bytes): Either a file-like object from which
          the `.read()` method returns `bytes`, or an instance of `bytes`.
        - path (str): A path, relative to `self.root`, to which the file object
          will be saved.
        """
        raise NotImplementedError()

    @abstractmethod
    def delete(self, path: str) -> None:
        """
        Delete a file.

        Parameters:

        - path (str)
        """
        raise NotImplementedError()

    @abstractmethod
    def get(self, path: str) -> IO[bytes]:
        """
        Retrieve a file.

        Parameters:

        - path (str): The path of a file relative to the root directory.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_url(self, path: str) -> str:
        """
        Get an absolute URL from a relative path.

        Parameters:

        - path (str): A file path relative to `self.root`.
        """
        raise NotImplementedError()

    @abstractmethod
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
        raise NotImplementedError()

    # For backwards compatibility
    get_file_paths = iter_file_paths

    @abstractmethod
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
        raise NotImplementedError()

    get_sub_directories = iter_sub_directories

    def iter_file_urls(
        self,
        directory: str = "",
        recursive: bool = True,
        sort_key: FileSortKey = FileSortKey.DEFAULT,
        sort_reverse: bool = False,
    ) -> Iterable[str]:
        """
        Iterate over file URLs within a directory.

        Parameters:

        - directory (str)
        - recursive (bool) = True
        - sort_key (file_system_client.base.FileSortKey) =
          file_system_client.base.FileSortKey.DEFAULT: This parameter
          indicates what property of the files to use for sorting returned
          file paths. By default, the file system default behavior will be
          used. The other sorting options available are:
          - MODIFIED: The date on which the file was most recently modified.
          - NAME: Alphabetical sorting.
        - sort_reverse (bool) = False: By default, sorting is in ascending
          order. If `sort_reverse is True`, sorting will be the opposite
          (descending order).
        """
        return map(
            self.get_url,
            self.iter_file_paths(
                directory=directory,
                recursive=recursive,
                sort_key=sort_key,
                sort_reverse=sort_reverse,
            ),
        )

    get_file_urls = iter_file_urls

    @abstractmethod
    def get_absolute_path(self, path: str) -> str:
        """
        Return the absolute path of the specified file path, if the path
        provided is expressed relative to the file system root. If the path
        is already an absolute path, just return that path.

        Parameters:

        - path (str)
        """
        absolute_path: str = path
        if path:
            if self.root and not path.startswith(self.root):
                if path.startswith(self.root.lstrip("/ ")):
                    absolute_path = f"/{path}"
                else:
                    stripped_path: str = path.lstrip("/ ")
                    if stripped_path.startswith(self.root):
                        absolute_path = stripped_path
                    elif path.startswith("/") and self.root.endswith("/"):
                        absolute_path = f"{self.root}{stripped_path}"
                    else:
                        absolute_path = f"{self.root}{path}"
        else:
            absolute_path = self.root
        assert "//" not in absolute_path, absolute_path
        return absolute_path

    def get_relative_path(self, path: str) -> str:
        """
        Given an absolute file path, return the same path expressed
        relative to the file system root.

        Parameters:

        - path (str)

        Returns: A file path relative to the file system root.
        """
        relative_path: str
        if path:
            relative_path = path.strip().replace("\\", "/")
            if self.root:
                root_length: int = len(self.root)
                if relative_path.startswith(self.root):
                    relative_path = relative_path[root_length:None]
                elif self.root.startswith("/") and (
                    f"/{relative_path}".startswith(self.root)
                ):
                    root_length -= 1
                    relative_path = f"/{relative_path[root_length:None]}"
                elif relative_path.startswith(f"/{self.root}"):
                    root_length += 1
                    relative_path = relative_path[root_length:None]
                elif relative_path.startswith("/") and self.root.endswith("/"):
                    relative_path = relative_path.lstrip("/ ")
        else:
            relative_path = self.root
        return relative_path

    @abstractmethod
    def is_file(self, path: str) -> bool:
        """
        Return `True` if a *file* exists at the specified `path`.

        Parameters:

        - path (str): A path, relative to the file system root, at which to
          look for a file.
        """
        raise NotImplementedError()

    @abstractmethod
    def is_directory(self, path: str) -> bool:
        """
        Return `True` if a directory exists at the specified `path`.

        Parameters:

        - path (str): A path, relative to the file system root, at which to
          look for a directory.
        """
        raise NotImplementedError()

    def had_success(self, directory: str) -> bool:
        """
        Check to see if files in the specified directory are part of a
        successfully completed operation (as opposed to being created as part
        of an operation which failed or was terminated prematurely). This is
        indicated by the presence of an empty file named "_SUCCESS".

        Note: If this directory does not exist, this method will return
        `False`, the same as if it existed but had no success indicator.

        Parameters:

        - directory (str)
        """
        log.info(f"Checking for a success indicator: {directory}")
        return self.is_file(f"{directory.rstrip('/ ')}/{SUCCESS_FILE_NAME}")

    def delete_success(self, directory: str) -> None:
        """
        If present, remove from the specified `directory` the success
        indicatory file. This is a file named "_SUCCESS", which indicates
        that the last operation on this directory was successful (as
        opposed to being still in-progress, or having failed).

        Note: If this directory does not exist, no error is raised.

        Parameters:

        - directory (str): The path, relative to the file system root, of
          a directory.
        """
        if self.had_success(directory):
            path: str = f'{directory.rstrip("/ ")}/{SUCCESS_FILE_NAME}'
            log.info(f"Deleting success indicator: {path}")
            self.delete(path)

    def put_success(self, directory: str) -> None:
        """
        Create a success indicator file in the specified `directory`,
        if one does not already exist (this is an empty file named "_SUCCESS").

        Note: If this `directory` does not exist, it will be created. If the
        success indicator already exists, no error will be raised.

        Parameters:

        - directory (str): A directory path, relative to the file system root,
          under which to create a success indicator file.
        """
        log.info(f"Putting a success indicator: {directory}")
        self.put(
            BytesIO(SUCCESS),
            f'{directory.rstrip("/ ")}/{SUCCESS_FILE_NAME}',
        )

    def iter_latest_directory_sub_directories(
        self, directory: str
    ) -> LatestDirectorySubDirectories:
        """
        This method finds the most recently created sub-directory under
        the specified `directory` (as determined by name, not file system
        metadata), and returns a tuple containing two items:

        - The first item in the returned tuple is the path of a timestamp-named
          sub-directory, located directly under `directory`, which was created
          most recently.
        - The second item in the returned tuple is an iterable which yields the
          path of all sub-sub-directories, directly under the latest
          timestamp-named sub-directory. This iterable is equivalent to the
          response you would get from
          `FileSystem.iter_latest_directories` for the same `directory`.

        Parameters:

        - directory (str): A directory path, relative to the file system root,
          under which to look for the most recently created sub-directory
          as determined by the sub-directory name.

          Notes:

          The date and time associated with a sub-directory will be determined
          using the function
          `file_system_client.utilities.get_path_datetime_and_index`,
          which simply finds all segments of numeric digits in a sub-directory
          name, and assigns the first chunk of numeric digits to a year,
          the next to a month, the next to a day, hour, minute, second, etc.
          Separators can be anything (except for numeric digits, of course).

          Sub-directory names conforming to the needed format can be produced
          with consistent formatting using the function
          `file_system_client.utilities.get_date_directory_name`.
        """
        latest_directory: str = self.get_latest_directory(directory)
        return LatestDirectorySubDirectories(
            directory=latest_directory,
            sub_directories=self.iter_sub_directories(
                latest_directory, recursive=False
            ),
        )

    def iter_latest_directories(self, directory: str) -> Iterable[str]:
        """
        This method finds the most recently created sub-directory under
        the specified `directory` (as determined by name, not file system
        metadata), and returns an iterable of all sub-sub-directories directly
        under that sub-directory.

        The iterable returned by this method is equivalent to the second item
        in the tuple returned by
        `FileSystem.iter_latest_directory_sub_directories`.

        Parameters:

        - directory (str): A directory path, relative to the file system root,
          under which to look for the most recently created sub-directory
          as determined by the sub-directory name.

          Notes:

          The date and time associated with a sub-directory will be determined
          using the function
          `file_system_client.utilities.get_path_datetime_and_index`,
          which simply finds all segments of numeric digits in a sub-directory
          name, and assigns the first chunk of numeric digits to a year,
          the next to a month, the next to a day, hour, minute, second, etc.
          Separators can be anything (except for numeric digits, of course).

          Sub-directory names conforming to the needed format can be produced
          with consistent formatting using the function
          `file_system_client.utilities.get_date_directory_name`.
        """
        return self.iter_latest_directory_sub_directories(
            directory
        ).sub_directories

    # For backwards compatibility
    get_latest_directories = iter_latest_directories

    def iter_latest_directory_files(
        self, directory: str, recursive: bool = True
    ) -> LatestDirectoryFiles:
        """
        This method finds the most recently created sub-directory under
        the specified `directory` (as determined by name, not file system
        metadata), and returns a tuple containing two items:

        - The first item in the returned tuple is the path of the
          timestamp-named sub-directory, located directly under `directory`,
          which was created most recently.
        - The second item in the returned tuple is an iterable which yields the
          path of all files directly under the latest timestamp-named
          sub-directory. This iterable is equivalent to the response you would
          get from `FileSystem.iter_latest_files` for the same `directory`.

        Parameters:

        - directory (str): A directory path, relative to the file system root,
          under which to look for the most recently created sub-directory
          as determined by the sub-directory name.

          Notes:

          The date and time associated with a sub-directory will be determined
          using the function
          `file_system_client.utilities.get_path_datetime_and_index`,
          which simply finds all segments of numeric digits in a sub-directory
          name, and assigns the first chunk of numeric digits to a year,
          the next to a month, the next to a day, hour, minute, second, etc.
          Separators can be anything (except for numeric digits, of course).

          Sub-directory names conforming to the needed format can be produced
          with consistent formatting using the function
          `file_system_client.utilities.get_date_directory_name`.

        - recursive (bool) = True: If `False`, only files *directly* under
          the time-stamped sub-directory will be included. If `True` (the
          default), files will be discovered and yielded recursively under
          descendant sub-sub-directories, etc.
        """
        sub_directory: str = self.get_latest_directory(directory)
        path: str
        return LatestDirectoryFiles(
            directory=sub_directory,
            files=filter(
                lambda path: path.split("/")[-1] != SUCCESS_FILE_NAME,
                self.iter_file_paths(sub_directory, recursive=recursive),
            ),
        )

    def iter_latest_files(
        self, directory: str, recursive: bool = True
    ) -> Iterable[str]:
        """
        This method finds the most recently created sub-directory under
        the specified `directory` (as determined by name, not file system
        metadata), and returns an iterable of all sub-sub-directories directly
        under that sub-directory.

        The iterable returned by this method is equivalent to the second item
        in the tuple returned by
        `FileSystem.iter_latest_directory_sub_directories`.

        Parameters:

        - directory (str): A directory path, relative to the file system root,
          under which to look for the most recently created sub-directory
          as determined by the sub-directory name.

          Notes:

          The date and time associated with a sub-directory will be determined
          using the function
          `file_system_client.utilities.get_path_datetime_and_index`,
          which simply finds all segments of numeric digits in a sub-directory
          name, and assigns the first chunk of numeric digits to a year,
          the next to a month, the next to a day, hour, minute, second, etc.
          Separators can be anything (except for numeric digits, of course).

          Sub-directory names conforming to the needed format can be produced
          with consistent formatting using the function
          `file_system_client.utilities.get_date_directory_name`.

        - recursive (bool) = True: If `False`, only files *directly* under
          the time-stamped sub-directory will be included. If `True` (the
          default), files will be discovered and yielded recursively under
          descendant sub-sub-directories, etc.
        """
        path: str
        return self.iter_latest_directory_files(
            directory, recursive=recursive
        ).files

    def get_latest_files(
        self, directory: str, recursive: bool = True
    ) -> Tuple[str, ...]:
        """
        See `FileSystem.iter_latest_files`. This function simply returns
        a tuple instead of an iterator.
        """
        return tuple(self.iter_latest_files(directory, recursive=recursive))

    def get_latest_timestamp(self, directory: str) -> Optional[datetime]:
        """
        Return the timestamp of the latest sub-directory nested under
        `directory`, as determined by `get_path_datetime_and_index()`.

        Parameters:

        - directory (str): A directory path, relative to the file system root,
          under which to look for the most recently created sub-directory
          as determined by the sub-directory name.
        """
        latest_directory: str = self.get_latest_directory(directory)
        if latest_directory:
            return get_path_datetime_and_index(latest_directory).datetime
        return None

    def clear(self, directory: str = "") -> None:
        """
        Delete all files in a directory.

        Parameters:

        - directory (str): A directory path, relative to the file system root.
        """
        file_path: str
        for file_path in self.iter_file_paths(directory):
            self.delete(file_path)

    def delete_directory(self, directory: str) -> None:
        """
        Delete a directory and all files in that directory. For some file
        systems, this may be effectively the same as `self.clear`.

        Parameters:

        - directory (str): A directory path, relative to the file system root.
        """
        self.clear(directory)

    def get_latest_directory(self, directory: str) -> str:
        """
        Parameter:

        - directory (str): A directory under which to search
          for time-stamped sub-directories.

        Returns: The most recently timestamped "sub-directory" path (object
        prefix) having a success indicator nested within.
        """
        directory_: str
        try:
            return self.get_relative_path(
                max(
                    filter(
                        self.had_success,
                        filter(
                            is_date_partition_directory,
                            self.iter_sub_directories(
                                directory, recursive=False
                            ),
                        ),
                    ),
                    key=lambda directory_: get_path_datetime_and_index(
                        directory_
                    ).datetime,
                )
            )
        except ValueError:
            return ""

    def get_date_partition_directory(
        self,
        directory: str = "",
        date_or_datetime: Union[date, datetime, None] = None,
        prefix: str = "date_partition=",
        precision: int = 5,
    ) -> str:
        """
        Get the path for a sub-directory, directly under `directory`,
        named to indicate it was created on the specified `date_or_datetime`.

        Parameters:

        - directory (str) = "": A directory, relative to the file system
          root, under which the date partition sub-directory will be.
        - date_or_datetime (datetime.datetime|datetime.date|None) = None:
          This indicates the date or date + time to use for the sub-directory
          naming. If not provided, the current date and time are used.
        - prefix (str) = "date_partition=": A prefix with which to prepend the
          formatted date/datetime string.
        - precision (int) = 5: The number of datetime components to include.
          The default precision is 5, which includes year + month + day + hour
          + minute. A precision of 6 would also include seconds, and a
          precision of 7 would include seconds + microseconds.
        """
        sub_directory = get_date_directory_name(
            date_or_datetime,
            prefix=prefix,
            precision=precision,
        )
        return (
            f"{self.get_relative_path(directory).rstrip(' /')}/"
            f"{sub_directory}/"
        )

    def get_unique_date_partition_directory(
        self,
        path: str,
    ) -> str:
        """
        Given a date-partition directory path, return a variation
        which is not already in existence by appending seconds/microseconds
        as needed.

        Parameters:

        - path (str): A file path, relative to the file system root, at which
          to check for an existing file or directory.
        """
        assert is_date_partition_directory(path)
        suffix: str = ""
        if path.rstrip(" ").endswith("/"):
            suffix = "/"
        non_unique_path: str = path.rstrip("/ ")
        if not self.is_directory(f"{non_unique_path}/"):
            return f"{non_unique_path}{suffix}"
        start: int = 1
        path_parts: List[str] = non_unique_path.split("/")
        timestamp_parts: List[str] = path_parts[-1].split("-")
        precision: int = len(timestamp_parts)
        if precision > 5:
            start = int(timestamp_parts[-1]) + 1
            non_unique_path = (
                f"{'/'.join(path_parts[:-1])}/"
                f"{'-'.join(timestamp_parts[:-1])}"
            )
        # Seconds should be represented with 2 digits (example: "01"), whereas
        # microseconds should be represented with 6 digits (example: "000001")
        number_of_digits: int = 2 if (precision < 6) else 6
        buffer: str = "0" * number_of_digits
        index: int
        for index in range(start, 61):
            index_string: str = f"{buffer}{index}"[-number_of_digits:]
            unique_path: str = f"{non_unique_path}-{index_string}/"
            if not self.is_directory(unique_path):
                return f"{unique_path}{suffix}"
        if precision < 6:
            unique_path = self.get_unique_date_partition_directory(
                f"{path.rstrip('/ ')}-00"
            )
            return f"{unique_path}{suffix}"
        elif precision == 6:
            unique_path = self.get_unique_date_partition_directory(
                f"{path.rstrip('/ ')}-000000"
            )
            return f"{unique_path}{suffix}"
        raise ValueError(path)
