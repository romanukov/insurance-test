import enum


class CargoTypes(enum.Enum):
    GLASS = 'Glass'
    OTHER = 'Other'


class ErrorCodes(enum.Enum):
    TARIFF_FOR_THIS_DATE_IS_NOT_DEFINED = 'tariff_for_this_date_is_not_defined'
