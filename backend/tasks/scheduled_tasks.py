from celery_worker import celery

from models.student import Student
from tasks.notification_tasks import send_notification


@celery.task(
    name="tasks.scheduled_tasks.daily_reminder"
)
def daily_reminder():

    students = Student.query.all()

    for student in students:

        send_notification.delay(
            student.user_id,
            "Placement Reminder",
            "Check the placement portal for new placement drives.",
            "REMINDER"
        )

    return {
        "message": "Daily reminders sent"
    }