from datetime import datetime
from extensions import db, bcrypt


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(
        db.Integer,
        primary_key=True
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    role = db.Column(
        db.Enum(
            "ADMIN",
            "COMPANY",
            "STUDENT",
            name="user_roles"
        ),
        nullable=False
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    is_approved = db.Column(
        db.Boolean,
        default=False
    )

    is_blacklisted = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # Relationships
    student = db.relationship(
        "Student",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    company = db.relationship(
        "Company",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    admin = db.relationship(
        "Admin",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    notifications = db.relationship(
        "Notification",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(
            self.password_hash,
            password
        )

    def __repr__(self):
        return f"<User {self.email}>"