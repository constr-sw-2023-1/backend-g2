"""This is the subject module, this folder should contain all the subject
"""
from fastapi import HTTPException
from ..models import Subject, SubjectsIn, Subjects, SubjectsPatch

async def get_all_subjects(name : str | None = None):
    """Retrieve all subjects"""
    if name:
        return await Subjects.from_queryset(Subject.filter(name=name))
    return await Subjects.from_queryset(Subject.all())

async def create_subject(subjects: SubjectsIn) -> Subjects:
    new_subject = await Subject.create(**subjects.dict(exclude_unset=True))
    return await Subjects.from_tortoise_orm(new_subject)

async def get_subject(subject_id: str) -> Subjects:
    return await Subjects.from_queryset_single(Subject.get(uuid=subject_id))

async def delete_subject(subject_id: str) -> int:
    deleted_count = await Subject.filter(uuid=subject_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Subject {subject_id} not found")
    return deleted_count

async def put_subject(subject_id: str, subjects: SubjectsIn) -> Subjects:
    await Subject.filter(uuid=subject_id).update(**subjects.dict(exclude_unset=True))
    return await Subjects.from_queryset_single(Subject.get(uuid=subject_id))

async def patch_subject(subject_id: str, subjects: SubjectsPatch) -> Subjects:
    await Subject.filter(uuid=subject_id).update(**subjects.dict(exclude_unset=True))
    return await Subjects.from_queryset_single(Subject.get(uuid=subject_id))
