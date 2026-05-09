import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database settings
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./business_system.db")

    # Security settings
    secret_key: str = os.getenv("SECRET_KEY", "supersecretkey")  # Change this in production!
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    # WhatsApp settings
    whatsapp_token: str = os.getenv("WHATSAPP_TOKEN", "your_token")
    whatsapp_phone_id: str = os.getenv("WHATSAPP_PHONE_ID", "your_phone_id")

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()

