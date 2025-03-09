"""initial migration2

Revision ID: 723449642f69
Revises: 68a6b80f3dfe
Create Date: 2025-03-09 03:20:51.575964

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '723449642f69'
down_revision: Union[str, None] = '68a6b80f3dfe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
