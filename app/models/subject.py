from uuid import UUID
from pydantic import BaseModel
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator
from app.models.lesson import LessonsOut
from app.models.type import TypesOut

class Subject(Model):
    uuid = fields.UUIDField(pk=True)
    name = fields.TextField()
    lesson = fields.ForeignKeyField('models.Lesson', related_name='subjects_lesson')
    type = fields.ForeignKeyField('models.Type', related_name='subjects_type')
    active = fields.BooleanField(default=True)

class SubjectsIn(BaseModel):
    name: str
    lesson_id: UUID
    type_id: UUID

class SubjectsOut(BaseModel):
    uuid: str
    name: str
    lesson: LessonsOut
    type: TypesOut
    active: bool

Subjects = pydantic_model_creator(Subject, name= "Subject")
# SubjectsIn = pydantic_model_creator(Subject, name= "SubjectsIn", exclude=("uuid",))
SubjectsPatch = pydantic_model_creator(Subject, name= "SubjectsPatch", optional=("name", "lesson", "type", "active"), exclude=("uuid",))
