"""
OpenID Connect (OIDC) is an authentication protocol that verifies
user identities when they sign in to access digital resources
"""

import csv
import os
import unittest
import warnings
from datetime import datetime
from io import BytesIO, StringIO
from typing import Any, Optional, Tuple

from file_system_client import from_url
from file_system_client.s3 import SimpleStorageService, get_web_identity_token
from file_system_client.utilities import (
    is_date_partition_directory,
    lru_cache,
    url_is_local,
)

TEST_DIRECTORY: str = "test_directory/"
TEST1_DIRECTORY: str = f"{TEST_DIRECTORY}1/"
TEST2_DIRECTORY: str = f"{TEST_DIRECTORY}2/"
TEST_INCREMENTAL_DIRECTORY: str = f"{TEST_DIRECTORY}incremental/"
TEST1_CSV: str = f"{TEST1_DIRECTORY}test1.csv"
TEST2_CSV: str = f"{TEST2_DIRECTORY}test2.csv"
BUCKET: str = "your-s3-bucket"
ARN: str = "arn:aws:iam::1234567890:role/cicd-arn"
WEB_IDENTITY_TOKEN: str = get_web_identity_token()
REGION_NAME: str = "us-west-2"


@lru_cache()
def get_file_system() -> SimpleStorageService:
    return SimpleStorageService(
        BUCKET,
        root="test_file_system_client/prefix/",
        arn=ARN,
        region_name=REGION_NAME,
    )


class TestS3(unittest.TestCase):
    """
    This test case verifies s3 file system functionality when leveraging
    IAM assume-role-with-OIDC for authentication
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._csv1_bytes: Optional[bytes] = None
        self._csv2_bytes: Optional[bytes] = None
        super().__init__(*args, **kwargs)
        if not WEB_IDENTITY_TOKEN:
            print(
                "Skipping S3 OIDC authentication tests because no web "
                "identity token was found"
            )

    @classmethod
    def setUpClass(cls) -> None:
        warnings.filterwarnings("ignore", category=ResourceWarning)
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    @property  # type: ignore
    def file_system(self) -> SimpleStorageService:
        return get_file_system()

    @property  # type: ignore
    def csv1(self) -> BytesIO:
        if self._csv1_bytes is None:
            with StringIO() as string_io:
                dict_writer: csv.DictWriter = csv.DictWriter(
                    string_io, ("a", "b", "c")
                )
                dict_writer.writerow(dict(a=1, b=2, c=3))
                string_io.seek(0)
                self._csv1_bytes = bytes(string_io.read(), encoding="utf-8")
        return BytesIO(self._csv1_bytes)

    @property  # type: ignore
    def csv2(self) -> BytesIO:
        if self._csv2_bytes is None:
            with StringIO() as string_io:
                dict_writer: csv.DictWriter = csv.DictWriter(
                    string_io, ("a", "b", "c")
                )
                dict_writer.writerow(dict(a=4, b=5, c=6))
                string_io.seek(0)
                self._csv2_bytes = bytes(string_io.read(), encoding="utf-8")
        return BytesIO(self._csv2_bytes)

    def test_put_get_delete_iter(self) -> None:
        """
        Please note that these need to execute sequentially
        """
        if not WEB_IDENTITY_TOKEN:
            return
        self.file_system.clear()
        self._test_put()
        self._test_iter_file_paths()
        self._test_get()
        self._test_delete_directory()
        self._test_delete()

    def _test_put(self) -> None:
        """
        This method tests uploading a file to S3
        """
        self.file_system.put(self.csv1, TEST1_CSV)
        assert self.file_system.is_file(TEST1_CSV)
        self.file_system.put(self.csv2, TEST2_CSV)
        assert self.file_system.is_file(TEST2_CSV)

    def _test_iter_file_paths(self) -> None:
        """
        This method tests retrieving file names from S3
        """
        file_paths: Tuple[str, ...] = tuple(
            self.file_system.iter_file_paths(recursive=True)
        )
        assert len(file_paths) == 2
        file_path: str
        for file_path in file_paths:
            assert self.file_system.is_file(file_path)

    def _test_get(self) -> None:
        """
        This method tests downloading a file from S3
        """
        assert self.file_system.get(TEST1_CSV).read() == self.csv1.read()
        assert self.file_system.get(TEST2_CSV).read() == self.csv2.read()

    def _test_delete_directory(self) -> None:
        """
        This method verifies that we can successfully delete a directory.
        """
        assert self.file_system.is_directory(TEST_DIRECTORY)
        assert self.file_system.is_directory(TEST1_DIRECTORY)
        assert self.file_system.is_directory(TEST2_DIRECTORY)
        self.file_system.delete_directory(f"{TEST1_DIRECTORY}")
        assert not self.file_system.is_file(TEST1_CSV)
        assert self.file_system.is_file(TEST2_CSV)
        assert not self.file_system.is_directory(TEST1_DIRECTORY)
        assert self.file_system.is_directory(TEST2_DIRECTORY)

    def _test_delete(self) -> None:
        """
        This method verifies that we can successfully delete a file.
        """
        assert self.file_system.is_file(TEST2_CSV)
        self.file_system.delete(TEST2_CSV)
        assert not self.file_system.is_file(TEST1_CSV)

    def test_get_url(self) -> None:
        """
        This method verifies that
        `analytics_etl.file_system.s3.S3.get_url` returns
        an S3 URL formatted in the expected fashion.
        """
        if not WEB_IDENTITY_TOKEN:
            return
        url: str = self.file_system.get_url(TEST1_CSV)
        expected_url: str = (
            f"s3://{self.file_system.bucket_name}/"
            f"{self.file_system.root}{TEST1_CSV}"
        )
        assert url == expected_url, f"\n{url} !=\n{expected_url}"

    def test_date_partition(self) -> None:
        """
        This method tests use of date partitioning functionality for the
        s3 file system. CSV1 is first written to a date partition directory,
        then CSV2.
        """
        if not WEB_IDENTITY_TOKEN:
            return
        sub_directory_1: str = self.file_system.get_date_partition_directory(
            TEST_INCREMENTAL_DIRECTORY, datetime.now(), precision=7
        )
        assert is_date_partition_directory(sub_directory_1)
        test1_csv: str = f"{sub_directory_1}{os.path.basename(TEST1_CSV)}"
        self.file_system.put(self.csv1, test1_csv)
        sub_directory_2: str = self.file_system.get_date_partition_directory(
            TEST_INCREMENTAL_DIRECTORY, datetime.now(), precision=7
        )
        assert is_date_partition_directory(sub_directory_2)
        test2_csv: str = f"{sub_directory_2}{os.path.basename(TEST2_CSV)}"
        latest_directory: str = self.file_system.get_latest_directory(
            TEST_INCREMENTAL_DIRECTORY
        )
        # There shouldn't be any latest directory yet, as we haven't
        # put any success indicators in either
        assert not latest_directory
        self.file_system.put_success(sub_directory_1)
        self.file_system.put(self.csv2, test2_csv)
        latest_directory = self.file_system.get_latest_directory(
            TEST_INCREMENTAL_DIRECTORY
        )
        # Only the first sub-directory has a success indicator, so it is
        # the latest
        assert (
            latest_directory == sub_directory_1
        ), f"\n{latest_directory} !=\n{sub_directory_1}"
        # Now we indicate the second directory was successful
        self.file_system.put_success(sub_directory_2)
        latest_directory = self.file_system.get_latest_directory(
            TEST_INCREMENTAL_DIRECTORY
        )
        assert latest_directory == sub_directory_2
        latest_files: Tuple[str, ...] = tuple(
            self.file_system.iter_latest_files(TEST_INCREMENTAL_DIRECTORY)
        )
        # There should only be one file
        assert len(latest_files) == 1, latest_files
        path: str
        for path in latest_files:
            # Ensure the file we wrote to the latest directory is the only
            # file found
            assert path == test2_csv, f"\n{test2_csv} !=\n{path}"
            assert self.file_system.get(path).read() == self.csv2.read()

    def test_endpoint_url(self) -> None:
        if not WEB_IDENTITY_TOKEN:
            return
        assert not url_is_local(
            self.file_system.bucket.meta.client.meta.endpoint_url
        )

    def test_from_url(self) -> None:
        url: str = self.file_system.get_url()
        assert from_url(url).get_url() == url


if __name__ == "__main__":
    unittest.main()
