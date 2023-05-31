"""This is the controllers module, this folder should contain all the controllers
"""
from fastapi import HTTPException

from app.exceptions.customExcept import CustomExpection, NotFound
from ..models import Lesson, LessonsIn, Lessons, LessonPatch


async def get_all_lessons():
    """Retrieve all lessons"""
    try:
        return await Lessons.from_queryset(Lesson.all())
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Lesson not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e,  "error method get all lessons")


async def create_lesson(lessons: LessonsIn) -> Lessons:
    try:
        new_lesson = await Lesson.create(**lessons.dict(exclude_unset=True))
        return await Lessons.from_tortoise_orm(new_lesson)
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Lesson not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e,  "error method create lesson")


async def get_lesson(lesson_id: str) -> Lessons:
    try:
        return await Lessons.from_queryset_single(Lesson.get(uuid=lesson_id))
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Lesson not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e,  "error method get lesson")


async def delete_lesson(lesson_id: str) -> int:
    try:
        deleted_count = await Lesson.filter(uuid=lesson_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Lesson {lesson_id} not found")
        return deleted_count
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Lesson not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e,  "error method delete lesson")


async def put_lesson(lesson_id: str, lessons: LessonsIn) -> Lessons:
    try:
        await Lesson.filter(uuid=lesson_id).update(**lessons.dict(exclude_unset=True))
        return await Lessons.from_queryset_single(Lesson.get(uuid=lesson_id))
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Lesson not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e,  "error method put lesson")


async def patch_lesson(lesson_id: str, lessons: LessonPatch) -> Lessons:
    try:
        await Lesson.filter(uuid=lesson_id).update(**lessons.dict(exclude_unset=True))
        return await Lessons.from_queryset_single(Lesson.get(uuid=lesson_id))
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Lesson not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e, "error method patch lesson")
