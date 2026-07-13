from extensions import db
from models.user import User
from models.admin import Admin

def create_default_admin():

    email = "admin@placement.com"

    existing = User.query.filter_by(email=email).first()

    if existing:
        return

    user = User(
        email=email,
        role="ADMIN",
        is_active=True,
        is_approved=True,
        is_blacklisted=False
    )

    user.set_password("admin123")

    db.session.add(user)
    db.session.flush()

    admin = Admin(
        user_id=user.user_id,
        name="System Administrator"
    )

    db.session.add(admin)

    db.session.commit()

    print("Default Admin Created")