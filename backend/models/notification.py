from datetime import datetime
from zoneinfo import ZoneInfo
from extensions import db


class Notification(db.Model):
    __tablename__ = "notifications"

    notification_id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False
    )

    title = db.Column(
        db.String(100),
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    notification_type = db.Column(
        db.String(30),
        nullable=False
    )
    # REMINDER
    # EXPORT
    # REPORT
    # GENERAL

    is_read = db.Column(
        db.Boolean,
        default=False,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(
            ZoneInfo("Asia/Kolkata")
        ).replace(tzinfo=None),
        nullable=False
    )

    # Relationship
    user = db.relationship(
        "User",
        back_populates="notifications"
    )

    def __repr__(self):
        return f"<Notification {self.notification_id}>"