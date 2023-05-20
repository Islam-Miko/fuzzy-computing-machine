from typing import Generic, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.base import BaseAbstractModel

Model = TypeVar("Model", bound=BaseAbstractModel)


class Repository(Generic[Model]):
    def __init__(self, model: Model, session: AsyncSession):
        self.model = model
        self.session = session

    async def commit(self) -> None:
        await self.session.commit()
