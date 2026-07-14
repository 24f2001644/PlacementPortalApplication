from celery_worker import celery

from extensions import db

from models.notification import Notification

from datetime import datetime



@celery.task(
    name="tasks.send_notification"
)
def send_notification(
    user_id,
    message
):


    notification = Notification(

        user_id=user_id,

        message=message,

        created_at=datetime.utcnow()

    )


    db.session.add(notification)

    db.session.commit()



    return {

        "message":"Notification created"

    }