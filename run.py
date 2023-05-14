"""This is the main module of the project

"""
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


app = FastAPI()


def custom_openapi():
    """Customize OpenAPI schema"""
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Backend_GRUPO2",
        version="1.0.0",
        description="Documentação Swagger grupo - 2",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.get("/")
async def root():
    """Root API endpoint

    Returns:
        String: Hello world message
    """
    return {"message": "Hello World"}

# POST /{resource}: criação de um objeto
# DELETE /{resource}/{id}: exclusão de um objeto
# PUT /{resource}/{id}: atualização de todo o objeto
# PATCH /{resource}/{id}: atualização de alguns atributos do objeto
# GET /{resource}: recuperação de todos os objetos
# GET /{resource}/{id}: recuperação de um objeto pelo seu id

@app.post("/lessons/")
async def create_lesson():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"message": "Lesson created successfully"}

@app.delete("/lessons/{lesson_id}")
async def delete_lesson(lesson_id: int):
    """Deleta uma aula"""
    return {"message": f"Lesson {lesson_id} deleted successfully"}

@app.put("/lessons/{lesson_id}")
async def update_lesson(lesson_id: int):
    """Atualiza uma aula"""
    return {"message": f"Lesson {lesson_id} updated successfully"}

@app.patch("/lessons/{lesson_id}")
async def pacial_update_lesson(lesson_id: int):
    """Atualiza parcialmente uma aula"""
    return {"message": f"Lesson {lesson_id} updated successfully"}

@app.get("/lessons/")
async def get_lessons():
    """Recupera todas as aulas"""
    return {"message": "Lessons retrieved successfully"}

@app.get("/lessons/{lesson_id}")
async def get_lesson(lesson_id: int):
    """Recupera uma aula pelo seu id"""
    return {"message": f"Lesson {lesson_id} retrieved successfully"}

@app.post("/lessons_type")
async def create_lesson_type():
    """Cria um novo tipo de aula"""
    return {"message": "Lesson type created successfully"}

@app.delete("/lessons_type/{lesson_type_id}")
async def delete_lesson_type(lesson_type_id: int):
    """Deleta um tipo de aula"""
    return {"message": f"Lesson type {lesson_type_id} deleted successfully"}

@app.put("/lessons_type/{lesson_type_id}")
async def update_lesson_type(lesson_type_id: int):
    """Atualiza um tipo de aula"""
    return {"message": f"Lesson type {lesson_type_id} updated successfully"}

@app.patch("/lessons_type/{lesson_type_id}")
async def parcial_update_lesson_type(lesson_type_id: int):
    """Atualiza parcialmente um tipo de aula"""
    return {"message": f"Lesson type {lesson_type_id} updated successfully"}

@app.get("/lessons_type/")
async def get_lessons_type():
    """Recupera todos os tipos de aula"""
    return {"message": "Lesson types retrieved successfully"}

@app.get("/lessons_type/{lesson_type_id}")
async def get_lesson_type(lesson_type_id: int):
    """Recupera um tipo de aula pelo seu id"""
    return {"message": f"Lesson type {lesson_type_id} retrieved successfully"}

@app.post("/students/")
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8080)
