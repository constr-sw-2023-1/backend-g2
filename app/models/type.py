from tortoise import fields
from tortoise.models import Model


class Type(Model):
    uuid = fields.UUIDField(pk=True)
    name = fields.TextField()
    