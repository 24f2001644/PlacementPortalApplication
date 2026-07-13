from datetime import datetime
from extensions import db


class ExportJob(db.Model):
    __tablename__ = "export_jobs"

    export_id = db.Column(
        db.Integer,
        primary_key=True
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.user_id", ondelete="CASCADE"),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="Pending"
    )
    # Pending
    # Processing
    # Completed
    # Failed

    file_path = db.Column(
        db.String(255)
    )

    error_message = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    completed_at = db.Column(
        db.DateTime
    )

    # Relationship
    student = db.relationship(
        "Student",
        back_populates="export_jobs"
    )

    def __repr__(self):
        return (
            f"<ExportJob {self.export_id} - "
            f"{self.status}>"
        )