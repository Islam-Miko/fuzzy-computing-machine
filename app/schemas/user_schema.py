from pydantic import UUID4

from app.schemas.base import BaseSchema


class CreateSchema(BaseSchema):
    name: str


class UserSchema(BaseSchema):
    id: UUID4
    token: UUID4
