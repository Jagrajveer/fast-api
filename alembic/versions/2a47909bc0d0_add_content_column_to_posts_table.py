"""add content column to posts table

Revision ID: 2a47909bc0d0
Revises: 7da07ed76339
Create Date: 2022-04-27 16:24:17.506242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a47909bc0d0'
down_revision = '7da07ed76339'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade():
    op.drop_column("posts", "content")
