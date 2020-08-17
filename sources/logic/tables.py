from tortoise import Model, fields

from logic.constants import CargoTypes


class Rate(Model):
    id = fields.IntField(pk=True)
    start_date = fields.DateField()
    cargo_type = fields.CharEnumField(CargoTypes)
    value = fields.FloatField()
