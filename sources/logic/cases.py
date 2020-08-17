import datetime
from typing import Dict, List

from logic.constants import ErrorCodes
from logic.errors import LogicError
from logic.models import RateModel, CargoInfoModel
from logic.tables import Rate


async def load_tariff(tariff: Dict[str, List[RateModel]]):
    await Rate.all().delete()  # Очищаем БД от старых тарифов

    for date_string, rate_list in tariff.items():
        date = datetime.date.fromisoformat(date_string)

        for rate in rate_list:
            rate = Rate(start_date=date, cargo_type=rate.cargo_type,
                        value=rate.rate)

            await rate.save()


async def get_insurance_price(cargo_info: CargoInfoModel) -> float:
    rates = await Rate\
        .filter(cargo_type=cargo_info.cargo_type)\
        .filter(start_date__lte=cargo_info.date)

    if len(rates) == 0:
        raise LogicError(ErrorCodes.TARIFF_FOR_THIS_DATE_IS_NOT_DEFINED)

    rate_with_latest_date = rates[0]
    for rate in rates:
        if rate.start_date > rate_with_latest_date.start_date:
            rate_with_latest_date = rate

    return cargo_info.declared_value * rate_with_latest_date.value



