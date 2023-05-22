import pydantic
from tortoise import fields
from tortoise.models import Model

@pydantic.dataclasses.dataclass
class Lesson(Model):
    uuid = fields.UUIDField(pk=True)
    datetime = fields.DatetimeField()
    classroom = fields.IntField()
    