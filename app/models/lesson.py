from tortoise import fields
from tortoise.models import Model


class Lesson(Model):
    uuid = fields.UUIDField(pk=True)
    datetime = fields.DatetimeField()
    name = fields.TextField()
    classroom = fields.IntField()