"""Create users table

Revision ID: 637bbaa3b73d
Revises: 30eb3e7f9f18
Create Date: 2023-08-09 15:53:48.308721

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '637bbaa3b73d'
down_revision: Union[str, None] = '30eb3e7f9f18'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
