from analytics_orm import sqlite

from ..base import Base


def main() -> None:
    """
    This function is the entry point for the
    `my-api-model sqlite` command.
    Execute `my-api-model sqlite -h` for information
    about his command.
    """
    sqlite.main(Base, "my-api-model sqlite")
