from pydantic import BaseSettings


class Settings(BaseSettings):
    API_KEY: str = "default"

    class Config:
        env_file = ".env"
