from itertools import chain
import unittest
import os
import sys
from time import time
from typing import Any, Dict, Tuple
from docker_utilities.config import SERVER
from docker_utilities.build import Platform, build
from docker_utilities.exists import exists
from docker_utilities._utilities import (
    check_call,
    get_tuple_str,
    check_output,
)

TEST_DIRECTORY: str = os.path.dirname(os.path.abspath(__file__))
TEST_IMAGE: str = f"{SERVER}/sustainability/test-docker-utilities"
KWARGS: Dict[str, Any] = {
    "file": "Dockerfile",
    "user": "a.BMX.SUSTAINABILITY",
    "password_cerberus_path": "app/sustainability/bmx/a.BMX.SUSTAINABILITY",
}
BUILD_COMMAND: Tuple[str, ...] = (
    sys.executable,
    "-m",
    "docker_utilities",
    "build",
    "-f",
    "Dockerfile",
    "-u",
    "a.BMX.SUSTAINABILITY",
    "-pcp",
    "app/sustainability/bmx/a.BMX.SUSTAINABILITY",
)
EXISTS_COMMAND: Tuple[str, ...] = (
    sys.executable,
    "-m",
    "docker_utilities",
    "exists",
    "-u",
    "a.BMX.SUSTAINABILITY",
    "-pcp",
    "app/sustainability/bmx/a.BMX.SUSTAINABILITY",
)
PLATFORMS: Tuple[Platform, ...] = (
    Platform.LINUX_AMD64,
    Platform.LINUX_ARM64,
)


def get_version() -> str:
    return f"0.0.{int(time())}"


class TestBuild(unittest.TestCase):
    """
    Test `docker_utilities.build`
    """

    @classmethod
    def setUpClass(cls) -> None:
        os.chdir(TEST_DIRECTORY)
        super().setUpClass()

    def test_single_platform_build(self) -> None:
        """
        Test `docker_utilities.build.build` with no `platforms` specified
        """
        version: str = get_version()
        versioned_tag: str = f"{TEST_IMAGE}:{version}"
        tags: Tuple[str, ...] = (
            versioned_tag,
            f"{TEST_IMAGE}:latest",
            TEST_IMAGE,
        )
        assert not exists(versioned_tag)
        assert build(
            tags=tags,
            **KWARGS,
        )
        for tag in tags:
            assert exists(tag)
        # These should already exist now, so if `skip_existing=True`,
        # the returned value should be `False`
        assert not build(
            tags=tags,
            skip_existing=True,
            **KWARGS,
        )

    def test_cli_single_platform_build(self) -> None:
        """
        Test `docker_utilities.build.build` with no `platforms` specified
        """
        version: str = get_version()
        versioned_tag: str = f"{TEST_IMAGE}:{version}"
        tags: Tuple[str, ...] = (
            versioned_tag,
            f"{TEST_IMAGE}:latest",
            TEST_IMAGE,
        )
        assert (
            check_output(EXISTS_COMMAND + (versioned_tag,)).strip() == "false"
        )
        check_call(
            BUILD_COMMAND
            + tuple(chain(*zip(("-t",) * len(tags), tags)))  # type: ignore
        )
        for tag in tags:
            assert check_output(EXISTS_COMMAND + (tag,)).strip() == "true"

    def test_multi_platform_build(self) -> None:
        """
        Test `docker_utilities.build.build` with one or more
        `platforms` specified
        """
        version: str = get_version()
        versioned_tag: str = f"{TEST_IMAGE}:{version}"
        tags: Tuple[str, ...] = (
            versioned_tag,
            f"{TEST_IMAGE}:latest",
            TEST_IMAGE,
        )
        assert not exists(versioned_tag)
        assert build(
            tags=tags,
            platforms=PLATFORMS,
            **KWARGS,
        )
        for tag in tags:
            assert exists(tag)
        # These should already exist now, so if `skip_existing=True`,
        # the returned value should be `False`
        assert not build(
            tags=tags,
            platforms=PLATFORMS,
            skip_existing=True,
            **KWARGS,
        )

    def test_cli_multi_platform_build(self) -> None:
        """
        Test `docker_utilities.build.build` with no `platforms` specified
        """
        version: str = get_version()
        versioned_tag: str = f"{TEST_IMAGE}:{version}"
        tags: Tuple[str, ...] = (
            versioned_tag,
            f"{TEST_IMAGE}:latest",
            TEST_IMAGE,
        )
        assert (
            check_output(EXISTS_COMMAND + (versioned_tag,)).strip() == "false"
        )
        platforms: Tuple[str, ...] = get_tuple_str(PLATFORMS)
        check_call(
            BUILD_COMMAND
            + tuple(
                chain(
                    *zip(  # type: ignore
                        ("--platform",) * len(platforms), platforms
                    )
                )
            )
            + tuple(chain(*zip(("-t",) * len(tags), tags)))  # type: ignore
        )
        for tag in tags:
            assert check_output(EXISTS_COMMAND + (tag,)).strip() == "true"


if __name__ == "__main__":
    unittest.main()
