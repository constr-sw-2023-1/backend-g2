from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from fastapi.responses import StreamingResponse
from app.models.lesson import Lesson

router = APIRouter(prefix="/lesson", tags=["Lesson"])

@router.post("/")
async def create_lesson():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"message": "Lesson created successfully"}

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
    return {"message": "Lessons retrieved successfully"}

@router.get("/{lesson_id}")
async def get_lesson(lesson_id: int):
    """Recupera uma aula pelo seu id"""
    return {"message": f"Lesson {lesson_id} retrieved successfully"}