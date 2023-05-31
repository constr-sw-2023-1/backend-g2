from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator

class Lesson(Model):
    uuid = fields.UUIDField(pk=True)
    datetime = fields.DatetimeField()
    classroom = fields.IntField()
    active = fields.BooleanField(default=True)

Lessons = pydantic_model_creator(Lesson, name="Lesson")
LessonsIn = pydantic_model_creator(Lesson, name="LessonsIn", exclude=("uuid",))
LessonPatch = pydantic_model_creator(Lesson, name="LessonPatch", optional=("datetime", "classroom", "active"), exclude=("uuid",))
