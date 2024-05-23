import pickle
from pathlib import Path

import pytest

from file_system_client.box import Box
from file_system_client.local import Local

FILES: Path = Path(__file__).parent.joinpath("files")


def test_pickle(box_client: Box) -> None:
    unpickled_box_client: Box = pickle.loads(pickle.dumps(box_client))
    assert unpickled_box_client.root == box_client.root
    pickle.dumps(unpickled_box_client)


def test_get(box_client: Box, test_files_client: Local) -> None:
    assert (
        box_client.get("a.txt").read() == test_files_client.get("a.txt").read()
    )
    assert (
        box_client.get("sub-directory-1/a1.txt").read()
        == test_files_client.get("sub-directory-1/a1.txt").read()
    )


def test_shared_get(box_shared_client: Box, test_files_client: Local) -> None:
    assert (
        box_shared_client.get("a.txt").read()
        == test_files_client.get("a.txt").read()
    )
    assert (
        box_shared_client.get("sub-directory-1/a1.txt").read()
        == test_files_client.get("sub-directory-1/a1.txt").read()
    )


def test_get_url_not_shared(box_client: Box) -> None:
    url: str = box_client.get_url("a.txt")
    assert url.startswith("https://"), url


def test_get_url(box_shared_client: Box) -> None:
    assert box_shared_client.get_url("a.txt").startswith("https://")


def test_iter_file_paths_not_shared(
    box_client: Box, test_files_client: Local
) -> None:
    assert set(box_client.iter_file_paths()) == set(
        test_files_client.iter_file_paths()
    )
    sub_directory: str
    for sub_directory in test_files_client.iter_sub_directories():
        assert set(box_client.iter_file_paths(sub_directory)) == set(
            test_files_client.iter_file_paths(sub_directory)
        )


def test_iter_file_paths_shared(
    box_shared_client: Box, test_files_client: Local
) -> None:
    assert set(box_shared_client.iter_file_paths()) == set(
        test_files_client.iter_file_paths()
    )
    sub_directory: str
    for sub_directory in test_files_client.iter_sub_directories():
        assert set(box_shared_client.iter_file_paths(sub_directory)) == set(
            test_files_client.iter_file_paths(sub_directory)
        )


def test_is_file_not_shared(box_client: Box) -> None:
    assert box_client.is_file("sub-directory-1/a1.txt")


def test_is_file_shared(box_shared_client: Box) -> None:
    assert box_shared_client.is_file("sub-directory-1/a1.txt")


def test_is_directory_not_shared(box_client: Box) -> None:
    assert box_client.is_directory("sub-directory-1/")


def test_is_directory_shared(box_shared_client: Box) -> None:
    assert box_shared_client.is_directory("sub-directory-1/")


def test_iter_sub_directories_not_shared(
    box_client: Box, test_files_client: Local
) -> None:
    assert set(box_client.iter_sub_directories(recursive=True)) == set(
        test_files_client.iter_sub_directories(recursive=True)
    )
    assert set(box_client.iter_sub_directories(recursive=False)) == set(
        test_files_client.iter_sub_directories(recursive=False)
    )


def test_iter_sub_directories_shared(
    box_shared_client: Box, test_files_client: Local
) -> None:
    assert set(box_shared_client.iter_sub_directories(recursive=True)) == set(
        test_files_client.iter_sub_directories(recursive=True)
    )
    assert set(box_shared_client.iter_sub_directories(recursive=False)) == set(
        test_files_client.iter_sub_directories(recursive=False)
    )


if __name__ == "__main__":
    pytest.main(["tests/test_box.py", "-s", "-vv"])
