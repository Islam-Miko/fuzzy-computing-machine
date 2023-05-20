from fastapi import Depends

from app.repositories.question_repository import (
    QuestionRepository,
    get_repository,
)
from app.schemas.question_schema import QuestionSchema


class QuestionService:
    def __init__(
        self, repo: QuestionRepository = Depends(get_repository)
    ) -> None:
        self.repository = repo

    async def get_last_question(self) -> dict:
        instance = await self.repository.get_last_question()
        if instance is None:
            return dict()
        return QuestionSchema.from_orm(instance).dict()
