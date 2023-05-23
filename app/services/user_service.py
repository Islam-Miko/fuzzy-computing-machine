from fastapi import Depends

from app.models.users import User
from app.repositories.user_repository import UserRepository, get_repository
from app.schemas.user_schema import CreateSchema


class UserService:
    def __init__(self, repo: UserRepository = Depends(get_repository)) -> None:
        self.repository = repo

    async def create(self, data: CreateSchema) -> str:
        try:
            instance_key = await self.repository.create(data.dict())
        except Exception:
            pass
        else:
            await self.repository.commit()
            return instance_key

    async def get(self, id: str) -> User:
        return await self.repository.get(id)
