"""This is the subject module, this folder should contain all the subject
"""
from fastapi import HTTPException

from app.exceptions.customExcept import CustomExpection, NotFound
from ..models import Subject, SubjectsIn, Subjects, SubjectsPatch

async def get_all_subjects():
    """Retrieve all subjects"""
    try:
        return await Subjects.from_queryset(Subject.all())
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Subject not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e,  "error method get all subjects")


async def create_subject(subjects: SubjectsIn) -> Subjects:
    try:
        new_subject = await Subject.create(**subjects.dict(exclude_unset=True))
        return await Subjects.from_tortoise_orm(new_subject)
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Subject not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e,  "error method create subject")


async def get_subject(subject_id: str) -> Subjects:
    try:
        return await Subjects.from_queryset_single(Subject.get(uuid=subject_id))
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Subject not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e,  "error method get subject")


async def delete_subject(subject_id: str) -> int:
    try:
        deleted_count = await Subject.filter(uuid=subject_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Subject {subject_id} not found")
        return deleted_count
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Subject not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e,  "error method delete subject")


async def put_subject(subject_id: str, subjects: SubjectsIn) -> Subjects:
    try:
        await Subject.filter(uuid=subject_id).update(**subjects.dict(exclude_unset=True))
        return await Subjects.from_queryset_single(Subject.get(uuid=subject_id))
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Subject not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e,  "error method put subject")


async def patch_subject(subject_id: str, subjects: SubjectsPatch) -> Subjects:
    try:
        await Subject.filter(uuid=subject_id).update(**subjects.dict(exclude_unset=True))
        return await Subjects.from_queryset_single(Subject.get(uuid=subject_id))
    except CustomExpection as e:
        if (e == 404):
            raise NotFound(e, detail="Subject not found\n", status= "404") 
    except Exception as e:
        raise CustomExpection(e,  "error method patch subject")