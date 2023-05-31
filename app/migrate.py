"""This file is used to migrate the database
    It is used to create the database tables
    drop the database tables, and populate
    the database tables with data
"""
from app.models import lesson, subject, type
from tortoise import Tortoise


async def init_db():
    await Tortoise.init(
        db_url='postgres://root:root@localhost:5432/backend',
        modules={'models': [lesson, subject, type]},
    )
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()


async def populate():
    """This function is used to populate the database
    """
