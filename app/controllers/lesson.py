"""This is the controllers module, this folder should contain all the controllers
"""
from datetime import datetime
from fastapi import HTTPException
from ..models import Lesson, LessonsIn, Lessons, LessonPatch

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


async def get_all_lessons(
    classroom: str | None = None, datetime: str | None = None , active: bool | None = None
):
    """Retrieve all lessons"""
    filter = {}

    if classroom is not None:
        suffix, value = filters(classroom)
        filter["classroom" + suffix] = int(value)
    if datetime is not None:
        suffix, value = filters(datetime)
        filter["datetime" + suffix] = value
    if active is not None:
        filter["active"] = active

    if filter:
        return await Lessons.from_queryset(Lesson.filter(**filter))
    return await Lessons.from_queryset(Lesson.all())

async def create_lesson(lessons: LessonsIn) -> Lessons:
    new_lesson = await Lesson.create(**lessons.dict(exclude_unset=True))
    return await Lessons.from_tortoise_orm(new_lesson)

async def get_lesson(lesson_id: str) -> Lessons:
    return await Lessons.from_queryset_single(Lesson.get(uuid=lesson_id))

async def delete_lesson(lesson_id: str) -> int:
    deleted_count = await Lesson.filter(uuid=lesson_id).update(active=False)
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Lesson {lesson_id} not found")
    return deleted_count

async def put_lesson(lesson_id: str, lessons: LessonsIn) -> Lessons:
    await Lesson.filter(uuid=lesson_id).update(**lessons.dict(exclude_unset=True))
    return await Lessons.from_queryset_single(Lesson.get(uuid=lesson_id))

async def patch_lesson(lesson_id: str, lessons: LessonPatch) -> Lessons:
    await Lesson.filter(uuid=lesson_id).update(**lessons.dict(exclude_unset=True))
    return await Lessons.from_queryset_single(Lesson.get(uuid=lesson_id))
