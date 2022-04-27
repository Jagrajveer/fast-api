"""create posts table

Revision ID: 7da07ed76339
Revises: 
Create Date: 2022-04-27 16:16:20.325685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7da07ed76339'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True), sa.Column("title", sa.String(), nullable=False))


def downgrade():
    op.drop_table("posts")
