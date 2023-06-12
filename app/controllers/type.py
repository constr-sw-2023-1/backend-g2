"""Type controller"""
from fastapi import HTTPException
from ..models import Type, TypesIn, Types, TypesPatch

async def create_type(type: TypesIn) -> Types:
    """Cria um novo type"""
    return await Type.create(**type.dict())

async def delete_type(type_id: str):
    """Deleta um type"""
    deleted_count = await Type.filter(uuid=type_id).update(active=False)
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Type {type_id} not found")
    return deleted_count

async def put_type(type_id: str, type: TypesIn) -> Types:
    """Atualiza um type"""
    await Type.filter(uuid=type_id).update(**type.dict(exclude_unset=True))
    return await Types.from_queryset_single(Type.get(uuid=type_id))

async def patch_type(type_id: str, type: TypesPatch) -> Types:
    """Atualiza parcialmente um type"""
    await Type.filter(uuid=type_id).update(**type.dict(exclude_unset=True))
    return await Types.from_queryset_single(Type.get(uuid=type_id))

async def get_type_id(type_id: str) -> Types:
    """Retorna um type específico"""
    return await Types.from_queryset_single(Type.get(uuid=type_id))

async def get_type(
    name: str | None = None,
    active: bool | None = None
):
    """Retrieve all types"""
    filter = {}

    if name is not None:
        suffix, value = filters(name)
        filter["name" + suffix] = value
    if active is not None:
        filter["active"] = active

    if filter:
        return await Types.from_queryset(Type.filter(**filter))
    return await Types.from_queryset(Type.all())

def filters(content):
    """Identify the filter and return the suffix and value"""
    if content.startswith("{neq}"):
        return ("__not", content.split("{neq}")[1])
    if content.startswith("{gt}"):
        return ("__gt", content.split("{gt}")[1])
    if content.startswith("{gteq}"):
        return ("__gte", content.split("{gteq}")[1])
    if content.startswith("{lt}"):
        return ("__lt", content.split("{lt}")[1])
    if content.startswith("{lteq}"):
        return ("__lte", content.split("{lteq}")[1])
    if content.startswith("{like}"):
        return ("__contains", content.split("{like}")[1])
    return ("", content)
