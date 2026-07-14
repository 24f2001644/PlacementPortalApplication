from app import create_app
from models.notification import Notification

app = create_app()

with app.app_context():
    notifications = Notification.query.all()

    print(f"Total notifications: {len(notifications)}\n")

    for n in notifications:
        print(f"ID: {n.notification_id}")
        print(f"User: {n.user_id}")
        print(f"Title: {n.title}")
        print(f"Message: {n.message}")
        print(f"Type: {n.notification_type}")
        print("-" * 40)