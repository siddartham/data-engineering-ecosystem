import argparse

from .smtp import send


def main() -> None:
    """
    This function is the entry point for using this script as a CLI.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        usage="mail-client send [optional arguments]"
    )
    parser.add_argument(
        "--to",
        "-to",
        type=str,
        action="append",
        default=[],
        help=(
            '\na comma-separated list of recipients to include in the "to" '
            "header for this message"
        ),
    )
    parser.add_argument(
        "--cc",
        "-cc",
        type=str,
        action="append",
        default=[],
        help=(
            '\na comma-separated list of recipients to include in the "cc" '
            "header for this message"
        ),
    )
    parser.add_argument(
        "--bcc",
        "-bcc",
        type=str,
        action="append",
        default=[],
        help=(
            '\na comma-separated list of recipients to include in the "bcc" '
            "header for this message"
        ),
    )
    parser.add_argument(
        "--from",
        "-f",
        type=str,
        default=[],
        help='\na "from" header for this message',
    )
    parser.add_argument(
        "--reply-to",
        "-rt",
        type=str,
        default="",
        help='\na "reply-to" header for this message',
    )
    parser.add_argument(
        "--user",
        "-u",
        type=str,
        default="",
        help=(
            "\na username with which to authenticate "
            "\nNote: "
            "\nif providing a PASSWORD_CERBERUS_PATH where the username "
            "is the secret key, and the secret key is appended to the path "
            "provided in the PASSWORD_CERBERUS_PATH, this can be left out"
            "\nif providing a PASSWORD_CERBERUS_PATH *without* a secret key "
            "appended to the path, the USER will be inferred to be the "
            "secret key"
        ),
    )
    parser.add_argument(
        "--password",
        "-p",
        type=str,
        default="",
        help=(
            "\na password with which to authenticate "
            "(this is not needed if providing a PASSWORD_CERBERUS_PATH)"
        ),
    )
    parser.add_argument(
        "--password-cerberus-path",
        "-pcp",
        type=str,
        default="",
        help=(
            "\nthe path to a password stored in a My Cerberus vault "
            "with which to authenticate"
        ),
    )
    parser.add_argument(
        "--subject",
        "-s",
        type=str,
        default="",
        help="\na subject header for this message",
    )
    parser.add_argument(
        "--body",
        "-b",
        type=str,
        default="",
        help="The body of the message",
    )
    arguments: argparse.Namespace = parser.parse_args()
    send(
        to=arguments.to,
        cc=arguments.cc,
        bcc=arguments.bcc,
        from_=getattr(arguments, "from"),
        reply_to=arguments.reply_to,
        user=arguments.user,
        password=arguments.password,
        password_cerberus_path=arguments.password_cerberus_path,
        subject=arguments.subject,
        body=arguments.body,
    )


if __name__ == "__main__":
    main()
