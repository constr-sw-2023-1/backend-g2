"""App initialization module"""
from fastapi import FastAPI
from . import dependencies, routes, models, controllers
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from app.routes import init_app
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

init_app(app)

@app.on_event("startup")
async def startup_event():
    from app.migrate import init_db
    await init_db()
    # from migrate import populate
    # await populate()


@app.on_event("shutdown")
async def shutdown_event():
    from app.migrate import close_db
    await close_db()

arbitrary_types_allowed = True

origins = [
    "http://localhost.grupo2.com",
    "https://localhost.grupo2.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def custom_openapi():
    """Customize OpenAPI schema"""
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Backend Grupo - 2",
        version="1.0.0",
        description="Documentação Swagger grupo - 2",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.get("/")
async def root():
    """Root API endpoint

    Returns:
        String: Hello world message
    """
    return {"message": "Hello World"}


def create_app() -> FastAPI:
    app = FastAPI()
    routes.init_app(app)
    dependencies.init_app(app)
    return app