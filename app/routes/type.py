"""Rotas para o CRUD de types"""
from fastapi import APIRouter, Query, HTTPException
from ..controllers import type as type_controller
from ..models import Types, TypesIn, TypesPatch

router = APIRouter(prefix="/lessons/subject/type", tags=["Type"])

@router.post("/")
async def create_type(type: TypesIn) -> Types:
    """Cria um novo type"""
    return await type_controller.create_type(type)

@router.delete("/{type_id}")
async def delete_type(type_id: str):
    """Deleta um type"""
    return await type_controller.delete_type(type_id)

@router.put("/{type_id}")
async def update_type(type_id: str, type: TypesIn) -> Types:
    """Atualiza um type"""
    return await type_controller.put_type(type_id, type)

@router.patch("/{type_id}")
async def parcial_update_type(type_id: str, type: TypesPatch) -> Types:
    """Atualiza parcialmente um type"""
    return await type_controller.patch_type(type_id, type)

@router.get("/")
async def get_type(name: str | None = Query(default=None, description="Filtro por nome"),
                   active: bool | None = Query(default=None, description="Filtro por ativo"),
                   ):
    """Recupera todos os types"""
    body = await type_controller.get_type(name, active)
    if body:
        return body
    raise HTTPException(status_code=404, detail="Type not found")

@router.get("/{type_id}")
async def get_type(type_id: str):
    """ Recupera um type pelo seu id"""
    body = await type_controller.get_type_id(type_id)
    if body:
        return body
    raise HTTPException(status_code=404, detail="Type not found")
