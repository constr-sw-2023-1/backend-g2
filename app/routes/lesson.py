import asyncio
import string
from fastapi import APIRouter

from ..controllers import lesson as lesson_controller
from ..models import Lessons, LessonsIn

router = APIRouter(prefix="/lesson", tags=["Lesson"])


@router.post("/", status_code=201)
async def create_lesson(lessons: LessonsIn) -> Lessons:
    return await lesson_controller.create_lesson(lessons)

@router.delete("/{lesson_id}")
async def delete_lesson(lesson_id: str):
    """Deleta uma aula"""
    return await lesson_controller.delete_lesson(lesson_id)

@router.put("/{lesson_id}")
async def update_lesson(lesson_id: int):
    """Atualiza uma aula"""
    return {"message": f"Lesson {lesson_id} updated successfully"}

@router.patch("/{lesson_id}")
async def pacial_update_lesson(lesson_id: int):
    """Atualiza parcialmente uma aula"""
    return {"message": f"Lesson {lesson_id} updated successfully"}

@router.get("/")
async def get_lessons():
    """Recupera todas as aulas"""
    return await lesson_controller.get_all_lessons()

@router.get("/{lesson_id}")
async def get_lesson(lesson_id: str):
    """Recupera uma aula pelo seu id"""
    return await lesson_controller.get_lesson(lesson_id)
