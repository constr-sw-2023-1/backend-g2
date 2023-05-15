from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from fastapi.responses import StreamingResponse

from ..controllers import user as user_controller
from ..helpers import after_route, generator, validate
from ..schemas import User

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/")
async def create_student():
    """ Cria um novo aluno"""
    return {"message": "Student created successfully"}

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    """Deleta um aluno"""
    return {"message": f"Student {student_id} deleted successfully"}

@app.put("/students/{student_id}")
async def update_student(student_id: int):
    """'Atualiza um aluno"""
    return {"message": f"Student {student_id} updated successfully"}

@app.patch("/students/{student_id}")
async def parcial_update_student(student_id: int):
    """Atualiza parcialmente um aluno"""
    return {"message": f"Student {student_id} updated successfully"}

@app.get("/students/")
async def get_students():
    """Recupera todos os alunos"""
    return {"message": "Students retrieved successfully"}

@app.get("/students/{student_id}")
async def get_student(student_id: int):
    """ Recupera um aluno pelo seu id"""
    return {"message": f"Student {student_id} retrieved successfully"}
