from fastapi import Depends
from sqlalchemy import exists as sql_exists
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.configs.database import get_session
from app.models.audio_data import AudioData
from app.repositories.base import Key, Repository


class AudioDataRepository(Repository[AudioData]):
    select_stmt = select(AudioData).where(AudioData.deleted_at.is_(None))

    async def check_data_exists(self, id: Key, user_id: Key) -> bool:
        result = await self.session.execute(
            sql_exists(self.model.id)
            .where(
                self.model.id == id,
                self.model.user_id == user_id,
            )
            .select()
        )
        return result.scalar_one()


def get_repository(
    session: AsyncSession = Depends(get_session),
) -> AudioDataRepository:
    return AudioDataRepository(AudioData, session)
