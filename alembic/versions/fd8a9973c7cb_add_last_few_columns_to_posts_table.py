"""add last few columns to posts table

Revision ID: fd8a9973c7cb
Revises: dff2f93cf90c
Create Date: 2022-04-27 16:42:58.803013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd8a9973c7cb'
down_revision = 'dff2f93cf90c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")))


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
