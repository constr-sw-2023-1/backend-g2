"""This is the models module, this folder should contain all the models
"""
from .lesson import Lesson, LessonsIn, Lessons, LessonPatch, LessonsOut
from .subject import Subject, SubjectsIn, Subjects, SubjectsPatch, SubjectsOut
from .type import Type, TypesIn, Types, TypesPatch, TypesOut
from fastapi import FastAPI

