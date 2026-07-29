from celery import Celery
from celery.schedules import crontab

from app import create_app


flask_app = create_app()



def create_celery(app):

    celery = Celery(
        app.import_name,
        include=[
            "tasks.export_tasks",
            "tasks.student_export_tasks",
            "tasks.notification_tasks",
            "tasks.scheduled_tasks",
            "tasks.admin_report_tasks",
        ]
    )
    celery.config_from_object("celery_config")

    
    
    celery.conf.beat_schedule = {

        "daily-reminder": {
            "task": "tasks.scheduled_tasks.daily_reminder",
            "schedule": crontab(hour=9, minute=0),
        },

        "monthly-placement-report": {
            "task": "tasks.scheduled_tasks.monthly_report_scheduler",
            "schedule": crontab(
                day_of_month=1,
                hour=0,
                minute=0
            ),
        },
    }
    
    # celery.conf.beat_schedule = {

    #     "daily-reminder": {
    #         "task": "tasks.scheduled_tasks.daily_reminder",
    #         "schedule": crontab(),          # every minute
    #     },

    #     "monthly-placement-report": {
    #         "task": "tasks.scheduled_tasks.monthly_report_scheduler",
    #         "schedule": crontab(),          # every minute
    #     },
    # }


    class ContextTask(celery.Task):

        def __call__(self, *args, **kwargs):

            with app.app_context():

                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    return celery


celery = create_celery(flask_app)

