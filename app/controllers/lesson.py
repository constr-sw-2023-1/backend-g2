"""This is the controllers module, this folder should contain all the controllers
"""
from fastapi import HTTPException
from ..models import Lesson, LessonsIn, Lessons, LessonPatch

async def get_all_lessons(classroom: int | None = None,
                           date: str | None = None,
                           classroom_neq: int | None = None,
                           classroom_gt: int | None = None,
                           classroom_gteq: int | None = None,
                           classroom_lt: int | None = None,
                           classroom_lteq: int | None = None,
                           classroom_like: int | None = None,
                           date_neq: str | None = None,
                           date_gt: str | None = None,
                           date_gteq: str | None = None,
                           date_lt: str | None = None,
                           date_lteq: str | None = None,
                           date_like: str | None = None
                           ):
    """Retrieve all lessons"""
    if classroom_neq:
        return await Lessons.from_queryset(Lesson.filter(classroom__not=classroom_neq))
    if classroom_gt:
        return await Lessons.from_queryset(Lesson.filter(classroom__gt=classroom_gt))
    if classroom_gteq:
        return await Lessons.from_queryset(Lesson.filter(classroom__gte=classroom_gteq))
    if classroom_lt:
        return await Lessons.from_queryset(Lesson.filter(classroom__lt=classroom_lt))
    if classroom_lteq:
        return await Lessons.from_queryset(Lesson.filter(classroom__lte=classroom_lteq))
    if classroom_like:
        return await Lessons.from_queryset(Lesson.filter(classroom__icontains=classroom_like))
    if date_neq:
        return await Lessons.from_queryset(Lesson.filter(datetime__not=date_neq))
    if date_gt:
        return await Lessons.from_queryset(Lesson.filter(datetime__gt=date_gt))
    if date_gteq:
        return await Lessons.from_queryset(Lesson.filter(datetime__gte=date_gteq))
    if date_lt:
        return await Lessons.from_queryset(Lesson.filter(datetime__lt=date_lt))
    if date_lteq:
        return await Lessons.from_queryset(Lesson.filter(datetime__lte=date_lteq))
    if date_like:
        return await Lessons.from_queryset(Lesson.filter(datetime__icontains=date_like))
    
    if classroom_neq and date:
        return await Lessons.from_queryset(Lesson.filter(classroom__not=classroom_neq, datetime=date))
    if classroom_gt and date:
        return await Lessons.from_queryset(Lesson.filter(classroom__gt=classroom_gt, datetime=date))
    if classroom_gteq and date:
        return await Lessons.from_queryset(Lesson.filter(classroom__gte=classroom_gteq, datetime=date))
    if classroom_lt and date:
        return await Lessons.from_queryset(Lesson.filter(classroom__lt=classroom_lt, datetime=date))
    if classroom_lteq and date:
        return await Lessons.from_queryset(Lesson.filter(classroom__lte=classroom_lteq, datetime=date))
    if classroom_like and date:
        return await Lessons.from_queryset(Lesson.filter(classroom__icontains=classroom_like, datetime=date))
    if date_neq and classroom:
        return await Lessons.from_queryset(Lesson.filter(datetime__not=date_neq, classroom=classroom))
    if date_gt and classroom:
        return await Lessons.from_queryset(Lesson.filter(datetime__gt=date_gt, classroom=classroom))
    if date_gteq and classroom:
        return await Lessons.from_queryset(Lesson.filter(datetime__gte=date_gteq, classroom=classroom))
    if date_lt and classroom:
        return await Lessons.from_queryset(Lesson.filter(datetime__lt=date_lt, classroom=classroom))
    if date_lteq and classroom:
        return await Lessons.from_queryset(Lesson.filter(datetime__lte=date_lteq, classroom=classroom))
    if date_like and classroom:
        return await Lessons.from_queryset(Lesson.filter(datetime__icontains=date_like, classroom=classroom))
    
    if classroom_neq and date_neq:
        return await Lessons.from_queryset(Lesson.filter(classroom__not=classroom_neq, datetime__not=date_neq))
    if classroom_gt and date_neq:
        return await Lessons.from_queryset(Lesson.filter(classroom__gt=classroom_gt, datetime__not=date_neq))
    if classroom_gteq and date_neq:
        return await Lessons.from_queryset(Lesson.filter(classroom__gte=classroom_gteq, datetime__not=date_neq))
    if classroom_lt and date_neq:
        return await Lessons.from_queryset(Lesson.filter(classroom__lt=classroom_lt, datetime__not=date_neq))
    if classroom_lteq and date_neq:
        return await Lessons.from_queryset(Lesson.filter(classroom__lte=classroom_lteq, datetime__not=date_neq))
    if classroom_like and date_neq:
        return await Lessons.from_queryset(Lesson.filter(classroom__icontains=classroom_like, datetime__not=date_neq))
    if date_gt and classroom_neq:
        return await Lessons.from_queryset(Lesson.filter(datetime__gt=date_gt, classroom__not=classroom_neq))
    if date_gteq and classroom_neq:
        return await Lessons.from_queryset(Lesson.filter(datetime__gte=date_gteq, classroom__not=classroom_neq))
    if date_lt and classroom_neq:
        return await Lessons.from_queryset(Lesson.filter(datetime__lt=date_lt, classroom__not=classroom_neq))
    if date_lteq and classroom_neq:
        return await Lessons.from_queryset(Lesson.filter(datetime__lte=date_lteq, classroom__not=classroom_neq))
    if date_like and classroom_neq:
        return await Lessons.from_queryset(Lesson.filter(datetime__icontains=date_like, classroom__not=classroom_neq))
    
    if classroom_gt and date_gt:
        return await Lessons.from_queryset(Lesson.filter(classroom__gt=classroom_gt, datetime__gt=date_gt))
    if classroom_gteq and date_gt:
        return await Lessons.from_queryset(Lesson.filter(classroom__gte=classroom_gteq, datetime__gt=date_gt))
    if classroom_lt and date_gt:
        return await Lessons.from_queryset(Lesson.filter(classroom__lt=classroom_lt, datetime__gt=date_gt))
    if classroom_lteq and date_gt:
        return await Lessons.from_queryset(Lesson.filter(classroom__lte=classroom_lteq, datetime__gt=date_gt))
    if classroom_like and date_gt:
        return await Lessons.from_queryset(Lesson.filter(classroom__icontains=classroom_like, datetime__gt=date_gt))
    if date_gteq and classroom_gt:
        return await Lessons.from_queryset(Lesson.filter(datetime__gte=date_gteq, classroom__gt=classroom_gt))
    if date_lt and classroom_gt:
        return await Lessons.from_queryset(Lesson.filter(datetime__lt=date_lt, classroom__gt=classroom_gt))
    if date_lteq and classroom_gt:
        return await Lessons.from_queryset(Lesson.filter(datetime__lte=date_lteq, classroom__gt=classroom_gt))
    if date_like and classroom_gt:
        return await Lessons.from_queryset(Lesson.filter(datetime__icontains=date_like, classroom__gt=classroom_gt))
    
    if classroom_gteq and date_gteq:
        return await Lessons.from_queryset(Lesson.filter(classroom__gte=classroom_gteq, datetime__gte=date_gteq))
    if classroom_lt and date_gteq:
        return await Lessons.from_queryset(Lesson.filter(classroom__lt=classroom_lt, datetime__gte=date_gteq))
    if classroom_lteq and date_gteq:
        return await Lessons.from_queryset(Lesson.filter(classroom__lte=classroom_lteq, datetime__gte=date_gteq))
    if classroom_like and date_gteq:
        return await Lessons.from_queryset(Lesson.filter(classroom__icontains=classroom_like, datetime__gte=date_gteq))
    if date_lt and classroom_gteq:
        return await Lessons.from_queryset(Lesson.filter(datetime__lt=date_lt, classroom__gte=classroom_gteq))
    if date_lteq and classroom_gteq:
        return await Lessons.from_queryset(Lesson.filter(datetime__lte=date_lteq, classroom__gte=classroom_gteq))
    if date_like and classroom_gteq:
        return await Lessons.from_queryset(Lesson.filter(datetime__icontains=date_like, classroom__gte=classroom_gteq))
    
    if classroom_lt and date_lt:
        return await Lessons.from_queryset(Lesson.filter(classroom__lt=classroom_lt, datetime__lt=date_lt))
    if classroom_lteq and date_lt:
        return await Lessons.from_queryset(Lesson.filter(classroom__lte=classroom_lteq, datetime__lt=date_lt))
    if classroom_like and date_lt:
        return await Lessons.from_queryset(Lesson.filter(classroom__icontains=classroom_like, datetime__lt=date_lt))
    if date_lteq and classroom_lt:
        return await Lessons.from_queryset(Lesson.filter(datetime__lte=date_lteq, classroom__lt=classroom_lt))
    if date_like and classroom_lt:
        return await Lessons.from_queryset(Lesson.filter(datetime__icontains=date_like, classroom__lt=classroom_lt))
    
    if classroom_lteq and date_lteq:
        return await Lessons.from_queryset(Lesson.filter(classroom__lte=classroom_lteq, datetime__lte=date_lteq))
    if classroom_like and date_lteq:
        return await Lessons.from_queryset(Lesson.filter(classroom__icontains=classroom_like, datetime__lte=date_lteq))
    if date_like and classroom_lteq:
        return await Lessons.from_queryset(Lesson.filter(datetime__icontains=date_like, classroom__lte=classroom_lteq))
    

    if classroom and date:
        return await Lessons.from_queryset(Lesson.filter(classroom=classroom, datetime=date))
    if classroom:
        return await Lessons.from_queryset(Lesson.filter(classroom=classroom))
    if date:
        return await Lessons.from_queryset(Lesson.filter(datetime=date))
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
