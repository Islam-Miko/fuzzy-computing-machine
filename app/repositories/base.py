from typing import Generic, Mapping, TypeVar

from sqlalchemy import exists as sql_exists
from sqlalchemy import insert, select
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

    async def create(self, data: Mapping) -> Key:
        stmt = insert(self.model).values(data).returning(self.model.id)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def check_id_exists(self, id: Key) -> bool:
        result = await self.session.execute(
            sql_exists(self.model.id).where(self.model.id == id).select()
        )
        return result.scalar_one()
