"""This is the models module, this folder should contain all the models
"""
from .lesson import Lesson, LessonsIn, Lessons, LessonPatch
from .subject import Subject, SubjectsIn, Subjects, SubjectsPatch
from .type import Type, TypesIn, Types, TypesPatch
from fastapi import FastAPI

def init_app(app: FastAPI) -> None:
    app.include_router(lesson.Model)
    app.include_router(subject.Model)
    app.include_router(type.Model)
