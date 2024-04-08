import functools
import logging
from itertools import chain
from smtplib import SMTP
from typing import Any, Callable, Iterable, List, Tuple, Union
from cerberus_assistant.get import get_secret

lru_cache: Callable[..., Any] = functools.lru_cache
SMTP_HOST: str = "smtp.office365.com"
SMTP_PORT: int = 587


def _format_message(
    to: Tuple[str, ...],
    cc: Tuple[str, ...],
    bcc: Tuple[str, ...],
    from_: str,
    reply_to: str,
    subject: str,
    body: str,
    content_type: str,
) -> str:
    return (
        "From: {from_}\n"
        "To: {to}\n"
        "Reply-to: {reply_to}\n"
        "Subject: {subject}\n"
        "Content-type: {content_type}\n"
        "{cc}"
        "{bcc}"
        "\n"
        "{body}"
    ).format(
        from_=from_,
        to=", ".join(to),
        reply_to=reply_to,
        subject=subject,
        content_type=content_type,
        cc=f"Cc: {','.join(cc)}\n" if cc else "",
        bcc=f"Bcc: {','.join(bcc)}\n" if bcc else "",
        body=body,
    )


@lru_cache()
def login(user: str = "", password: str = "") -> SMTP:
    smtp: SMTP = SMTP(host=SMTP_HOST, port=SMTP_PORT)
    smtp.starttls()
    smtp.ehlo_or_helo_if_needed()
    smtp.login(user, password)
    return smtp


def _iter_recipient_tuples(
    *recipient_iterables: Union[str, Iterable[str]]
) -> Iterable[Tuple[str, ...]]:
    recipients: Union[str, Iterable[str]]
    for recipients in recipient_iterables:
        if recipients:
            if isinstance(recipients, str):
                yield (recipients,)
            elif isinstance(recipients, tuple):
                yield recipients
            else:
                yield tuple(recipients)
        else:
            yield ()


def _get_recipient_tuples(
    *recipient_iterables: Union[str, Iterable[str]]
) -> Tuple[Tuple[str, ...], ...]:
    recipient_tuples: Tuple[Tuple[str, ...], ...] = tuple(
        _iter_recipient_tuples(*recipient_iterables)
    )
    return (tuple(chain(*recipient_tuples)),) + recipient_tuples


def send(
    to: Union[str, Iterable[str]] = (),
    cc: Union[str, Iterable[str]] = (),
    bcc: Union[str, Iterable[str]] = (),
    from_: str = "",
    reply_to: str = "",
    user: str = "",
    password: str = "",
    password_cerberus_path: str = "",
    subject: str = "",
    content_type: str = "text/plain; charset=UTF-8",
    body: str = "",
) -> None:
    """
    This function sends an email using the SMTP protocol. If authentication
    is required, either a `user` and `password` must be provided, or
    a `password_cerberus_path`, which will cause a username and password
    to be retrieved from one of MY Cerberus vaults.

    Parameters:

    - to (str|[str]):
      A list of recipients to include in the "To:" header of this message
    - cc (str|[str]):
      A list of recipients to include in the "Cc:" header of this message
    - bcc (str):
      A list of recipients to include in the "Bcc:" header of this message.
      header of this message
    - from_ (str):
      An email address to use in the "From:" header of this message
    - reply_to (str):
      An email address to use in the "Reply-to:" header of this message
    - user (str): A username with which to authenticate. Note:
      If providing a `password_cerberus_path` where the username
      is the secret key, and the secret key is appended to the path
      provided in the `password_cerberus_path`, this can be left out.
      If providing a `password_cerberus_path` *without* a secret key
      appended to the path, the `user` will be inferred to be the
      secret key.
    - password (str): A password with which to authenticate (this is not
      needed if providing a `password_cerberus_path`)
    - password_cerberus_path (str):
      The path to a password stored in a MY Cerberus vault with which to
      authenticate
    - subject (str): A subject header for this message
    - body (str): The body of the message

    Returns: `None` if successful, or raises an exception if errors occur.
    """
    recipients: Tuple[str, ...]
    recipients, to, cc, bcc = _get_recipient_tuples(to, cc, bcc)
    if not (user and password):
        path_parts: List[str] = password_cerberus_path.strip(" /").split("/")
        key: str = user
        if len(path_parts) > 3:
            user = path_parts[-1]
            user = user or key
        password = get_secret(password_cerberus_path)
    if "@" not in user:
        user = f"{user.lower()}@my.com"
    from_ = from_ or user
    reply_to = reply_to or from_
    if not recipients:
        to = recipients = (from_,)
    smtp: SMTP = login(user, password)
    message: str = _format_message(
        to=to,
        cc=cc,
        bcc=bcc,
        from_=from_,
        reply_to=reply_to,
        subject=subject,
        content_type=content_type,
        body=body,
    )
    logging.info(message)
    smtp.sendmail(from_, recipients, message)
