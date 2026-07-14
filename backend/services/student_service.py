from sqlalchemy import or_

from flask import Response

from io import StringIO

import csv

from extensions import db

from models.student import Student
from models.application import Application
from models.placement_drive import PlacementDrive

# ==========================================================
# STUDENT PROFILE
# ==========================================================

def get_student_profile(user_id):

    student = Student.query.filter_by(

        user_id=user_id

    ).first()

    if not student:

        return {

            "message": "Student profile not found"

        }, 404

    return {

        "student_id": student.user_id,

        "full_name": student.full_name,

        "email": student.user.email,

        "phone": student.phone,

        "roll_number": student.roll_number,

        "course": student.course,

        "branch": student.branch,

        "year": student.year,

        "graduation_year": student.graduation_year,

        "cgpa": student.cgpa,

        "tenth_marks": student.tenth_marks,

        "twelfth_marks": student.twelfth_marks,

        "dob": student.dob,

        "address": student.address,

        "skills": student.skills,

        "resume_path": student.resume_path,

        "profile_completed": student.profile_completed,

        "created_at": student.created_at

    }, 200


# ==========================================================
# GET AVAILABLE PLACEMENT DRIVES
# ==========================================================

def get_available_drives(search=None):

    query = PlacementDrive.query.filter_by(

        status="Approved"

    )

    if search:

        query = query.filter(

            or_(

                PlacementDrive.job_title.ilike(

                    f"%{search}%"

                ),

                PlacementDrive.interview_location.ilike(

                    f"%{search}%"

                ),

                PlacementDrive.salary_package.ilike(

                    f"%{search}%"

                )

            )

        )

    drives = query.order_by(

        PlacementDrive.created_at.desc()

    ).all()

    data = []

    for drive in drives:

        data.append({

            "drive_id": drive.drive_id,

            "company_name": drive.company.company_name,

            "job_title": drive.job_title,

            "job_description": drive.job_description,

            "eligible_branches": drive.eligible_branches,

            "eligible_cgpa": drive.eligible_cgpa,

            "eligible_year": drive.eligible_year,

            "application_deadline": drive.application_deadline,

            "interview_date": drive.interview_date,

            "interview_location": drive.interview_location,

            "salary_package": drive.salary_package,

            "status": drive.status,

            "created_at": drive.created_at

        })

    return data, 200



# ==========================================================
# APPLY FOR PLACEMENT DRIVE
# ==========================================================

def apply_for_drive(user_id, drive_id):

    student = Student.query.filter_by(

        user_id=user_id

    ).first()

    if not student:

        return {

            "message": "Student not found"

        }, 404


    drive = PlacementDrive.query.filter_by(

        drive_id=drive_id

    ).first()

    if not drive:

        return {

            "message": "Drive not found"

        }, 404


    if drive.status != "Approved":

        return {

            "message": "Drive is not available"

        }, 400


    # ----------------------------
    # Eligibility Validation
    # ----------------------------

    if drive.eligible_branches:

        allowed = [

            branch.strip().lower()

            for branch in drive.eligible_branches.split(",")

        ]

        if student.branch.lower() not in allowed:

            return {

                "message": "You are not eligible for this drive (Branch)."

            }, 400


    if (

        drive.eligible_cgpa is not None

        and student.cgpa is not None

        and student.cgpa < drive.eligible_cgpa

    ):

        return {

            "message": "CGPA criteria not satisfied."

        }, 400


    if (

        drive.eligible_year is not None

        and student.graduation_year != drive.eligible_year

    ):

        return {

            "message": "Graduation year does not match."

        }, 400


    existing = Application.query.filter_by(

        student_id=user_id,

        drive_id=drive_id

    ).first()

    if existing:

        return {

            "message": "You have already applied."

        }, 400


    application = Application(

        student_id=user_id,

        drive_id=drive_id,

        status="Applied"

    )

    db.session.add(application)

    db.session.commit()

    return {

        "message": "Application submitted successfully.",

        "application_id": application.application_id

    }, 201


# ==========================================================
# MY APPLICATIONS
# ==========================================================

def get_my_applications(user_id):

    applications = Application.query.filter_by(

        student_id=user_id

    ).order_by(

        Application.application_date.desc()

    ).all()

    data = []

    for application in applications:

        drive = application.drive

        company = drive.company

        data.append({

            "application_id": application.application_id,

            "company_name": company.company_name,

            "job_title": drive.job_title,

            "salary_package": drive.salary_package,

            "status": application.status,

            "application_date": application.application_date,

            "remarks": application.remarks,

            "interview_datetime": application.interview_datetime

        })

    return data, 200


# ==========================================================
# WITHDRAW APPLICATION
# ==========================================================

def withdraw_application(user_id, application_id):

    application = Application.query.filter_by(

        application_id=application_id,

        student_id=user_id

    ).first()

    if not application:

        return {

            "message": "Application not found"

        }, 404


    if application.status != "Applied":

        return {

            "message": "Application cannot be withdrawn after processing."

        }, 400


    db.session.delete(application)

    db.session.commit()

    return {

        "message": "Application withdrawn successfully."

    }, 200
    
    
    
    
# ==========================================================
# STUDENT DASHBOARD
# ==========================================================

def student_dashboard(user_id):

    student = Student.query.filter_by(

        user_id=user_id

    ).first()

    if not student:

        return {

            "message": "Student not found"

        }, 404


    # ======================================================
    # TOTAL APPROVED DRIVES
    # ======================================================

    total_drives = PlacementDrive.query.filter_by(

        status="Approved"

    ).count()


    # ======================================================
    # STUDENT APPLICATIONS
    # ======================================================

    applications = Application.query.filter_by(

        student_id=user_id

    ).order_by(

        Application.application_date.desc()

    ).all()


    applied_drives = len(applications)


    shortlisted = Application.query.filter_by(

        student_id=user_id,

        status="Shortlisted"

    ).count()


    selected = Application.query.filter_by(

        student_id=user_id,

        status="Selected"

    ).count()


    rejected = Application.query.filter_by(

        student_id=user_id,

        status="Rejected"

    ).count()


    # ======================================================
    # PROFILE COMPLETION
    # ======================================================

    profile_fields = [

        student.full_name,

        student.roll_number,

        student.phone,

        student.course,

        student.branch,

        student.year,

        student.graduation_year,

        student.cgpa,

        student.skills,

        student.resume_path

    ]


    completed = sum(

        1

        for field in profile_fields

        if field not in (None, "", [])

    )


    profile_completion = int(

        (completed / len(profile_fields)) * 100

    )


    # Keep database field updated

    student.profile_completed = (

        profile_completion == 100

    )

    db.session.commit()


    # ======================================================
    # RECENT APPLICATIONS
    # ======================================================

    recent_applications = []

    for application in applications[:5]:

        drive = application.drive

        recent_applications.append({

            "application_id": application.application_id,

            "company_name": drive.company.company_name,

            "job_title": drive.job_title,

            "status": application.status,

            "application_date": application.application_date.strftime(

                "%Y-%m-%d"

            )

            if application.application_date

            else None

        })


    # ======================================================
    # DASHBOARD RESPONSE
    # ======================================================

    return {

        "student_name": student.full_name,

        "profile_completed": student.profile_completed,

        "profile_completion": profile_completion,

        "total_drives": total_drives,

        "applied_drives": applied_drives,

        "shortlisted": shortlisted,

        "selected": selected,

        "rejected": rejected,

        "recent_applications": recent_applications

    }, 200
    
    
# ==========================================================
# GET SINGLE DRIVE DETAILS
# ==========================================================

def get_drive_details(drive_id):

    drive = PlacementDrive.query.filter_by(

        drive_id=drive_id

    ).first()

    if not drive:

        return {

            "message": "Drive not found"

        }, 404


    if drive.status != "Approved":

        return {

            "message": "Drive is not available"

        }, 400


    return {

        "drive_id": drive.drive_id,

        "company_name": drive.company.company_name,

        "job_title": drive.job_title,

        "job_description": drive.job_description,

        "eligible_branches": drive.eligible_branches,

        "eligible_cgpa": drive.eligible_cgpa,

        "eligible_year": drive.eligible_year,

        "application_deadline":

            drive.application_deadline.strftime("%Y-%m-%d")

            if drive.application_deadline

            else None,

        "interview_date":

            drive.interview_date.strftime("%Y-%m-%d")

            if drive.interview_date

            else None,

        "interview_location": drive.interview_location,

        "salary_package": drive.salary_package,

        "status": drive.status,

        "created_at":

            drive.created_at.strftime("%Y-%m-%d %H:%M")

            if drive.created_at

            else None

    }, 200


# ==========================================================
# EXPORT APPLICATIONS CSV
# ==========================================================

def export_student_csv(user_id):

    applications = (
        Application.query
        .filter_by(
            student_id=user_id
        )
        .order_by(
            Application.application_date.desc()
        )
        .all()
    )

    output = StringIO()

    writer = csv.writer(output)

    writer.writerow([

        "Application ID",

        "Company",

        "Job Title",

        "Salary Package",

        "Application Status",

        "Application Date"

    ])


    for application in applications:

        drive = application.drive

        company = drive.company

        writer.writerow([

            application.application_id,

            company.company_name,

            drive.job_title,

            drive.salary_package,

            application.status,

            application.application_date.strftime(

                "%Y-%m-%d %H:%M"

            )

            if application.application_date

            else ""

        ])


    csv_data = output.getvalue()

    output.close()


    return Response(

        csv_data,

        mimetype="text/csv",

        headers={

            "Content-Disposition":

                "attachment; filename=my_applications.csv"

        }

    )