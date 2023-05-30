from fastapi import FastAPI

from . import dependencies, routes, models


def create_app() -> FastAPI:
    app = FastAPI()
    models.init_app(app)
    routes.init_app(app)

    return app