import sys
import warnings
from collections import deque
from pathlib import Path
from time import sleep
from typing import Iterable, Optional

import pytest

from file_system_client.base import FileSystem
from file_system_client.box import Box
from file_system_client.dbfs import DatabricksFileSystem
from file_system_client.local import Local, from_url
from file_system_client.s3 import SimpleStorageService
from file_system_client.s3 import from_url as s3_from_url
from file_system_client.s3 import get_web_identity_token
from file_system_client.utilities import run

TESTS_PATH: Path = Path(__file__).absolute().parent
DATABRICKS_TOKEN_CERBERUS_PATH: str = (
    "app/sustainability/sustainability/"
    "ServicePrincipal_-sole-react.cloud.databricks.com_"
    "App.Sole.sustainability.Developer"
)
DBFS_TEST_FILES_DIRECTORY: Path = (
    Path(__file__).absolute().parent.joinpath(".dbfs_files")
)
TEST_FILES_DIRECTORY: Path = Path(__file__).absolute().parent.joinpath("files")
BOX_SHARED_DIRECTORY_URL: str = (
    "https://box.com/s/kcfl0m2op2x1ly7f5w6tccqcuw1rp2dj"
)
BOX_HOME: str = (
    "test--file-system-client/"
    # Differentiate by python version to avoid conflicting
    # reads/writes during multi-version testing
    f"py{sys.version_info.major}.{sys.version_info.minor}/"
)
DBFS_HOME: str = (
    "/Volumes/development/team_sustainability/waffle_window/"
    "test--file-system-client/"
    # Differentiate by python version to avoid conflicting
    # reads/writes during multi-version testing
    f"py{sys.version_info.major}.{sys.version_info.minor}/"
)
DBFS_READ_ONLY_HOME: str = (
    "/Volumes/development/team_sustainability/waffle_window/dev/tables/"
)


def _clear(client: FileSystem) -> None:
    """
    This function deletes all files and directories under the client root.
    """
    # Cleanup Files
    deque(map(client.delete, client.iter_file_paths(recursive=True)))

    # Cleanup Directories
    deque(
        map(
            client.delete_directory,
            client.iter_sub_directories(recursive=False),
        )
    )


@pytest.fixture(name="test_files_client", scope="session", autouse=True)
def setup_test_files_client() -> Local:
    return Local(str(TEST_FILES_DIRECTORY))


@pytest.fixture(name="box_shared_client", scope="session")
def setup_teardown_shared_box_client(
    test_files_client: Local,
) -> Iterable[Box]:
    """
    This fixture creates a shared directory, then creates a Box client
    in that shared directory and populates it with test files.
    """
    # Create a non-shared client
    box_client: Box = Box(  # type: ignore
        root=f"{BOX_HOME}shared/",
        client_id_cerberus_path="app/sustainability/box/client_id",
        client_secret_cerberus_path="app/sustainability/box/client_secret",
        public_key_id_cerberus_path="app/sustainability/box/public_key_id",
        private_key_cerberus_path="app/sustainability/box/private_key",
        passphrase_cerberus_path="app/sustainability/box/passphrase",
        enterprise_id_cerberus_path="app/sustainability/box/enterprise_id",
        echo=True,
    )
    _clear(box_client)
    # Upload test files
    path: str
    for path in test_files_client.iter_file_paths(recursive=True):
        box_client.put(test_files_client.get(path), path)
    # Create a shared client
    box_shared_client: Box = Box(  # type: ignore
        # Create a shared URL using the non-shared client, and use it to create
        # a shared client
        root=box_client.get_url(),
        client_id_cerberus_path="app/sustainability/box/client_id",
        client_secret_cerberus_path="app/sustainability/box/client_secret",
        public_key_id_cerberus_path="app/sustainability/box/public_key_id",
        private_key_cerberus_path="app/sustainability/box/private_key",
        passphrase_cerberus_path="app/sustainability/box/passphrase",
        enterprise_id_cerberus_path="app/sustainability/box/enterprise_id",
        echo=True,
    )
    yield box_shared_client
    # Cleanup
    _clear(box_client)


@pytest.fixture(name="box_client", scope="session")
def setup_teardown_box_client(test_files_client: Local) -> Iterable[Box]:
    """
    This fixture creates a Box client relative the app's/user's home directory
    and populates it with test files.
    """
    # Cleanup existing files
    box_client: Box = Box(  # type: ignore
        root=f"{BOX_HOME}not-shared/",
        client_id_cerberus_path="app/sustainability/box/client_id",
        client_secret_cerberus_path="app/sustainability/box/client_secret",
        public_key_id_cerberus_path="app/sustainability/box/public_key_id",
        private_key_cerberus_path="app/sustainability/box/private_key",
        passphrase_cerberus_path="app/sustainability/box/passphrase",
        enterprise_id_cerberus_path="app/sustainability/box/enterprise_id",
        echo=True,
    )
    # Cleanup Files
    _clear(box_client)
    # Upload test files
    path: str
    for path in test_files_client.iter_file_paths(recursive=True):
        box_client.put(test_files_client.get(path), path)
    yield box_client
    _clear(box_client)


@pytest.fixture(name="dbfs_client", scope="session")
def setup_teardown_dbfs_client(
    test_files_client: Local,
) -> Iterable[DatabricksFileSystem]:
    """
    This fixture creates a Databricks File System client.
    """
    dbfs_client: DatabricksFileSystem = DatabricksFileSystem(
        root=DBFS_HOME, token_cerberus_path=DATABRICKS_TOKEN_CERBERUS_PATH
    )
    _clear(dbfs_client)
    # Upload test files
    path: str
    for path in test_files_client.iter_file_paths(recursive=True):
        dbfs_client.put(test_files_client.get(path), path)
    yield dbfs_client
    # Cleanup Files
    _clear(dbfs_client)


@pytest.fixture(name="dbfs_local_client", scope="session")
def setup_teardown_dbfs_local_client(
    test_files_client: Local,
) -> Iterable[DatabricksFileSystem]:
    """
    This fixture creates a Databricks File System client for local use.
    """
    dbfs_client: DatabricksFileSystem = DatabricksFileSystem(
        root=str(DBFS_TEST_FILES_DIRECTORY)
    )
    _clear(dbfs_client)
    # Upload test files
    path: str
    for path in test_files_client.iter_file_paths(recursive=True):
        dbfs_client.put(test_files_client.get(path), path)
    yield dbfs_client
    # Cleanup Files
    _clear(dbfs_client)


@pytest.fixture(name="local_client", scope="session")
def setup_teardown_local_client(test_files_client: Local) -> Iterable[Local]:
    """
    This fixture creates a Local File System client.
    """
    local_client: Local = from_url()
    # Upload test files
    path: str
    for path in test_files_client.iter_file_paths(recursive=True):
        local_client.put(test_files_client.get(path), path)
    yield local_client
    # Cleanup Files
    _clear(local_client)


@pytest.fixture(name="s3_client", scope="session")
def setup_teardown_s3_client(
    test_files_client: Local,
) -> Iterable[SimpleStorageService]:
    """
    This fixture creates an S3 client.
    """
    # Start up localstack
    warnings.filterwarnings("ignore", category=ResourceWarning)
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    run(
        [
            "docker-compose",
            "-f",
            str(TESTS_PATH.joinpath("docker-compose.yml")),
            "--project-directory",
            str(TESTS_PATH),
            "up",
            "-d",
        ],
    )
    sleep(20)
    # Create the client
    s3_client: SimpleStorageService = s3_from_url(
        "s3://test-bucket/test/prefix/",
        endpoint_url="http://localhost:4566",
    )
    # Cleanup Files
    _clear(s3_client)
    # Upload test files
    path: str
    for path in test_files_client.iter_file_paths(recursive=True):
        s3_client.put(test_files_client.get(path), path)
    yield s3_client
    # Cleanup Files
    _clear(s3_client)
    # Shutdown localstack
    run(
        [
            "docker-compose",
            "-f",
            str(TESTS_PATH.joinpath("docker-compose.yml")),
            "--project-directory",
            str(TESTS_PATH),
            "down",
        ],
    )


@pytest.fixture(name="s3_oidc_client", scope="session")
def setup_teardown_s3_oidc_client(
    test_files_client: Local,
) -> Iterable[Optional[SimpleStorageService]]:
    """
    This fixture creates an S3 client using OIDC authentication.
    """
    s3_client: Optional[SimpleStorageService] = None
    if get_web_identity_token():
        s3_client = SimpleStorageService(
            "-sustainability-prod-us-west-2",
            root="test_file_system_client/prefix/",
            arn="arn:aws:iam::567546912947:role/bmx-sustainability",
            region_name="us-west-2",
        )
        _clear(s3_client)
        # Upload test files
        path: str
        for path in test_files_client.iter_file_paths(recursive=True):
            s3_client.put(test_files_client.get(path), path)
    yield s3_client
    # Cleanup Files
    if s3_client:
        _clear(s3_client)
