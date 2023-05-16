from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def starter(request: Request):
    return {"msg": request.user}


@app.exception_handler(Exception)
async def handle(request: Request, exc: Exception):
    return JSONResponse(
        content=str(exc), status_code=status.HTTP_418_IM_A_TEAPOT
    )
