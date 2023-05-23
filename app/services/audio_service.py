from fastapi import Depends, concurrency

from app.exceptions import FileDoesNotExist
from app.repositories.audio_data_repository import (
    AudioDataRepository,
    get_repository,
)
from app.schemas.audio_schema import AudioAddSchema
from app.utils import convert_to_mp3, generate_download_url


class AudioDataService:
    def __init__(
        self, repo: AudioDataRepository = Depends(get_repository)
    ) -> None:
        self.repository = repo

    async def check_exists_file(self, file_id: str, user_id: str) -> None:
        exists = await self.repository.check_data_exists(file_id, user_id)
        if not exists:
            raise FileDoesNotExist()

    async def store_file(self, data: AudioAddSchema) -> str:
        key = await self.repository.create(dict(user_id=data.id))
        await self.repository.commit()
        await concurrency.run_in_threadpool(
            convert_to_mp3, str(key), data.audio_file
        )
        return generate_download_url(data.id, str(key))
