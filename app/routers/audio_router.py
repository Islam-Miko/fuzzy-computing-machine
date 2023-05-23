from fastapi import APIRouter, Body, Depends, UploadFile
from fastapi.responses import FileResponse
from pydantic import UUID4

from app.schemas.audio_schema import AudioAddSchema, ResponseSchema
from app.services.audio_service import AudioDataService
from app.utils import generate_filename

router = APIRouter(prefix="/audios", tags=["audio"])
download_router = APIRouter(tags=["audio"])


@router.post("/", response_model=ResponseSchema)
async def add_audio_file(
    audio_file: UploadFile,
    id: UUID4 = Body(...),
    token: UUID4 = Body(...),
    service: AudioDataService = Depends(),
):
    download_url = await service.store_file(
        AudioAddSchema(id=id, token=token, audio_file=audio_file)
    )
    return ResponseSchema(download_url=download_url)


@download_router.get("/record")
async def return_file(
    id: str, user: str, service: AudioDataService = Depends()
):
    await service.check_exists_file(id, user)
    return FileResponse(generate_filename(id))
