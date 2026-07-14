from datetime import datetime

from celery_worker import celery
from extensions import db
from models.notification import Notification


@celery.task(name="tasks.notification_tasks.send_notification")
def send_notification(
    user_id,
    message,
    title="System Notification",
    notification_type="GENERAL"
):

    notification = Notification(
        user_id=user_id,
        title=title,
        message=message,
        notification_type=notification_type,
        is_read=False,
        created_at=datetime.utcnow()
    )

    db.session.add(notification)
    db.session.commit()

    return {
        "message": "Notification created successfully"
    }