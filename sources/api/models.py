from pydantic.main import BaseModel


class SimpleResponseModel(BaseModel):
    ok: bool
