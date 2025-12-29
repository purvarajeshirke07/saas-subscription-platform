from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "SaaS Subscription Platform"
    DATABASE_URL: str = "sqlite:///./app.db"
    SECRET_KEY: str = "super-secret"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
