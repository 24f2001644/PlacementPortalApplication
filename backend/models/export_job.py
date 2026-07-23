from datetime import datetime
from zoneinfo import ZoneInfo
from extensions import db


class ExportJob(db.Model):
    __tablename__ = "export_jobs"

    export_id = db.Column(
        db.Integer,
        primary_key=True
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "students.user_id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="PENDING"
    )

    file_path = db.Column(
        db.String(255)
    )

    error_message = db.Column(
        db.Text
    )

    created_at = db.Column(
    db.DateTime,
    default=lambda: datetime.now(ZoneInfo("Asia/Kolkata")).replace(tzinfo=None)
)

    completed_at = db.Column(
        db.DateTime
    )

    student = db.relationship(
        "Student",
        back_populates="export_jobs"
    )

    def __repr__(self):
        return f"<ExportJob {self.export_id}>"