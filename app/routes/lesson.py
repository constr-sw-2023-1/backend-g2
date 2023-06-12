"""Rota de aula"""
from datetime import datetime
from uuid import UUID
from fastapi import APIRouter, Query, HTTPException
from flask import jsonify

from ..controllers import lesson as lesson_controller
from ..models import Lessons, LessonsIn, LessonPatch

router = APIRouter(prefix="/lesson", tags=["Lesson"])

@router.post("/", status_code=201)
async def create_lesson(lessons: LessonsIn) -> Lessons:
    """Cria uma aula"""
    return await lesson_controller.create_lesson(lessons)

@router.delete("/{lesson_id}")
async def delete_lesson(lesson_id: str):
    """Deleta uma aula"""
    return await lesson_controller.delete_lesson(lesson_id)

@router.put("/{lesson_id}")
async def update_lesson(lesson_id: str, lessons: LessonsIn):
    """Atualiza uma aula pelo seu id completamente"""
    return await lesson_controller.put_lesson(lesson_id, lessons)

@router.patch("/{lesson_id}")
async def pacial_update_lesson(lesson_id: str, lessons: LessonPatch):
    """Atualiza parcialmente uma aula"""
    return await lesson_controller.patch_lesson(lesson_id, lessons)

@router.get("/")
async def get_lessons(
    classroom: str | None = Query(default=None, description="Filtro por sala de aula"),
    datetime: str | None = Query(default=None, description="Filtro por data"),
    active: bool | None = Query(default=None, description="Filtro por ativo"),
):
    """Recupera todas as aulas"""
    body = await lesson_controller.get_all_lessons(classroom, datetime, active)
    if body:
        return body
    raise HTTPException(status_code=404, detail="Lesson not found")


@router.get("/{lesson_id}")
async def get_lesson(lesson_id: UUID):
    """Recupera uma aula pelo seu id"""
    body = await lesson_controller.get_lesson(lesson_id)
    if body == []:
        raise HTTPException(status_code=404, detail="Nenhuma aula encontrada")
    return body
