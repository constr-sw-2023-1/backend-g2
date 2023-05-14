from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# POST /{resource}: criação de um objeto
# DELETE /{resource}/{id}: exclusão de um objeto
# PUT /{resource}/{id}: atualização de todo o objeto
# PATCH /{resource}/{id}: atualização de alguns atributos do objeto
# GET /{resource}: recuperação de todos os objetos
# GET /{resource}/{id}: recuperação de um objeto pelo seu id

@app.post("/lessons/")
async def create_lesson():
    return {"message": "Lesson created successfully"}

@app.delete("/lessons/{lesson_id}")
async def delete_lesson(lesson_id: int):
    return {"message": f"Lesson {lesson_id} deleted successfully"}

@app.put("/lessons/{lesson_id}")
async def update_lesson(lesson_id: int):
    return {"message": f"Lesson {lesson_id} updated successfully"}

@app.patch("/lessons/{lesson_id}")
async def update_lesson(lesson_id: int):
    return {"message": f"Lesson {lesson_id} updated successfully"}

@app.get("/lessons/")
async def get_lessons():
    return {"message": "Lessons retrieved successfully"}

@app.get("/lessons/{lesson_id}")
async def get_lesson(lesson_id: int):
    return {"message": f"Lesson {lesson_id} retrieved successfully"}

@app.post("/lessons_type")
async def create_lesson_type():
    return {"message": "Lesson type created successfully"}

@app.delete("/lessons_type/{lesson_type_id}")
async def delete_lesson_type(lesson_type_id: int):
    return {"message": f"Lesson type {lesson_type_id} deleted successfully"}

@app.put("/lessons_type/{lesson_type_id}")
async def update_lesson_type(lesson_type_id: int):
    return {"message": f"Lesson type {lesson_type_id} updated successfully"}

@app.patch("/lessons_type/{lesson_type_id}")
async def update_lesson_type(lesson_type_id: int):
    return {"message": f"Lesson type {lesson_type_id} updated successfully"}

@app.get("/lessons_type/")
async def get_lessons_type():
    return {"message": "Lesson types retrieved successfully"}

@app.get("/lessons_type/{lesson_type_id}")
async def get_lesson_type(lesson_type_id: int):
    return {"message": f"Lesson type {lesson_type_id} retrieved successfully"}

@app.post("/students/")
async def create_student():
    return {"message": "Student created successfully"}

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    return {"message": f"Student {student_id} deleted successfully"}

@app.put("/students/{student_id}")
async def update_student(student_id: int):
    return {"message": f"Student {student_id} updated successfully"}

@app.patch("/students/{student_id}")
async def update_student(student_id: int):
    return {"message": f"Student {student_id} updated successfully"}

@app.get("/students/")
async def get_students():
    return {"message": "Students retrieved successfully"}

@app.get("/students/{student_id}")
async def get_student(student_id: int):
    return {"message": f"Student {student_id} retrieved successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8080)