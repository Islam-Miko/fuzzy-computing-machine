from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.configs.settings import AUDIO_DIR
from app.exceptions import BaseAPIException
from app.routers import audio_router, question_router, user_router
from app.worker import queue

app = FastAPI()

app.include_router(question_router.router, prefix="/api/v1")
app.include_router(user_router.router, prefix="/api/v1")
app.include_router(audio_router.router, prefix="/api/v1")
app.include_router(audio_router.download_router)


@app.get("/")
async def starter(request: Request):
    await queue.enqueue("example")
    return {"msg": "hi"}


@app.on_event("startup")
async def startup_event():
    if not AUDIO_DIR.exists():
        AUDIO_DIR.mkdir()


@app.exception_handler(BaseAPIException)
async def handle_http_exception(request: Request, exc: BaseAPIException):
    return JSONResponse(content=exc.detail, status_code=exc.status_code)


@app.exception_handler(Exception)
async def handle(request: Request, exc: Exception):
    return JSONResponse(
        content={"detail": "Error"}, status_code=status.HTTP_418_IM_A_TEAPOT
    )
