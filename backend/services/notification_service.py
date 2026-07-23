from models.user import User

from models.notification import Notification
from extensions import db

from flask_jwt_extended import get_jwt_identity


# ==========================================================
# GET ALL NOTIFICATIONS
# ==========================================================

def get_notifications():

    current_user = get_jwt_identity()

    notifications = (

        Notification.query

        .filter_by(user_id=current_user)

        .order_by(Notification.created_at.desc())

        .all()

    )

    data = []

    for notification in notifications:

        data.append({

            "notification_id": notification.notification_id,

            "title": notification.title,

            "message": notification.message,

            "notification_type": notification.notification_type,

            "is_read": notification.is_read,

            "created_at": notification.created_at

        })

    return data, 200


# ==========================================================
# MARK AS READ
# ==========================================================

def mark_notification_read(notification_id):

    current_user = get_jwt_identity()

    notification = Notification.query.filter_by(

        notification_id=notification_id,

        user_id=current_user

    ).first()

    if not notification:

        return {

            "message": "Notification not found"

        }, 404

    notification.is_read = True

    db.session.commit()

    return {

        "message": "Notification marked as read"

    }, 200


# ==========================================================
# DELETE NOTIFICATION
# ==========================================================

def delete_notification(notification_id):

    current_user = get_jwt_identity()

    notification = Notification.query.filter_by(

        notification_id=notification_id,

        user_id=current_user

    ).first()

    if not notification:

        return {

            "message": "Notification not found"

        }, 404

    db.session.delete(notification)

    db.session.commit()

    return {

        "message": "Notification deleted"

    }, 200


# ==========================================================
# UNREAD COUNT
# ==========================================================

def unread_count():

    current_user = get_jwt_identity()

    count = Notification.query.filter_by(

        user_id=current_user,

        is_read=False

    ).count()

    return {

        "count": count

    }, 200
    
    
    
    


def create_notification(body):

    from tasks.notification_tasks import send_notification

    title = body.get("title")
    message = body.get("message")
    notification_type = body.get("notification_type", "GENERAL")
    target = body.get("target", "").upper()

    if not title or not message or not target:
        return {
            "message": "Title, message and target are required"
        }, 400

    if target == "STUDENT":

        users = User.query.filter_by(
            role="STUDENT"
        ).all()

    elif target == "COMPANY":

        users = User.query.filter_by(
            role="COMPANY"
        ).all()

    elif target == "ALL":

        users = User.query.filter(
            User.role.in_(["STUDENT", "COMPANY"])
        ).all()

    else:

        return {
            "message": "Invalid target"
        }, 400

    print("TARGET =", target)
    print("USERS =", users)

    user_ids = [user.user_id for user in users]

    print("USER IDS =", user_ids)

    send_notification.delay(
        user_ids,
        title,
        message,
        notification_type
    )

    return {
        "message": "Notification queued successfully"
    }, 202