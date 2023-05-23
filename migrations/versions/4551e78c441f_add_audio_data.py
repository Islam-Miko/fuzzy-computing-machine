"""add audio data

Revision ID: 4551e78c441f
Revises: 1555ba2379ab
Create Date: 2023-05-23 18:20:41.086029

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "4551e78c441f"
down_revision = "1555ba2379ab"
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table(
        "audio_data",
        sa.Column("id", sa.UUID, server_default=sa.text("uuid_generate_v4()")),
        sa.PrimaryKeyConstraint("id"),
        sa.Column(
            "created_at", sa.DateTime(True), server_default=sa.text("now()")
        ),
        sa.Column("deleted_at", sa.DateTime(True), nullable=True),
        sa.Column("user_id", sa.UUID, sa.ForeignKey("users.id"), index=True),
    )


def downgrade() -> None:
    op.drop_table("audio_data")
