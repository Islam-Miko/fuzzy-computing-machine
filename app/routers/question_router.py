from fastapi import APIRouter, Depends

from app.schemas.question_schema import RequestData
from app.services.question_service import QuestionService
from app.worker import queue

router = APIRouter(prefix="/questions", tags=["question"])


@router.post("/")
async def save_questions(
    data: RequestData, service: QuestionService = Depends()
):
    last_question = await service.get_last_question()
    await queue.enqueue("save_questions", count=data.question_num)
    return last_question
