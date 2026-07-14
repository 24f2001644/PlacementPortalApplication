import os


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
        "jwt-secret"
    )


    # ==========================================================
    # REDIS CONFIGURATION
    # ==========================================================

    REDIS_URL = os.getenv(
        "REDIS_URL",
        "redis://localhost:6379/0"
    )


    # ==========================================================
    # FLASK CACHE
    # ==========================================================

    CACHE_TYPE = "RedisCache"

    CACHE_REDIS_URL = REDIS_URL

    CACHE_DEFAULT_TIMEOUT = 300


    # ==========================================================
    # CELERY
    # ==========================================================

    CELERY_BROKER_URL = REDIS_URL

    CELERY_RESULT_BACKEND = REDIS_URL