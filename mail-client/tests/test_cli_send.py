import unittest
import warnings
from datetime import datetime
from subprocess import getstatusoutput
from typing import Any, Tuple


PASSWORD_CERBERUS_PATHS: Tuple[str, str, str] = (
    "app/sustainability/bmx/a.BMX.SUSTAINABILITY",
    "app/sustainability/ngap/a.NGAP.SE",
    "app/sustainability/ngap/a.NGAP.SE",
    # "app/sustainability/ngap/a.NGAP.SE.NP",
)


def run(command: str) -> str:
    """
    This function runs a shell command, raises an error if a non-zero
    exit code is returned, and echo's both the command and output *if*
    the `echo` parameter is `True`.

    Parameters:

    - command (str): A shell command
    """
    status: int
    output: str
    status, output = getstatusoutput(command)
    # Raise an error if a non-zero exit status is returned
    if status:
        raise OSError(output)
    else:
        output = output.strip()
        print(output)
    return output


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
            run(
                "mail-client send "
                f"-pcp {password_cerberus_path} "
                "-s 'Unit Test #1 for mail-client CLI' "
                f"-b 'Successful test run completed on: "
                f"{datetime.now().isoformat()}.' "
            )

    def test_02_send_to_cc_bcc(self) -> None:
        to: str
        cc: str
        bcc: str
        path: str
        to, cc, bcc = (
            f"{path.split('/')[-1].lower()}@my.com"
            for path in PASSWORD_CERBERUS_PATHS
        )
        run(
            "mail-client send "
            f"-to {to} "
            f"-cc {cc} "
            f"-bcc {bcc} "
            f"-pcp {PASSWORD_CERBERUS_PATHS[0]} "
            "-s 'Unit Test #2 for mail-client CLI' "
            f"-b 'Successful test run completed on: "
            f"{datetime.now().isoformat()}.' "
        )


if __name__ == "__main__":
    unittest.main()
