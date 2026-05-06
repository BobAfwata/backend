import os


# Corrected the typo 'postgress' -> 'postgres'
# Ensure this matches the password you set for the postgres user
DEFAULT_DATABASE_URL = "postgresql://postgres:soongsil@localhost:5432/business_app"

class Settings:
    # Logic: It checks the Environment Variable first. 
    # If not found, it falls back to our corrected local string.
    DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL)
    
    SECRET_KEY = "supersecretkey"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN", "your_token")
    WHATSAPP_PHONE_ID = os.getenv("WHATSAPP_PHONE_ID", "your_phone_id")

settings = Settings()

