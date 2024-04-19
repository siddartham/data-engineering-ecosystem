"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}
"""
${imports if imports else ""}
from typing import Optional
from alembic import op  # type: ignore
from sqlalchemy.engine import (  # type: ignore
    Connectable,
    Connection,
    Transaction,
)

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def _attempt_upgrade() -> None:
    ${upgrades if upgrades else "pass"}


def upgrade() -> None:
    bind: Connectable = op.get_bind()
    connection: Connection = bind.connect()
    transaction: Optional[Transaction] = getattr(
        connection, "begin", lambda: None
    )()
    try:
        _attempt_upgrade()
        if transaction is not None:
            transaction.commit()
    except Exception:
        if transaction is not None:
            transaction.rollback()
        raise


def _attempt_downgrade() -> None:
    ${downgrades if downgrades else "pass"}


def downgrade() -> None:
    bind: Connectable = op.get_bind()
    connection: Connection = bind.connect()
    transaction: Optional[Transaction] = getattr(
        connection, "begin", lambda: None
    )()
    try:
        _attempt_downgrade()
        if transaction is not None:
            transaction.commit()
    except Exception:
        if transaction is not None:
            transaction.rollback()
        raise
