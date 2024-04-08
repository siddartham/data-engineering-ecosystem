import unittest

from my_datastore_etl_wrapper.utilities import alert


class TestAlert(unittest.TestCase):
    """
    Test the alert utility
    """

    def test_alert(self) -> None:
        alert(
            environment="dev", subject="Test Alert", body="This is only a test"
        )


if __name__ == "__main__":
    unittest.main()
