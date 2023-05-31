"""This file is used to migrate the database
    It is used to create the database tables
    drop the database tables, and populate
    the database tables with data
"""
from app.exceptions.customExcept import CustomExpection, InternalServerError
from app.models import lesson, subject, type
from tortoise import Tortoise


async def init_db():
    try:
        await Tortoise.init(
            db_url='postgres://root:root@localhost:5432/backend',
            modules={'models': [lesson, subject, type]},
    )
        await Tortoise.generate_schemas()
    except CustomExpection as e:
        raise InternalServerError("something went wrong starting the database")
    except Exception as e:
        raise CustomExpection(e, "something went wrong starting the database")


async def close_db():
    try:
        await Tortoise.close_connections()
    except CustomExpection as e:
        raise InternalServerError("something went wrong closing the database")
    except Exception as e:
        raise CustomExpection(e, "something went wrong closing the database")


async def populate():
    """This function is used to populate the database
    """
