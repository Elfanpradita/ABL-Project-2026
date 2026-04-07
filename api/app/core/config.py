from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Monitoring API"
    DEBUG: bool = True
    API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()