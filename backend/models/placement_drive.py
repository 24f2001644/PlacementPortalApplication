from datetime import datetime

from extensions import db


class PlacementDrive(db.Model):
    __tablename__ = "placement_drives"

    drive_id = db.Column(
        db.Integer,
        primary_key=True
    )

    company_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "companies.user_id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    job_title = db.Column(
        db.String(150),
        nullable=False
    )

    job_description = db.Column(
        db.Text,
        nullable=False
    )

    eligible_branches = db.Column(
        db.String(255)
    )

    eligible_cgpa = db.Column(
        db.Float
    )

    eligible_year = db.Column(
        db.Integer
    )

    application_deadline = db.Column(
        db.Date
    )

    interview_date = db.Column(
        db.Date
    )

    interview_location = db.Column(
        db.String(200)
    )

    salary_package = db.Column(
        db.String(50)
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Pending"
    )
    # Pending
    # Approved
    # Rejected
    # Closed

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    company = db.relationship(
        "Company",
        back_populates="drives"
    )

    applications = db.relationship(
        "Application",
        back_populates="drive",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<PlacementDrive {self.job_title}>"