from datetime import datetime
from extensions import db


class Company(db.Model):
    __tablename__ = "companies"

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.user_id", ondelete="CASCADE"),
        primary_key=True
    )

    company_name = db.Column(
        db.String(150),
        nullable=False
    )

    industry = db.Column(db.String(100))

    location = db.Column(db.String(200))

    website = db.Column(db.String(200))

    hr_name = db.Column(db.String(100))

    hr_email = db.Column(
        db.String(120),
        nullable=False
    )

    hr_phone = db.Column(db.String(20))

    description = db.Column(db.Text)

    approval_date = db.Column(db.DateTime)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # Relationships
    user = db.relationship(
        "User",
        back_populates="company"
    )

    drives = db.relationship(
        "PlacementDrive",
        back_populates="company",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Company {self.company_name}>"