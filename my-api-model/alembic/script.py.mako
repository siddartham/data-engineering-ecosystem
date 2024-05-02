"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}
"""
${imports if imports else ""}
import sys
from alembic import op  # type: ignore
from my_api_model.dialects.postgresql import (
    create_environment,
    grant_environment_permissions
)
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
    transaction: Transaction = connection.begin()
    try:
        _attempt_upgrade()
        if "head" in sys.argv:
            create_environment(bind=bind, checkfirst=True)
        else:
            grant_environment_permissions(bind=bind)
        transaction.commit()
    except:  # noqa
        transaction.rollback()
        raise


def _attempt_downgrade() -> None:
    ${downgrades if downgrades else "pass"}


def downgrade() -> None:
    bind: Connectable = op.get_bind()
    connection: Connection = bind.connect()
    transaction: Transaction = connection.begin()
    try:
        _attempt_downgrade()
        transaction.commit()
    except:  # noqa
        transaction.rollback()
        raise
