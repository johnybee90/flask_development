"""Create users table

Revision ID: 30eb3e7f9f18
Revises: 695655348eb3
Create Date: 2023-08-09 13:42:45.712440

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30eb3e7f9f18'
down_revision: Union[str, None] = '695655348eb3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
