from tortoise import fields
from tortoise.models import Model


class Subject(Model):
    uuid = fields.UUIDField(pk=True)
    name = fields.TextField()
    lesson = fields.ForeignKeyField('models.Lesson', related_name='contents')
