from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


def init_app(app: FastAPI):
    register_tortoise(
        app,
        db_url="postgres://root:root@localhost:5432/backend",
        modules={"models": ["app.models.lesson"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
