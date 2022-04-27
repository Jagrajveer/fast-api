"""add user table

Revision ID: dff2f93cf90c
Revises: 2a47909bc0d0
Create Date: 2022-04-27 16:38:28.506479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dff2f93cf90c'
down_revision = '2a47909bc0d0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email")
    )

def downgrade():
    op.drop_table("users")
