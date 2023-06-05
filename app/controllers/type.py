

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

"""
def apply_comparison_operator(query, field, operator, value):
    if operator == "eq":
        return query.filter(**{field: value})
    elif operator == "neq":
        return query.filter(**{field + "__ne": value})
    elif operator == "gt":
        return query.filter(**{field + "__gt": value})
    elif operator == "gteq":
        return query.filter(**{field + "__gte": value})
    elif operator == "lt":
        return query.filter(**{field + "__lt": value})
    elif operator == "lteq":
        return query.filter(**{field + "__lte": value})
    elif operator == "like":
        return query.filter(**{field + "__icontains": value})
    else:
        return query
    
async def get_resource(name: str = None, active: str = None) -> Types:
    query = Type.all()

    if name:
        operator, value = name.split(":")
        query = apply_comparison_operator(query, "name", operator, value)
    if active:
        operator, value = active.split(":")
        query = apply_comparison_operator(query, "active", operator, value)

    resources = await query
    return await Types.from_queryset(resources)
"""
