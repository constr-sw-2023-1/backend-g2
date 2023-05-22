import asyncio
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from app.models.lesson import Lesson
from ..controllers import lesson as lesson_controller

router = APIRouter(prefix="/lesson", tags=["Lesson"])


@router.post("/", status_code=201)
async def create_lesson(lesson: Lesson) -> Lesson:
    print("ROUTER LESSON----------------------------------")
    print(lesson)
    return lesson_controller.create_lesson(lesson)

@router.delete("/{lesson_id}")
async def delete_lesson(lesson_id: int):
    """Deleta uma aula"""
    return {"message": f"Lesson {lesson_id} deleted successfully"}

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
    return get_all_lessons()

@router.get("/{lesson_id}")
async def get_lesson(lesson_id: int):
    """Recupera uma aula pelo seu id"""
    return {"message": f"Lesson {lesson_id} retrieved successfully"}
