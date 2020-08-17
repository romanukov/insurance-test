import datetime

from pydantic.main import BaseModel

from logic.constants import CargoTypes


class RateModel(BaseModel):
    cargo_type: CargoTypes
    rate: float


class CargoInfoModel(BaseModel):
    cargo_type: CargoTypes
    date: datetime.date
    declared_value: float
