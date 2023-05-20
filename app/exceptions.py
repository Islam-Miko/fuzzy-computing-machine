from typing import ClassVar

from fastapi import HTTPException, status


class BaseAPIException(HTTPException):
    status_code: ClassVar[int]
    detail: ClassVar[str]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            status_code=self.status_code, detail=self.detail, *args, **kwargs
        )


class EmptyBodyException(BaseAPIException):
    status_code = status.HTTP_200_OK
    detail = None
