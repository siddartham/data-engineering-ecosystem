import pickle
from pathlib import Path

import pytest

from file_system_client.dbfs import DatabricksFileSystem
from file_system_client.local import Local

FILES: Path = Path(__file__).parent.joinpath("files")


def test_pickle(
    dbfs_client: DatabricksFileSystem,
    dbfs_local_client: DatabricksFileSystem,
) -> None:
    unpickled_dbfs_client: DatabricksFileSystem = pickle.loads(
        pickle.dumps(dbfs_client)
    )
    assert unpickled_dbfs_client.root == dbfs_client.root
    pickle.dumps(unpickled_dbfs_client)
    unpickled_dbfs_client = pickle.loads(pickle.dumps(dbfs_local_client))
    assert unpickled_dbfs_client.root == dbfs_local_client.root
    pickle.dumps(unpickled_dbfs_client)


def test_get(
    dbfs_client: DatabricksFileSystem,
    dbfs_local_client: DatabricksFileSystem,
    test_files_client: Local,
) -> None:
    assert (
        dbfs_client.get("a.txt").read()
        == test_files_client.get("a.txt").read()
    )
    assert (
        dbfs_client.get("sub-directory-1/a1.txt").read()
        == test_files_client.get("sub-directory-1/a1.txt").read()
    )
    assert (
        dbfs_local_client.get("a.txt").read()
        == test_files_client.get("a.txt").read()
    )
    assert (
        dbfs_local_client.get("sub-directory-1/a1.txt").read()
        == test_files_client.get("sub-directory-1/a1.txt").read()
    )


def test_get_url(
    dbfs_client: DatabricksFileSystem, dbfs_local_client: DatabricksFileSystem
) -> None:
    url: str = dbfs_client.get_url("a.txt")
    assert url.startswith("dbfs://"), url
    url = dbfs_local_client.get_url("a.txt")
    assert url.startswith("dbfs://"), url


def test_iter_file_paths_not_shared(
    dbfs_client: DatabricksFileSystem,
    dbfs_local_client: DatabricksFileSystem,
    test_files_client: Local,
) -> None:
    assert set(dbfs_client.iter_file_paths()) == set(
        test_files_client.iter_file_paths()
    )
    sub_directory: str
    for sub_directory in test_files_client.iter_sub_directories():
        assert set(dbfs_client.iter_file_paths(sub_directory)) == set(
            test_files_client.iter_file_paths(sub_directory)
        )
    assert set(dbfs_local_client.iter_file_paths()) == set(
        dbfs_local_client.iter_file_paths()
    )
    for sub_directory in dbfs_local_client.iter_sub_directories():
        assert set(dbfs_local_client.iter_file_paths(sub_directory)) == set(
            dbfs_local_client.iter_file_paths(sub_directory)
        )


def test_is_file(
    dbfs_client: DatabricksFileSystem, dbfs_local_client: DatabricksFileSystem
) -> None:
    assert dbfs_client.is_file("sub-directory-1/a1.txt")
    assert dbfs_local_client.is_file("sub-directory-1/a1.txt")


def test_is_directory(
    dbfs_client: DatabricksFileSystem, dbfs_local_client: DatabricksFileSystem
) -> None:
    assert dbfs_client.is_directory("sub-directory-1/")
    assert dbfs_local_client.is_directory("sub-directory-1/")


def test_iter_sub_directories(
    dbfs_client: DatabricksFileSystem,
    dbfs_local_client: DatabricksFileSystem,
    test_files_client: Local,
) -> None:
    assert set(dbfs_client.iter_sub_directories(recursive=True)) == set(
        test_files_client.iter_sub_directories(recursive=True)
    )
    assert set(dbfs_client.iter_sub_directories(recursive=False)) == set(
        test_files_client.iter_sub_directories(recursive=False)
    )
    assert set(dbfs_local_client.iter_sub_directories(recursive=True)) == set(
        test_files_client.iter_sub_directories(recursive=True)
    )
    assert set(dbfs_local_client.iter_sub_directories(recursive=False)) == set(
        test_files_client.iter_sub_directories(recursive=False)
    )


if __name__ == "__main__":
    pytest.main(["tests/test_dbfs.py", "-s", "-vv"])
