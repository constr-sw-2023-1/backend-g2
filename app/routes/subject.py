from fastapi import APIRouter, Query

from ..controllers import subject as subject_controller
from ..models import Subjects, SubjectsIn, SubjectsPatch

router = APIRouter(prefix="/lessons/subject", tags=["Subject"])

@router.post("/", status_code=201)
async def create_subject(subjects: SubjectsIn) -> Subjects:
    """Cria uma aula"""
    return await subject_controller.create_subject(subjects)

@router.delete("/{subject_id}")
async def delete_subject(subject_id: str):
    """Deleta uma aula"""
    return await subject_controller.delete_subject(subject_id)

@router.put("/{subject_id}")
async def update_subject(subject_id: str, subjects: SubjectsIn) -> SubjectsIn:
    """Atualiza uma aula"""
    return await subject_controller.put_subject(subject_id, subjects)

@router.patch("/{subject_id}")
async def pacial_update_subject(subject_id: str, subjects: SubjectsPatch) -> Subjects:
    """Atualiza parcialmente uma aula"""
    return await subject_controller.patch_subject(subject_id, subjects)

@router.get("/")
async def get_subjects(name: str | None = Query(default=None, description="Filtro por nome"),):
    """Recupera todas as aulas"""
    return await subject_controller.get_all_subjects(name)

@router.get("/{subject_id}")
async def get_subject(subject_id: str):
    """Recupera uma aula pelo seu id"""
    return await subject_controller.get_subject(subject_id)