from typing import Mapping, Union

from fastapi import Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.configs.database import get_session
from app.models.questions import Question
from app.repositories.base import Key, Repository


class QuestionRepository(Repository[Question]):
    select_stmt = select(Question).where(Question.deleted_at.is_(None))

    async def get_last_question(self) -> Union[Question, None]:
        stmt = self.select_stmt.order_by(Question.created_at.desc()).limit(1)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def exists(self, *clauses) -> bool:
        stmt = self.select_stmt.where(*clauses).exists().select()
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def create(self, data: Mapping) -> Key:
        stmt = insert(Question).values(data).returning(Question.id)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def pk_exists(self, pk: Key) -> bool:
        return await self.exists(Question.id == pk)


def get_repository(
    session: AsyncSession = Depends(get_session),
) -> QuestionRepository:
    return QuestionRepository(Question, session)
