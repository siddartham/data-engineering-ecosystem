import unittest
import warnings
import sys
from typing import Any
from analytics_orm.utilities import is_ci, run
from sample_snowflake2postgresql_etl.broker import Broker


class TestBroker(unittest.TestCase):
    """
    This test case verifies S3 file system functionality
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def setUp(self) -> None:
        warnings.filterwarnings("ignore", category=ResourceWarning)
        warnings.filterwarnings("ignore", category=DeprecationWarning)

    def test_etl(self) -> None:
        if not is_ci():
            # We can't run this test on Jenkins or other CI runners
            # because the NGAP platform team won't give our CI runners
            # S3 access and this can't be simulated locally because we are
            # using Aurora-specific S3 loader plugins which won't work
            # with a dockerized postgresql localstack
            run(
                (
                    f"{sys.executable}",
                    "-m",
                    "sample_snowflake2postgresql_etl",
                    "dev",
                )
            )

    def test_get_environment_postgresql_boto3_session(self) -> None:
        """
        Test our ability to assume the CI role. This test is mostly to
        ensure CI tools have proper cross-account access.
        """
        getattr(Broker("dev").work, "postgresql_boto3_session")


if __name__ == "__main__":
    unittest.main()
