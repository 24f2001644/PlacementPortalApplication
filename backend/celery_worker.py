from celery import Celery
from config import Config


celery = Celery(
    "placement_portal",
    broker=Config.CELERY_BROKER_URL,
    backend=Config.CELERY_RESULT_BACKEND
)


celery.conf.update(

    task_serializer="json",

    result_serializer="json",

    accept_content=["json"],

    timezone="Asia/Kolkata",

    enable_utc=True
)


# Import tasks explicitly
import tasks.export_tasks
import tasks.notification_tasks