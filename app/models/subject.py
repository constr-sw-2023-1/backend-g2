from pydantic import BaseModel
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator

class Subject(Model):
    uuid = fields.UUIDField(pk=True)
    name = fields.TextField()
    lesson = fields.ForeignKeyField('models.Lesson', related_name='subjects')
    type = fields.ForeignKeyField('models.Type', related_name='subjects')

class SubjectsIn(BaseModel):
    name: str
    lesson_id: str
    type_id: str

Subjects = pydantic_model_creator(Subject, name= "Subject")
# SubjectsIn = pydantic_model_creator(Subject, name= "SubjectsIn", exclude=("uuid",))
SubjectsPatch = pydantic_model_creator(Subject, name= "SubjectsPatch", optional=("name", "lesson", "type"), exclude=("uuid",))