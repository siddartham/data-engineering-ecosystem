import unittest
import warnings
from datetime import datetime
from typing import Any, Tuple

from mail_client.smtp import send


PASSWORD_CERBERUS_PATHS: Tuple[str, str, str] = (
    "app/sustainability/bmx/a.BMX.SUSTAINABILITY",
    "app/sustainability/ngap/a.NGAP.SE",
    "app/sustainability/ngap/a.NGAP.SE",
    # "app/sustainability/ngap/a.NGAP.SE.NP",
)


class TestMain(unittest.TestCase):
    """
    This test case verifies S3 file system functionality
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def setUp(self) -> None:
        warnings.filterwarnings("ignore", category=ResourceWarning)
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        warnings.filterwarnings("ignore", category=FutureWarning)

    def test_01_send_no_recipients(self) -> None:
        password_cerberus_path: str
        for password_cerberus_path in PASSWORD_CERBERUS_PATHS:
            send(
                password_cerberus_path=password_cerberus_path,
                subject="Unit Test #1 for mail-client",
                body=(
                    "Successful test run completed on: "
                    f"{datetime.now().isoformat()}."
                ),
            )

    def test_02_send_to_cc_bcc(self) -> None:
        # password_cerberus_path: str
        to: str
        cc: str
        bcc: str
        # path: str
        to, cc, bcc = (
            f"{path.split('/')[-1].lower()}@my.com"
            for path in PASSWORD_CERBERUS_PATHS
        )
        send(
            to=to,
            cc=cc,
            bcc=bcc,
            password_cerberus_path=PASSWORD_CERBERUS_PATHS[0],
            subject="Unit Test #2 for mail-client",
            body=(
                "Successful test run completed on: "
                f"{datetime.now().isoformat()}."
            ),
        )


if __name__ == "__main__":
    unittest.main()
