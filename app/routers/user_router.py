from fastapi import APIRouter, Depends

from app.schemas.user_schema import CreateSchema, ResponseSchema
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["user"])


@router.post("/", response_model=ResponseSchema)
async def create_user(data: CreateSchema, service: UserService = Depends()):
    id_ = await service.create(data)
    return await service.get(id_)
