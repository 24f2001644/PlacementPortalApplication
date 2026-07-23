# from datetime import datetime
# from zoneinfo import ZoneInfo

# from celery_worker import celery
# from extensions import db
# from models.notification import Notification


# @celery.task(
#     name="tasks.notification_tasks.send_notification"
# )
# def send_notification(
#     user_ids,
#     title,
#     message,
#     notification_type="GENERAL"
# ):
#     try:

#         notifications = []

#         created_time = datetime.now(
#             ZoneInfo("Asia/Kolkata")
#         ).replace(tzinfo=None)

#         for user_id in user_ids:

#             notifications.append(

#                 Notification(

#                     user_id=user_id,

#                     title=title,

#                     message=message,

#                     notification_type=notification_type,

#                     is_read=False,

#                     created_at=created_time

#                 )

#             )

#         db.session.bulk_save_objects(
#             notifications
#         )
#         print(user_ids)

#         db.session.commit()

#         return {

#             "message": "Notifications sent"

#         }

#     except Exception as e:

#         db.session.rollback()

#         return {

#             "error": str(e)

#         }




from datetime import datetime
from zoneinfo import ZoneInfo

from celery_worker import celery
from extensions import db
from models.notification import Notification


@celery.task(
    name="tasks.notification_tasks.send_notification"
)
def send_notification(
    user_ids,
    title,
    message,
    notification_type="GENERAL"
):
    try:

        print("Received user_ids:", user_ids)

        notifications = []

        created_time = datetime.now(
            ZoneInfo("Asia/Kolkata")
        ).replace(tzinfo=None)

        for user_id in user_ids:

            print("Creating notification for user:", user_id)

            notifications.append(

                Notification(

                    user_id=user_id,

                    title=title,

                    message=message,

                    notification_type=notification_type,

                    is_read=False,

                    created_at=created_time

                )

            )

        print("Total notifications:", len(notifications))

        db.session.bulk_save_objects(
            notifications
        )

        db.session.commit()

        print("Notifications committed successfully")

        return {
            "message": "Notifications sent"
        }

    except Exception as e:

        db.session.rollback()

        print("ERROR:", e)

        return {
            "error": str(e)
        }