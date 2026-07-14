from celery import Celery

from app import create_app



def create_celery(app):

    celery = Celery(

        app.import_name,

        broker=app.config["CELERY_BROKER_URL"],

        backend=app.config["CELERY_RESULT_BACKEND"],

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



flask_app = create_app()


celery = create_celery(
    flask_app
)