"""This is the controllers module, this folder should contain all the controllers
"""
from datetime import datetime

from fastapi import HTTPException, Request, Response

from ..models import lesson


async def get_all_lessons():
    """Retrieve all lessons"""
    return await lesson.all()

async def create_lesson(lesson: lesson.Lesson) -> lesson.Lesson:
    print("post_lesson----------------------------------")
    new_user = {}
    headers = {'Content-Type': 'application/json'}

    payload = Request.get_json()
    datetime = payload['datetime']
    classroom = payload['classroom']

    # Creating the new user
    new_lesson = await lesson.create(datetime=datetime, classroom=classroom)

    return new_lesson
