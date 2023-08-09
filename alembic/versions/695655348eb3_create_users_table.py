"""Create users table

Revision ID: 695655348eb3
Revises: 384c5be19c12
Create Date: 2023-08-09 13:05:12.075599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '695655348eb3'
down_revision: Union[str, None] = '384c5be19c12'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
