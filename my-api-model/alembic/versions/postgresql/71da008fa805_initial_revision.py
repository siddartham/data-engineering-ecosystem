"""initial revision

Revision ID: 71da008fa805
Revises:
Create Date: 2023-05-07 13:17:24.952431
"""

import sys

from alembic import op  # type: ignore
from sqlalchemy.engine import Connection, Transaction  # type: ignore

from my_api_model.dialects.postgresql import (
    create_environment,
    grant_environment_permissions,
)

# revision identifiers, used by Alembic.
revision = "6b19e298affb"
down_revision = None
branch_labels = None
depends_on = None


def _attempt_upgrade() -> None:
    pass


def upgrade() -> None:
    connection: Connection = op.get_bind()
    transaction: Transaction = connection.begin()
    try:
        _attempt_upgrade()
        if "head" in sys.argv:
            create_environment(checkfirst=True)
        else:
            grant_environment_permissions()
        transaction.commit()
    except:  # noqa
        transaction.rollback()
        raise


def _attempt_downgrade() -> None:
    pass


def downgrade() -> None:
    connection: Connection = op.get_bind()
    transaction: Transaction = connection.begin()
    try:
        _attempt_downgrade()
        transaction.commit()
    except:  # noqa
        transaction.rollback()
        raise
