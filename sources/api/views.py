from typing import List, Dict

from fastapi import HTTPException

from logic.cases import load_tariff, get_insurance_price
from logic.errors import LogicError
from logic.models import RateModel, CargoInfoModel


async def load_tariff_view(tariff: Dict[str, List[RateModel]]):
    await load_tariff(tariff)

    return {
        "loaded": True
    }


async def get_insurance_price_view(cargo_info: CargoInfoModel):
    try:
        price = await get_insurance_price(cargo_info)
    except LogicError as err:
        raise HTTPException(status_code=400, detail={
            "error_code": err.error_code.value,
            "data": err.data,
        })

    return {
        "price": price
    }
