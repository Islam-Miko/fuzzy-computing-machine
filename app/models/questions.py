from typing import Optional

from sqlalchemy import BigInteger, SmallInteger, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseAbstractModel


class Question(BaseAbstractModel):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=False
    )
    question: Mapped[str] = mapped_column(Text)
    answer: Mapped[str] = mapped_column(Text)
    value: Mapped[Optional[int]] = mapped_column(SmallInteger)
