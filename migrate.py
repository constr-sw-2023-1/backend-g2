"""This file is used to migrate the database
    It is used to create the database tables
    drop the database tables, and populate
    the database tables with data
"""
from app.models import lesson, subject, type
from tortoise import Tortoise, run_async

