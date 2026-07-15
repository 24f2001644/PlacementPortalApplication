from celery import Celery
from celery.schedules import crontab

from app import create_app


# ==========================================================
# Create Flask App
# ==========================================================

flask_app = create_app()


# ==========================================================
# Create Celery
# ==========================================================

def create_celery(app):

    celery = Celery(
        app.import_name,
        include=[
            "tasks.export_tasks",
            "tasks.notification_tasks",
            "tasks.scheduled_tasks",
        ]
    )

    # Load Celery configuration
    celery.config_from_object("celery_config")

    # ==========================================================
    # Celery Beat Schedule
    # ==========================================================
    
    
    celery.conf.beat_schedule = {

    "daily-reminder": {
        "task": "tasks.scheduled_tasks.daily_reminder",
        "schedule": crontab(hour=9, minute=0)
    },
}

    # ==========================================================
    # Flask Application Context
    # ==========================================================

    class ContextTask(celery.Task):

        def __call__(self, *args, **kwargs):

            with app.app_context():

                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    return celery


# ==========================================================
# Celery Instance
# ==========================================================

celery = create_celery(flask_app)

