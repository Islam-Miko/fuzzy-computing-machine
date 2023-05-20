import asyncio

import httpx

from app.configs.settings import get_settings
from app.repositories.question_repository import (
    QuestionRepository,
    get_repository,
)
from app.schemas.question_schema import QuestionSchema

Settings = get_settings()


async def get_questions(count: int) -> list[dict]:
    async with httpx.AsyncClient() as client:
        response = await client.get(Settings.JSERVICE, params={"count": count})
        return response.json()


async def store_question(repository: QuestionRepository, data: dict) -> None:
    while True:
        question = QuestionSchema(**data)
        exists = await repository.pk_exists(question.id)
        if not exists:
            break
        data = await get_questions(1)[0]
        await asyncio.sleep(3.0)

    await repository.create(question.dict())
    await repository.commit()


async def save_questions(ctx, count: int) -> None:
    repository = get_repository(ctx["session"])
    questions = await get_questions(count)
    for question in questions:
        await store_question(repository, question)
