import uuid

from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseAbstractModel


class User(BaseAbstractModel):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        UUID(True), primary_key=True, default=uuid.uuid4
    )
    token: Mapped[str] = mapped_column(
        UUID(True),
        index=True,
        default=uuid.uuid4,
        unique=True,
    )
    name: Mapped[str] = mapped_column(String(25))
