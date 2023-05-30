from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model

class Lesson(Model):
    uuid = fields.UUIDField(pk=True)
    datetime = fields.DatetimeField()
    classroom = fields.IntField()

Lessons = pydantic_model_creator(Lesson, name="Lesson")
LessonsIn = pydantic_model_creator(Lesson, name="LessonsIn", exclude=("uuid",))
LessonPatch = pydantic_model_creator(Lesson, name="LessonPatch", optional=("datetime", "classroom"), exclude=("uuid",))