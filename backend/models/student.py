from datetime import datetime
from extensions import db


class Student(db.Model):
    __tablename__ = "students"

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id", ondelete="CASCADE"),
        primary_key=True
    )

    full_name = db.Column(
        db.String(100),
        nullable=False
    )

    roll_number = db.Column(
        db.String(50),
        unique=True,
        nullable=False,
        index=True
    )

    graduation_year = db.Column(
        db.Integer,
        nullable=False
    )

    cgpa = db.Column(db.Float)

    tenth_marks = db.Column(db.Float)

    twelfth_marks = db.Column(db.Float)

    dob = db.Column(db.Date)

    year = db.Column(db.Integer)

    course = db.Column(db.String(100))

    branch = db.Column(db.String(100))

    phone = db.Column(db.String(20))

    address = db.Column(db.Text)

    skills = db.Column(db.Text)

    # Example:
    # uploads/resumes/student_1.pdf
    resume_path = db.Column(db.String(255))

    profile_completed = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # Relationships
    user = db.relationship(
        "User",
        back_populates="student"
    )

    applications = db.relationship(
        "Application",
        back_populates="student",
        cascade="all, delete-orphan"
    )

    export_jobs = db.relationship(
        "ExportJob",
        back_populates="student",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Student {self.full_name}>"