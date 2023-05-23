from typing import Mapping

from fastapi import Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.configs.database import get_session
from app.models.users import User
from app.repositories.base import Key, Repository


class UserRepository(Repository[User]):
    select_stmt = select(User).where(User.deleted_at.is_(None))

    async def create(self, data: Mapping) -> Key:
        stmt = insert(self.model).values(data).returning(self.model.id)
        result = await self.session.execute(stmt)
        return result.scalar_one()


def get_repository(
    session: AsyncSession = Depends(get_session),
) -> UserRepository:
    return UserRepository(User, session)
