"""create user table

Revision ID: 6d3d90ce93f2
Revises: 
Create Date: 2026-04-19 13:18:28.305267

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d3d90ce93f2'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        email VRCHAR(255) UNIQUE NOT NULL,
        hashed_password VARCHAR(255) NOT NULL 
    );
    """)


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP TABLE users IF EXISTS")
