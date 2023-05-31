

from fastapi import HTTPException
from ..models import Type, TypesIn, Types, TypesPatch

async def create_type(type: TypesIn) -> Types:
    """Cria um novo type"""
    return await Type.create(**type.dict())

async def delete_type(type_id: str):
    """Deleta um type"""
    deleted_count = await Type.filter(uuid=type_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Type {type_id} not found")
    return deleted_count

async def put_type(type_id: str, type: TypesIn) -> Types:
    await Type.filter(uuid=type_id).update(**type.dict(exclude_unset=True))
    return await Types.from_queryset_single(Type.get(uuid=type_id))

async def patch_type(type_id: str, type: TypesPatch) -> Types:
    await Type.filter(uuid=type_id).update(**type.dict(exclude_unset=True))
    return await Types.from_queryset_single(Type.get(uuid=type_id))

async def get_type(name : str | None = None) -> Types:
    """Retorna todos os types"""
    if name:
        return await Types.from_queryset(Type.filter(name=name))
    return await Types.from_queryset(Type.all())

async def get_type_id(type_id: str) -> Types:
    """Retorna um type específico"""
    return await Types.from_queryset_single(Type.get(uuid=type_id))

