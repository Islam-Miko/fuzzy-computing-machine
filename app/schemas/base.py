from datetime import datetime

from pydantic import BaseModel, root_validator


class BaseSchema(BaseModel):
    class Config:
        orm_mode = True

    @root_validator()
    def set_null_microseconds(cls, data: dict) -> dict:
        """Drops microseconds in all the datetime field values."""
        datetime_fields = {
            k: v.replace(microsecond=0)
            for k, v in data.items()
            if isinstance(k, datetime)
        }

        return {**data, **datetime_fields}
