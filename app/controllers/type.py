

from fastapi import HTTPException

from app.exceptions.customExcept import CustomExpection, NotFound
from ..models import Type, TypesIn, Types, TypesPatch

async def create_type(type: TypesIn) -> Types:
    """Cria um novo type"""
    try:
        return await Type.create(**type.dict())
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Type not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e,  "error method create type")


async def delete_type(type_id: str):
    """Deleta um type"""
    try:
        deleted_count = await Type.filter(uuid=type_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Type {type_id} not found")
        return deleted_count
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Type not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e,  "error method delete type")


async def put_type(type_id: str, type: TypesIn) -> Types:
    try:
        await Type.filter(uuid=type_id).update(**type.dict(exclude_unset=True))
        return await Types.from_queryset_single(Type.get(uuid=type_id))
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Type not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e,  "error method put type")


async def patch_type(type_id: str, type: TypesPatch) -> Types:
    try:
        await Type.filter(uuid=type_id).update(**type.dict(exclude_unset=True))
        return await Types.from_queryset_single(Type.get(uuid=type_id))
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Type not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e,  "error method patch type")


async def get_type():
    """Retorna todos os types"""
    try:
        return await Types.from_queryset(Type.all())
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Type not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e,  "error method get type")


async def get_type_id(type_id: str) -> Types:
    """Retorna um type específico"""
    try:
        return await Types.from_queryset_single(Type.get(uuid=type_id))
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Type not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e,  "error method get type id")
