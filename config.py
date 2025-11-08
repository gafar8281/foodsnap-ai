import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # database
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    # Model
    MODEL_PATH: str = os.getenv("MODEL_PATH")
    MODEL_NAME: str = "RestNet50"

    # API
    HOST: str = os.getenv("HOST")
    PORT: int = int(os.getenv("PORT"))
    CORS_ORIGINS: str = os.getenv("CORS_ORIGINS")


settings = Settings()


