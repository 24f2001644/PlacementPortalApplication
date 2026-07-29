from datetime import datetime
import os

from flask import current_app
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity
)
from werkzeug.utils import secure_filename

from extensions import db
from models.user import User
from models.student import Student
from models.company import Company



def _save_resume(resume_file):

    if not resume_file or resume_file.filename == "":
        return None

    filename = secure_filename(resume_file.filename)

    upload_folder = current_app.config.get(
        "UPLOAD_FOLDER",
        "uploads/resumes"
    )

    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(
        upload_folder,
        filename
    )

    resume_file.save(file_path)

    return file_path


def _user_response(user):

    return {
        "user_id": user.user_id,
        "email": user.email,
        "role": user.role,
        "approved": user.is_approved,
        "active": user.is_active,
        "blacklisted": user.is_blacklisted
    }



def login_user(data):

    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    if not email or not password or not role:
        return {
            "message": "Missing credentials"
        }, 400

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:
        return {
            "message": "Invalid email or password"
        }, 401

    if not user.check_password(password):
        return {
            "message": "Invalid email or password"
        }, 401

    if user.role != role:
        return {
            "message": "Incorrect role selected"
        }, 401

    if not user.is_active:
        return {
            "message": "Account is inactive"
        }, 403

    if user.is_blacklisted:
        return {
            "message": "Account has been blacklisted"
        }, 403

    if (
        user.role == "COMPANY"
        and
        not user.is_approved
    ):
        return {
            "message": "Company approval pending"
        }, 403

    access_token = create_access_token(
        identity=str(user.user_id),
        additional_claims={
            "role": user.role
        }
    )

    return {
        "message": "Login successful",
        "token": access_token,
        "user": _user_response(user)
    }, 200



def get_profile():

    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return {
            "message": "User not found"
        }, 404

    response = _user_response(user)

    if user.role == "STUDENT":

        student = Student.query.get(user.user_id)

        if student:

            response["profile"] = {

                "full_name": student.full_name,
                "roll_number": student.roll_number,
                "graduation_year": student.graduation_year,
                "cgpa": student.cgpa,
                "tenth_marks": student.tenth_marks,
                "twelfth_marks": student.twelfth_marks,
                "dob": student.dob,
                "year": student.year,
                "course": student.course,
                "branch": student.branch,
                "phone": student.phone,
                "address": student.address,
                "skills": student.skills,
                "resume_path": student.resume_path,
                "profile_completed":
                student.profile_completed

            }

    elif user.role == "COMPANY":

        company = Company.query.get(user.user_id)

        if company:

            response["profile"] = {

                "company_name":
                company.company_name,

                "industry":
                company.industry,

                "location":
                company.location,

                "website":
                company.website,

                "hr_name":
                company.hr_name,

                "hr_email":
                company.hr_email,

                "hr_phone":
                company.hr_phone,

                "description":
                company.description

            }

    return response, 200




def register_student(data, resume_file):

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {
            "message": "Email and password are required"
        }, 400

    if User.query.filter_by(email=email).first():
        return {
            "message": "Email already registered"
        }, 409

    if Student.query.filter_by(
        roll_number=data.get("roll_number")
    ).first():
        return {
            "message": "Roll number already exists"
        }, 409

    resume_path = _save_resume(resume_file)

    user = User(
        email=email,
        role="STUDENT",
        is_active=True,
        is_approved=True,
        is_blacklisted=False
    )

    user.set_password(password)

    db.session.add(user)
    db.session.flush()

    dob = None
    if data.get("dob"):
        try:
            dob = datetime.strptime(
                data.get("dob"),
                "%Y-%m-%d"
            ).date()
        except Exception:
            pass

    student = Student(

        user_id=user.user_id,

        full_name=data.get("full_name"),

        roll_number=data.get("roll_number"),

        graduation_year=int(
            data.get("graduation_year")
        ),

        cgpa=float(data.get("cgpa"))
        if data.get("cgpa") else None,

        tenth_marks=float(
            data.get("tenth_marks")
        ) if data.get("tenth_marks") else None,

        twelfth_marks=float(
            data.get("twelfth_marks")
        ) if data.get("twelfth_marks") else None,

        dob=dob,

        year=int(data.get("year"))
        if data.get("year") else None,

        course=data.get("course"),

        branch=data.get("branch"),

        phone=data.get("phone"),

        address=data.get("address"),

        skills=data.get("skills"),

        resume_path=resume_path,

        profile_completed=True
    )

    db.session.add(student)

    db.session.commit()

    access_token = create_access_token(
        identity=str(user.user_id),
        additional_claims={
            "role": user.role
        }
    )

    return {

        "message":
        "Student registered successfully",

        "token":
        access_token,

        "user":
        _user_response(user),

        "student": {

            "full_name":
            student.full_name,

            "roll_number":
            student.roll_number,

            "graduation_year":
            student.graduation_year,

            "cgpa":
            student.cgpa,

            "course":
            student.course,

            "branch":
            student.branch,

            "resume_path":
            student.resume_path

        }

    }, 201
    
    
    
    
    

def register_company(data):

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {
            "message": "Email and password are required"
        }, 400

    if User.query.filter_by(email=email).first():
        return {
            "message": "Email already registered"
        }, 409

    if Company.query.filter_by(
        company_name=data.get("company_name")
    ).first():
        return {
            "message": "Company already exists"
        }, 409

    if Company.query.filter_by(
        hr_email=data.get("hr_email")
    ).first():
        return {
            "message": "HR email already registered"
        }, 409

    user = User(
        email=email,
        role="COMPANY",
        is_active=True,
        is_approved=False,
        is_blacklisted=False
    )

    user.set_password(password)

    db.session.add(user)
    db.session.flush()

    company = Company(

        user_id=user.user_id,

        company_name=data.get("company_name"),

        industry=data.get("industry"),

        location=data.get("location"),

        website=data.get("website"),

        hr_name=data.get("hr_name"),

        hr_email=data.get("hr_email"),

        hr_phone=data.get("hr_phone"),

        description=data.get("description")

    )

    db.session.add(company)

    db.session.commit()

    return {

        "message":
        "Company registered successfully. Waiting for admin approval.",

        "user": _user_response(user),

        "company": {

            "company_name": company.company_name,

            "industry": company.industry,

            "location": company.location,

            "website": company.website,

            "hr_name": company.hr_name,

            "hr_email": company.hr_email,

            "hr_phone": company.hr_phone,

            "description": company.description

        }

    }, 201



def update_student_profile(data):

    user_id = get_jwt_identity()

    student = Student.query.get(user_id)

    if not student:
        return {
            "message": "Student not found"
        }, 404

    student.full_name = data.get(
        "full_name",
        student.full_name
    )

    student.cgpa = data.get(
        "cgpa",
        student.cgpa
    )

    student.tenth_marks = data.get(
        "tenth_marks",
        student.tenth_marks
    )

    student.twelfth_marks = data.get(
        "twelfth_marks",
        student.twelfth_marks
    )

    student.course = data.get(
        "course",
        student.course
    )

    student.branch = data.get(
        "branch",
        student.branch
    )

    student.phone = data.get(
        "phone",
        student.phone
    )

    student.address = data.get(
        "address",
        student.address
    )

    student.skills = data.get(
        "skills",
        student.skills
    )

    if data.get("year"):
        student.year = int(data.get("year"))

    if data.get("graduation_year"):
        student.graduation_year = int(
            data.get("graduation_year")
        )

    if data.get("dob"):
        student.dob = datetime.strptime(
            data.get("dob"),
            "%Y-%m-%d"
        ).date()

    student.profile_completed = True

    db.session.commit()

    return {
        "message": "Profile updated successfully"
    }, 200



def upload_resume(resume_file):

    user_id = get_jwt_identity()

    student = Student.query.get(user_id)

    if not student:
        return {
            "message": "Student not found"
        }, 404

    if not resume_file:
        return {
            "message": "Resume file required"
        }, 400

    resume_path = _save_resume(resume_file)

    student.resume_path = resume_path

    db.session.commit()

    return {
        "message": "Resume uploaded successfully",
        "resume_path": resume_path
    }, 200
    
    
    

def update_company_profile(data):

    user_id = get_jwt_identity()

    company = Company.query.get(user_id)

    if not company:

        return {
            "message": "Company profile not found"
        },404



    company.company_name = data.get(
        "company_name",
        company.company_name
    )


    company.industry = data.get(
        "industry",
        company.industry
    )


    company.website = data.get(
        "website",
        company.website
    )


    company.location = data.get(
        "location",
        company.location
    )


    company.hr_name = data.get(
        "hr_name",
        company.hr_name
    )


    company.hr_email = data.get(
        "hr_email",
        company.hr_email
    )


    company.hr_phone = data.get(
        "hr_phone",
        company.hr_phone
    )


    company.description = data.get(
        "description",
        company.description
    )


    db.session.commit()


    return {

        "message":
        "Company profile updated successfully"

    },200