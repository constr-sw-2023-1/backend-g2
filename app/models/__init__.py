"""This is the models module, this folder should contain all the models
"""
from .lesson import Lesson, LessonsIn, Lessons, LessonPatch
from .subject import Subject, SubjectsIn, Subjects, SubjectsPatch
from .type import Type, TypesIn, Types, TypesPatch
from fastapi import FastAPI

