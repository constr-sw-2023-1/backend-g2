"""
Esse módulo contém as rotas da aplicação.

As rotas devem ter a menor quantidade de lógica possível e se ater
somente a receber requisições e chamar controllers.
"""
from fastapi import FastAPI

from . import lesson, subject, type

def init_app(app: FastAPI) -> None:
    app.include_router(lesson.router)
    app.include_router(subject.router)
    app.include_router(type.router)
