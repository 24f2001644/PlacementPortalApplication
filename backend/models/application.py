from datetime import datetime
from extensions import db


class Application(db.Model):
    __tablename__ = "applications"

    application_id = db.Column(
        db.Integer,
        primary_key=True
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.user_id", ondelete="CASCADE"),
        nullable=False
    )

    drive_id = db.Column(
        db.Integer,
        db.ForeignKey("placement_drives.drive_id", ondelete="CASCADE"),
        nullable=False
    )

    application_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    status = db.Column(
        db.String(30),
        default="Applied"
    )   # Applied / Shortlisted / Selected / Rejected

    remarks = db.Column(db.Text)

    interview_datetime = db.Column(db.DateTime)

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    __table_args__ = (
        db.UniqueConstraint(
            "student_id",
            "drive_id",
            name="unique_application"
        ),
    )

    # Relationships
    student = db.relationship(
        "Student",
        back_populates="applications"
    )

    drive = db.relationship(
        "PlacementDrive",
        back_populates="applications"
    )

    def __repr__(self):
        return (
            f"<Application {self.application_id} - "
            f"{self.status}>"
        )