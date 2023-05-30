"""This is the controllers module, this folder should contain all the controllers
"""
from datetime import datetime
import string

from fastapi import HTTPException, Request, Response

from ..models import Lesson, LessonsIn, Lessons


async def get_all_lessons():
    """Retrieve all lessons"""
    return await Lessons.from_queryset(Lesson.all())

async def create_lesson(lessons: LessonsIn) -> Lessons:
    new_lesson = await Lesson.create(**lessons.dict(exclude_unset=True))
    return await Lessons.from_tortoise_orm(new_lesson)

async def get_lesson(lesson_id: str) -> Lessons:
    return await Lessons.from_queryset_single(Lesson.get(uuid=lesson_id))

async def delete_lesson(lesson_id: str) -> int:
    deleted_count = await Lesson.filter(uuid=lesson_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Lesson {lesson_id} not found")
    return deleted_count

