import pickle

import pytest

from file_system_client.local import Local
from file_system_client.s3 import SimpleStorageService


def test_pickle(s3_client: SimpleStorageService) -> None:
    unpickled_s3_client: SimpleStorageService = pickle.loads(
        pickle.dumps(s3_client)
    )
    assert unpickled_s3_client.root == s3_client.root
    assert unpickled_s3_client.bucket == s3_client.bucket
    pickle.dumps(unpickled_s3_client)


def test_get(s3_client: SimpleStorageService, local_client: Local) -> None:
    assert s3_client.get("a.txt").read() == local_client.get("a.txt").read()
    assert (
        s3_client.get("sub-directory-1/a1.txt").read()
        == local_client.get("sub-directory-1/a1.txt").read()
    )


def test_get_url(s3_client: SimpleStorageService) -> None:
    url: str = s3_client.get_url("a.txt")
    assert url.startswith("s3://"), url


def test_iter_file_paths_not_shared(
    s3_client: SimpleStorageService, local_client: Local
) -> None:
    assert set(s3_client.iter_file_paths()) == set(
        local_client.iter_file_paths()
    )
    sub_directory: str
    for sub_directory in local_client.iter_sub_directories():
        assert set(s3_client.iter_file_paths(sub_directory)) == set(
            local_client.iter_file_paths(sub_directory)
        )


def test_is_file(s3_client: SimpleStorageService) -> None:
    assert s3_client.is_file("sub-directory-1/a1.txt")


def test_is_directory(s3_client: SimpleStorageService) -> None:
    assert s3_client.is_directory("sub-directory-1/")


def test_iter_sub_directories(
    s3_client: SimpleStorageService, local_client: Local
) -> None:
    assert set(s3_client.iter_sub_directories(recursive=True)) == set(
        local_client.iter_sub_directories(recursive=True)
    )
    assert set(s3_client.iter_sub_directories(recursive=False)) == set(
        local_client.iter_sub_directories(recursive=False)
    )


if __name__ == "__main__":
    pytest.main(["tests/test_s3.py", "-s", "-vv"])
