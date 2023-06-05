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
async def get_lessons(classroom: int | None = Query(default=None, description="Filtro por sala de aula"),
                      date: str | None = Query(default=None, description="Filtro por data"),
                      classroom_neq: int | None = Query(default=None, description="Filtro por sala de aula diferente"),
                      classroom_gt: int | None = Query(default=None, description="Filtro por sala de aula maior que"),
                      classroom_gteq: int | None = Query(default=None, description="Filtro por sala de aula maior ou igual a"),
                      classroom_lt: int | None = Query(default=None, description="Filtro por sala de aula menor que"),
                      classroom_lteq: int | None = Query(default=None, description="Filtro por sala de aula menor ou igual a"),
                      classroom_like: int | None = Query(default=None, description="Filtro por sala de aula que contém"),
                      date_neq: str | None = Query(default=None, description="Filtro por data diferente"),
                      date_gt: str | None = Query(default=None, description="Filtro por data maior que"),
                      date_gteq: str | None = Query(default=None, description="Filtro por data maior ou igual a"),
                      date_lt: str | None = Query(default=None, description="Filtro por data menor que"),
                      date_lteq: str | None = Query(default=None, description="Filtro por data menor ou igual a"),
                      date_like: str | None = Query(default=None, description="Filtro por data que contém"),
                      ):
    """Recupera todas as aulas"""
    body = await lesson_controller.get_all_lessons(classroom, 
                                                   date,
                                                    classroom_neq,
                                                    classroom_gt,
                                                    classroom_gteq,
                                                    classroom_lt,
                                                    classroom_lteq,
                                                    classroom_like,
                                                    date_neq,
                                                    date_gt,
                                                    date_gteq,
                                                    date_lt,
                                                    date_lteq,
                                                    date_like
                                                   )
    if body == []:
        raise HTTPException(status_code=404, detail="Nenhuma aula encontrada")
    return body

@router.get("/{lesson_id}")
async def get_lesson(lesson_id: UUID):
    """Recupera uma aula pelo seu id"""
    body = await lesson_controller.get_lesson(lesson_id)
    if body == []:
        raise HTTPException(status_code=404, detail="Nenhuma aula encontrada")
    return body
