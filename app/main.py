from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.worker import queue

app = FastAPI()


@app.get("/")
async def starter(request: Request):
    await queue.enqueue("example")
    return {"msg": "hi"}


@app.exception_handler(Exception)
async def handle(request: Request, exc: Exception):
    return JSONResponse(
        content=str(exc), status_code=status.HTTP_418_IM_A_TEAPOT
    )
