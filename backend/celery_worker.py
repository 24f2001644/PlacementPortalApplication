from celery import Celery

from config import Config


def create_celery():

    celery = Celery(
        "placement_portal",
        broker=Config.CELERY_BROKER_URL,
        backend=Config.CELERY_RESULT_BACKEND,
        include=[
            "tasks.export_tasks",
            "tasks.notification_tasks"
        ]
    )


    celery.conf.update(

        task_serializer="json",

        result_serializer="json",

        accept_content=["json"],

        timezone="Asia/Kolkata",

        enable_utc=True
    )


    return celery



celery = create_celery()