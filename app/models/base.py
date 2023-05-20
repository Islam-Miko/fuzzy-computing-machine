from datetime import datetime
from typing import Optional

from sqlalchemy import DATETIME
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class BaseAbstractModel(Base):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    created_at: Mapped[datetime] = mapped_column(
        DATETIME(True), default=datetime.now
    )
    deleted_at: Mapped[Optional[datetime]] = mapped_column(
        DATETIME(True),
    )
