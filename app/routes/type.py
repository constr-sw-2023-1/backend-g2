from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from fastapi.responses import StreamingResponse
from app.models.type import Type

router = APIRouter(prefix="/lessons/subject/type", tags=["Type"])


@router.post("/")
async def create_type():
    """Cria um novo aluno"""
    return {"message": "type created successfully"}

@router.delete("/{type_id}")
async def delete_type(type_id: int):
    """Deleta um aluno"""
    return {"message": f"type {type_id} deleted successfully"}

@router.put("/{type_id}")
async def update_type(type_id: int):
    """Atualiza um aluno"""
    return {"message": f"type {type_id} updated successfully"}

@router.patch("/{type_id}")
async def parcial_update_type(type_id: int):
    """Atualiza parcialmente um aluno"""
    return {"message": f"type {type_id} updated successfully"}

@router.get("/")
async def get_type():
    """Recupera todos os alunos"""
    return {"message": "type retrieved successfully"}

@router.get("/{type_id}")
async def get_type(type_id: int):
    """ Recupera um aluno pelo seu id"""
    return {"message": f"type {type_id} retrieved successfully"}
