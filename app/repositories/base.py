from typing import Generic, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.base import BaseAbstractModel

Model = TypeVar("Model", bound=BaseAbstractModel)

Key = TypeVar("Key", int, str)


class Repository(Generic[Model]):
    def __init__(self, model: Model, session: AsyncSession):
        self.model = model
        self.session = session

    async def commit(self) -> None:
        await self.session.commit()

    async def get(self, id: Key) -> Model:
        stmt = select(self.model).where(
            self.model.id == id, self.model.deleted_at.is_(None)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one()
