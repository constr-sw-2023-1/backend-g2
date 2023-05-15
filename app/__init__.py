from fastapi import FastAPI

from . import dependencies, routes
from .settings import Settings

def create_app() -> FastAPI:
    app = FastAPI()

    settings = Settings()
    dependencies.init_app(app, settings)
    routes.init_app(app)

    return app