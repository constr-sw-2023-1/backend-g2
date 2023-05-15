from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from fastapi.responses import StreamingResponse
from app.models.subject import Subject

router = APIRouter(prefix="/lessons/subject", tags=["Subject"])

@router.post("/")
async def create_subject():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"message": "subject created successfully"}

@router.delete("/{subject_id}")
async def delete_subject(subject_id: int):
    """Deleta uma aula"""
    return {"message": f"subject {subject_id} deleted successfully"}

@router.put("/{subject_id}")
async def update_subject(subject_id: int):
    """Atualiza uma aula"""
    return {"message": f"subject {subject_id} updated successfully"}

@router.patch("/{subject_id}")
async def pacial_update_subject(subject_id: int):
    """Atualiza parcialmente uma aula"""
    return {"message": f"subject {subject_id} updated successfully"}

@router.get("/")
async def get_subjects():
    """Recupera todas as aulas"""
    return {"message": "subjects retrieved successfully"}

@router.get("/{subject_id}")
async def get_subject(subject_id: int):
    """Recupera uma aula pelo seu id"""
    return {"message": f"subject {subject_id} retrieved successfully"}