"""add user table

Revision ID: 1555ba2379ab
Revises: 514e243b984a
Create Date: 2023-05-22 18:15:39.440510

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "1555ba2379ab"
down_revision = "514e243b984a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

    op.create_table(
        "users",
        sa.Column("id", sa.UUID, server_default=sa.text("uuid_generate_v4()")),
        sa.PrimaryKeyConstraint("id"),
        sa.Column(
            "created_at", sa.DateTime(True), server_default=sa.text("now()")
        ),
        sa.Column("deleted_at", sa.DateTime(True), nullable=True),
        sa.Column(
            "token",
            sa.UUID,
            server_default=sa.text("uuid_generate_v4()"),
            unique=True,
        ),
        sa.Column("name", sa.String(25), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
    op.execute('DROP EXTENSION IF EXISTS "uuid-ossp";')
