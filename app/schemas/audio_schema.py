from fastapi import UploadFile
from pydantic import UUID4, HttpUrl

from app.schemas.base import BaseSchema


class AudioAddSchema(BaseSchema):
    id: UUID4
    token: UUID4
    audio_file: UploadFile


class ResponseSchema(BaseSchema):
    download_url: HttpUrl
