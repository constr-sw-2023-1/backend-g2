"""This is the subject module, this folder should contain all the subject
"""
from uuid import UUID
from fastapi import HTTPException

from ..models import Subject, SubjectsIn, Subjects, SubjectsPatch, SubjectsOut, TypesOut, LessonsOut

def filters(content):
    if content.startswith("{neq}"):
        return ("__not", content.split("{neq}")[1])
    if content.startswith("{gt}"):
        return ("__gt", content.split("{gt}")[1])
    if content.startswith("{gteq}"):
        return ("__gte", content.split("{gteq}")[1])
    if content.startswith("{lt}"):
        return ("__lt", content.split("{lt}")[1])
    if content.startswith("{lteq}"):
        return ("__lte", content.split("{lteq}")[1])
    if content.startswith("{like}"):
        return ("__contains", content.split("{like}")[1])
    return ("", content)

async def get_all_subjects(name : str | None = None,
                           active : bool | None = None,
                           ) -> list[SubjectsOut]:
    """Retrieve all subjects"""
    filter = {}

    if name is not None:
        sufix, value = filters(name)
        filter["name" + sufix] = value
    if active is not None:
        filter["active"] = active

    if filter:
            body = await Subject.filter(**filter).prefetch_related('lesson', 'type').all()
            body = subjects_para_subjectsout(body)
            return body
    body = await Subject.all().prefetch_related('lesson', 'type')
    body = subjects_para_subjectsout(body)
    return body

async def create_subject(subjects: SubjectsIn) -> Subjects:
    """Create a new subject"""
    new_subject = await Subject.create(**subjects.dict(exclude_unset=True))
    return await Subjects.from_tortoise_orm(new_subject)

async def get_subject(subject_id: str) -> Subjects:
    """Retrieve a subject"""
    return await Subjects.from_queryset_single(Subject.get(uuid=subject_id))

async def delete_subject(subject_id: str) -> int:
    """Delete a subject"""
    deleted_count = await Subject.filter(uuid=subject_id).update(active=False)
    if deleted_count:
        return deleted_count
    raise HTTPException(status_code=404, detail=f"Subject {subject_id} not found")

async def put_subject(subject_id: str, subjects: SubjectsIn) -> Subjects:
    """Update a subject"""
    await Subject.filter(uuid=subject_id).update(**subjects.dict(exclude_unset=True))
    return await Subjects.from_queryset_single(Subject.get(uuid=subject_id))

async def patch_subject(subject_id: str, subjects: SubjectsPatch) -> Subjects:
    """Partially Update a subject"""
    await Subject.filter(uuid=subject_id).update(**subjects.dict(exclude_unset=True))
    return await Subjects.from_queryset_single(Subject.get(uuid=subject_id))

def subjects_para_subjectsout(lista_subjects):
    lista_subjectsout = []
    for subject in lista_subjects:
        subjectsout = SubjectsOut(
            uuid=str(subject.uuid),
            name=subject.name,
            lesson=lessons_para_lessonsout([subject.lesson])[0],
            type=types_para_typesout([subject.type])[0],
            active=subject.active
        )
        lista_subjectsout.append(subjectsout.dict())
    return lista_subjectsout

def lessons_para_lessonsout(lista_lessons):
    lista_lessonsout = []
    for lesson in lista_lessons:
        lesson_out = LessonsOut(
            uuid=str(lesson.uuid),
            datetime=lesson.datetime,
            classroom=lesson.classroom,
            active=lesson.active
        )
        lista_lessonsout.append(lesson_out)
    return lista_lessonsout

def types_para_typesout(lista_types):
    lista_typesout = []
    for type_obj in lista_types:
        type_out = TypesOut(
            uuid=str(type_obj.uuid),
            name=type_obj.name,
            active=type_obj.active
        )
        lista_typesout.append(type_out)
    return lista_typesout
