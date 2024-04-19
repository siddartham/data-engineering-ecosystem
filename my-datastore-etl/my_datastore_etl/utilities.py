import functools
import os
from getpass import getuser
from smtplib import SMTPException
from subprocess import CalledProcessError, check_output
from typing import Any, Callable, Tuple

from analytics_etl.utilities import retry
from mail_client.smtp import send

lru_cache: Callable[..., Any] = functools.lru_cache
SMTP_USER: str = "a.NGAP.SE"


def _get_environment_alert_email_user(environment: str) -> str:
    user: str = "a.NGAP.SE"
    if not environment.lower().endswith("prod"):
        user = f"{user}.NP"
    return user


def _get_user_email(user: str = "") -> str:
    user = user or getuser()
    line: str
    try:
        return (
            next(
                filter(
                    lambda line: line.startswith("mail:"),
                    check_output(
                        (
                            "ldapsearch",
                            "-H",
                            "ldap://ad.org.com",
                            "-b",
                            "DC=ad,DC=org,DC=com",
                            f"(&(objectClass=person)(sAMAccountName={user}))",
                            "mail",
                        ),
                        encoding="utf-8",
                        universal_newlines=True,
                    )
                    .strip()
                    .split("\n"),
                )
            )
            .rpartition("mail:")[-1]
            .strip()
        )
    except (StopIteration, CalledProcessError, FileNotFoundError):
        return ""


def get_commit_author_email(commit: str = "") -> str:
    email_address: str = ""
    try:
        email_address = check_output(
            ("git", "--no-pager", "show", "-s", "--format=%ae") + ((commit,)),
            encoding="utf-8",
            universal_newlines=True,
        ).strip()
    except Exception:
        pass
    if (not email_address) or email_address.lower() == "nobody@nowhere":
        email_address = os.environ.get("CHANGE_AUTHOR_EMAIL", "")
    return email_address


def _get_environment_alert_email_to(environment: str) -> Tuple[str, ...]:
    assert environment  # For forwards compatibility
    if environment.lower().endswith("prod"):
        return ("reddy.siddartha53@gmail.com",)
    else:
        email_address: str = _get_user_email() or get_commit_author_email()
        if email_address:
            return (email_address,)
        else:
            return (
                f"{_get_environment_alert_email_user(environment)}@siddartha.com",
                "jenkins@siddartha.com",
            )


@retry((SMTPException,), number_of_attempts=6)
def alert(environment: str, subject: str, body: str) -> None:
    """
    Email an alert to the current user's email address if running locally, or
    the Jenkins email or
    """
    send(
        to=_get_environment_alert_email_to(environment),
        password_cerberus_path=f"app/siddartham/{SMTP_USER}",
        subject=subject,
        body=body,
    )
