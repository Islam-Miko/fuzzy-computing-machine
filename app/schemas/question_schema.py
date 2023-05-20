from typing import Optional

from pydantic import BaseModel, Field

from app.schemas.base import BaseSchema


class RequestData(BaseModel):
    question_num: int = Field(..., gt=0)


class QuestionSchema(BaseSchema):
    id: int
    question: str
    answer: str
    value: Optional[int]
