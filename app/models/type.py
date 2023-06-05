from uuid import UUID
from pydantic import BaseModel
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator

class Type(Model):
    uuid = fields.UUIDField(pk=True)
    name = fields.TextField()
    active = fields.BooleanField(default=True)

class TypesOut(BaseModel):
    uuid: UUID
    name: str
    active: bool
    
Types = pydantic_model_creator(Type, name= "Type")
TypesIn = pydantic_model_creator(Type, name= "TypesIn", exclude=("uuid",))
TypesPatch = pydantic_model_creator(Type, name= "TypesPatch", optional=("name", "active"), exclude=("uuid",))
