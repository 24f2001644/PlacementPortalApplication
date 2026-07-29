import os
from datetime import timedelta


class Config:


    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "placement-portal-secret"
    )

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///placement.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY",
        "placement_portal_application_secret_key_2026_very_secure"
    )

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)


    REDIS_URL = os.getenv(
        "REDIS_URL",
        "redis://localhost:6379/0"
    )
    

    CACHE_TYPE = "RedisCache"

    CACHE_REDIS_URL = REDIS_URL

    CACHE_DEFAULT_TIMEOUT = 300