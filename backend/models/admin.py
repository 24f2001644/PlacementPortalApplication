from datetime import datetime
from extensions import db


class Admin(db.Model):
    __tablename__ = "admins"

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id", ondelete="CASCADE"),
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # Relationship
    user = db.relationship(
        "User",
        back_populates="admin"
    )

    def __repr__(self):
        return f"<Admin {self.name}>"