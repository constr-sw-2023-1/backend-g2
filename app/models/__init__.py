"""This is the models module, this folder should contain all the models
"""
from .lesson import Lesson, LessonsIn, Lessons

from fastapi import FastAPI

def init_app(app: FastAPI) -> None:
    app.include_router(lesson.Model)
