"""create question table

Revision ID: 514e243b984a
Revises: 
Create Date: 2023-05-20 16:01:14.651761

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "514e243b984a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "questions",
        sa.Column("id", sa.BigInteger, autoincrement=False),
        sa.PrimaryKeyConstraint("id"),
        sa.Column(
            "created_at", sa.DateTime(True), server_default=sa.text("now()")
        ),
        sa.Column("deleted_at", sa.DateTime(True), nullable=True),
        sa.Column("question", sa.Text, nullable=False),
        sa.Column("answer", sa.Text, nullable=False),
        sa.Column("value", sa.SmallInteger, nullable=True),
    )


def downgrade() -> None:
    op.drop_table("questions")
