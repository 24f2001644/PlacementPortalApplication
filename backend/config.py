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



    CACHE_TYPE = "SimpleCache"
