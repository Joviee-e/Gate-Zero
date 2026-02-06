import os
from datetime import timedelta

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Config:
    # ----------------------------
    # FLASK
    # ----------------------------
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")

    # ----------------------------
    # JWT
    # ----------------------------
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        seconds=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 86400))
    )

    # ----------------------------
    # MONGODB
    # ----------------------------
    MONGO_URI = os.getenv("MONGO_URI")
    DB_NAME = os.getenv("DB_NAME", "shelter_connect")

    # ----------------------------
    # SERVER
    # ----------------------------
    PORT = int(os.getenv("PORT", 5000))

    # ----------------------------
    # TESTING FLAGS
    # ----------------------------
    TESTING = False
