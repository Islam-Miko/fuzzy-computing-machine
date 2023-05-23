import uuid

from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseAbstractModel


class AudioData(BaseAbstractModel):
    __tablename__ = "audio_data"

    id: Mapped[str] = mapped_column(
        UUID(True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[str] = mapped_column(
        UUID, ForeignKey("users.id"), index=True
    )
