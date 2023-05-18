"""This is the models module, this folder should contain all the models
"""
from tortoise import Tortoise


async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        db_url='postgres://root:root@localhost:5432/backend',
        modules={'models': ['app.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()