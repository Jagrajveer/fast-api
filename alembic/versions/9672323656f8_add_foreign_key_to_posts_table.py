"""add foreign key to posts table

Revision ID: 9672323656f8
Revises: fd8a9973c7cb
Create Date: 2022-04-27 16:56:34.639405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9672323656f8'
down_revision = 'fd8a9973c7cb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    op.drop_column("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
