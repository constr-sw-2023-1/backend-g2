from pydantic import BaseSettings


class Settings(BaseSettings):
    API_KEY: str = "default"
    arbitrary_types_allowed = True

    class Config:
        env_file = ".env"
