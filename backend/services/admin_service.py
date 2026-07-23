from datetime import datetime

from sqlalchemy import or_, func

from extensions import db

from models.user import User
from models.student import Student
from models.company import Company
from models.placement_drive import PlacementDrive
from models.application import Application
from extensions import cache
import os
from flask import send_file

from models.export_job import ExportJob

# from models.user import User
# from tasks.notification_tasks import send_notification
# ==========================================================
# ADMIN DASHBOARD
# ==========================================================

def admin_dashboard():

    total_students = Student.query.count()

    total_companies = Company.query.count()

    total_drives = PlacementDrive.query.count()

    total_applications = Application.query.count()

    approved_companies = User.query.filter_by(
        role="COMPANY",
        is_approved=True
    ).count()

    pending_companies = User.query.filter_by(
        role="COMPANY",
        is_approved=False
    ).count()

    approved_drives = PlacementDrive.query.filter_by(
        status="Approved"
    ).count()

    pending_drives = PlacementDrive.query.filter_by(
        status="Pending"
    ).count()

    rejected_drives = PlacementDrive.query.filter_by(
        status="Rejected"
    ).count()

    closed_drives = PlacementDrive.query.filter_by(
        status="Closed"
    ).count()

    active_students = User.query.filter_by(
        role="STUDENT",
        is_active=True
    ).count()

    blocked_students = User.query.filter_by(
        role="STUDENT",
        is_active=False
    ).count()

    applied = Application.query.filter_by(
        status="Applied"
    ).count()

    shortlisted = Application.query.filter_by(
        status="Shortlisted"
    ).count()

    selected = Application.query.filter_by(
        status="Selected"
    ).count()

    rejected = Application.query.filter_by(
        status="Rejected"
    ).count()

    registered_today = User.query.filter(

        func.date(User.created_at)
        ==
        datetime.utcnow().date()

    ).count()

    return {

        "students": total_students,

        "companies": total_companies,

        "placement_drives": total_drives,

        "applications": total_applications,

        "approved_companies": approved_companies,

        "pending_companies": pending_companies,

        "approved_drives": approved_drives,

        "pending_drives": pending_drives,

        "rejected_drives": rejected_drives,

        "closed_drives": closed_drives,

        "active_students": active_students,

        "blocked_students": blocked_students,

        "applied": applied,

        "shortlisted": shortlisted,

        "selected": selected,

        "rejected": rejected,

        "registered_today": registered_today

    }, 200


# ==========================================================
# GET ALL COMPANIES
# ==========================================================

def get_all_companies(search=None):

    query = Company.query.join(User)

    if search:

        query = query.filter(

            or_(

                Company.company_name.ilike(
                    f"%{search}%"
                ),

                Company.industry.ilike(
                    f"%{search}%"
                ),

                Company.location.ilike(
                    f"%{search}%"
                ),

                Company.hr_name.ilike(
                    f"%{search}%"
                ),

                User.email.ilike(
                    f"%{search}%"
                )

            )

        )

    companies = query.order_by(

        Company.created_at.desc()

    ).all()

    result = []

    for company in companies:

        user = company.user

        result.append({

            "user_id": company.user_id,

            "company_name": company.company_name,

            "industry": company.industry,

            "location": company.location,

            "website": company.website,

            "hr_name": company.hr_name,

            "hr_email": company.hr_email,

            "hr_phone": company.hr_phone,

            "description": company.description,

            "approval_date":
                company.approval_date.strftime("%Y-%m-%d %H:%M")
                if company.approval_date
                else None,

            "created_at":
                company.created_at.strftime("%Y-%m-%d %H:%M")
                if company.created_at
                else None,

            "email": user.email,

            "approved": user.is_approved,

            "blacklisted": user.is_blacklisted,

            "active": user.is_active

        })

    return result, 200


# ==========================================================
# APPROVE COMPANY
# ==========================================================

def approve_company(user_id):

    user = db.session.get(
        User,
        user_id
    )

    if not user or user.role != "COMPANY":

        return {

            "message": "Company not found"

        }, 404

    if user.is_approved:

        return {

            "message": "Company already approved"

        }, 400

    user.is_approved = True

    company = db.session.get(
        Company,
        user_id
    )

    if company:

        company.approval_date = datetime.utcnow()

    db.session.commit()
    
    cache.clear()

    return {

        "message": "Company approved successfully"

    }, 200


# ==========================================================
# REJECT COMPANY
# ==========================================================

def reject_company(user_id):

    user = db.session.get(
        User,
        user_id
    )

    if not user or user.role != "COMPANY":

        return {

            "message": "Company not found"

        }, 404

    db.session.delete(user)

    db.session.commit()
    
    cache.clear()

    return {

        "message": "Company rejected successfully"

    }, 200


# ==========================================================
# BLACKLIST / UNBLACKLIST COMPANY
# ==========================================================

def blacklist_company(user_id):

    user = db.session.get(
        User,
        user_id
    )

    if not user or user.role != "COMPANY":

        return {

            "message": "Company not found"

        }, 404

    user.is_blacklisted = not user.is_blacklisted

    db.session.commit()
    cache.clear()

    return {

        "message": "Blacklist status updated successfully",

        "blacklisted": user.is_blacklisted

    }, 200
    
    
    
# ==========================================================
# GET ALL STUDENTS
# ==========================================================

def get_all_students(search=None):

    query = Student.query.join(User)

    if search:

        query = query.filter(

            or_(

                Student.full_name.ilike(
                    f"%{search}%"
                ),

                Student.roll_number.ilike(
                    f"%{search}%"
                ),

                Student.branch.ilike(
                    f"%{search}%"
                ),

                Student.course.ilike(
                    f"%{search}%"
                ),

                User.email.ilike(
                    f"%{search}%"
                )

            )

        )

    students = query.order_by(

        Student.created_at.desc()

    ).all()

    result = []

    for student in students:

        user = student.user

        selected_application = Application.query.filter_by(
            student_id=student.user_id,
            status="Selected"
        ).first()

        placement_status = (
            selected_application.status
            if selected_application
            else "Not Placed"
        )

        result.append({

            "user_id": student.user_id,

            "full_name": student.full_name,

            "roll_number": student.roll_number,

            "email": user.email,

            "course": student.course,

            "branch": student.branch,

            "year": student.year,

            "graduation_year": student.graduation_year,

            "cgpa": student.cgpa,

            "phone": student.phone,

            "resume_path": student.resume_path,

            "profile_completed": student.profile_completed,

            "active": user.is_active,

            "placement_status": placement_status,

            "created_at":
                student.created_at.strftime("%Y-%m-%d %H:%M")
                if student.created_at
                else None

        })

    return result, 200



def get_student_details(user_id):

    student = Student.query.filter_by(
        user_id=user_id
    ).first()


    if not student:

        return {
            "message": "Student not found"
        }, 404


    user = User.query.filter_by(
        user_id=user_id
    ).first()


    resume_url = None

    if student.resume_path:

        resume_url = (
            "http://127.0.0.1:5000/"
            +
            student.resume_path.replace("\\","/")
        )


    return {

        "user_id": student.user_id,

        "full_name": student.full_name,

        "email": user.email,

        "roll_number": student.roll_number,

        "graduation_year": student.graduation_year,

        "cgpa": student.cgpa,

        "tenth_marks": student.tenth_marks,

        "twelfth_marks": student.twelfth_marks,

        "dob": (
            student.dob.strftime("%Y-%m-%d")
            if student.dob
            else None
        ),

        "year": student.year,

        "course": student.course,

        "branch": student.branch,

        "phone": student.phone,

        "address": student.address,

        "skills": student.skills,

        "resume_path": student.resume_path,

        "resume_url": resume_url,

        "profile_completed": student.profile_completed,

        "created_at": (
            student.created_at.strftime("%Y-%m-%d %H:%M:%S")
            if student.created_at
            else None
        )

    },200

# ==========================================================
# TOGGLE STUDENT STATUS
# ==========================================================

def toggle_student_status(user_id):

    user = db.session.get(
        User,
        user_id
    )

    if not user or user.role != "STUDENT":

        return {

            "message": "Student not found"

        }, 404

    user.is_active = not user.is_active

    db.session.commit()
    cache.clear()

    return {

        "message": "Student status updated successfully",

        "active": user.is_active

    }, 200





# ==========================================================
# GET ALL PLACEMENT DRIVES
# ==========================================================

def get_all_drives(search=None):

    query = PlacementDrive.query.join(Company)

    if search:

        query = query.filter(

            or_(

                PlacementDrive.job_title.ilike(
                    f"%{search}%"
                ),

                Company.company_name.ilike(
                    f"%{search}%"
                ),

                PlacementDrive.status.ilike(
                    f"%{search}%"
                )

            )

        )

    drives = query.order_by(

        PlacementDrive.created_at.desc()

    ).all()

    result = []

    for drive in drives:

        total_applications = Application.query.filter_by(

            drive_id=drive.drive_id

        ).count()

        result.append({

            "drive_id": drive.drive_id,

            "company_id": drive.company.user_id,

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

            "applications": total_applications,

            "created_at":
                drive.created_at.strftime("%Y-%m-%d %H:%M")
                if drive.created_at
                else None

        })

    return result, 200


# ==========================================================
# APPROVE PLACEMENT DRIVE
# ==========================================================

def approve_drive(drive_id):

    drive = db.session.get(
        PlacementDrive,
        drive_id
    )

    if not drive:

        return {

            "message": "Placement Drive not found"

        }, 404

    if drive.status == "Approved":

        return {

            "message": "Placement Drive already approved"

        }, 400

    drive.status = "Approved"

    db.session.commit()
    
    cache.clear()

    return {

        "message": "Placement Drive approved successfully"

    }, 200


# ==========================================================
# REJECT PLACEMENT DRIVE
# ==========================================================

def reject_drive(drive_id):

    drive = db.session.get(
        PlacementDrive,
        drive_id
    )

    if not drive:

        return {

            "message": "Placement Drive not found"

        }, 404

    drive.status = "Rejected"

    db.session.commit()
    cache.clear()

    return {

        "message": "Placement Drive rejected successfully"

    }, 200


# ==========================================================
# CLOSE PLACEMENT DRIVE
# ==========================================================

def close_drive(drive_id):

    drive = db.session.get(
        PlacementDrive,
        drive_id
    )

    if not drive:

        return {

            "message": "Placement Drive not found"

        }, 404

    if drive.status == "Closed":

        return {

            "message": "Placement Drive already closed"

        }, 400

    drive.status = "Closed"

    db.session.commit()
    
    cache.clear()

    return {

        "message": "Placement Drive closed successfully"

    }, 200
    
# ==========================================================
# GET ALL APPLICATIONS
# ==========================================================

def get_all_applications(

    search=None,

    status=None

):

    query = (

        Application.query

        .join(Student)

        .join(PlacementDrive)

        .join(Company)

    )

    # ------------------------------------------------------
    # FILTER BY STATUS
    # ------------------------------------------------------

    if status:

        query = query.filter(

            Application.status == status

        )

    # ------------------------------------------------------
    # SEARCH
    # ------------------------------------------------------

    if search:

        query = query.filter(

            or_(

                Student.full_name.ilike(
                    f"%{search}%"
                ),

                Student.roll_number.ilike(
                    f"%{search}%"
                ),

                Company.company_name.ilike(
                    f"%{search}%"
                ),

                PlacementDrive.job_title.ilike(
                    f"%{search}%"
                ),

                Application.status.ilike(
                    f"%{search}%"
                )

            )

        )

    applications = query.order_by(

        Application.application_date.desc()

    ).all()

    result = []

    for application in applications:

        student = application.student

        drive = application.drive

        company = drive.company

        result.append({

            "application_id":
                application.application_id,

            "student_id":
                student.user_id,

            "student_name":
                student.full_name,

            "roll_number":
                student.roll_number,

            "branch":
                student.branch,

            "course":
                student.course,

            "cgpa":
                student.cgpa,

            "company_id":
                company.user_id,

            "company_name":
                company.company_name,

            "drive_id":
                drive.drive_id,

            "job_title":
                drive.job_title,

            "salary_package":
                drive.salary_package,

            "status":
                application.status,

            "remarks":
                application.remarks,

            "application_date":
                application.application_date.strftime(
                    "%Y-%m-%d %H:%M"
                )
                if application.application_date
                else None,

            "interview_datetime":
                application.interview_datetime.strftime(
                    "%Y-%m-%d %H:%M"
                )
                if application.interview_datetime
                else None,

            "updated_at":
                application.updated_at.strftime(
                    "%Y-%m-%d %H:%M"
                )
                if application.updated_at
                else None

        })

    return result, 200


# ==========================================================
# UPDATE APPLICATION STATUS
# ==========================================================

def update_application_status(

    application_id,

    status

):

    application = db.session.get(

        Application,

        application_id

    )

    if not application:

        return {

            "message": "Application not found"

        }, 404

    allowed_status = [

        "Applied",

        "Shortlisted",

        "Selected",

        "Rejected"

    ]

    if status not in allowed_status:

        return {

            "message": "Invalid application status"

        }, 400

    application.status = status

    application.updated_at = datetime.utcnow()

    db.session.commit()
    
    cache.clear()

    return {

        "message": "Application status updated successfully",

        "status": application.status

    }, 200
    
    
# ==========================================================
# PLACEMENT STATISTICS
# ==========================================================
@cache.cached(timeout=300)
def placement_statistics():

    # ------------------------------------------------------
    # OVERALL COUNTS
    # ------------------------------------------------------

    total_students = Student.query.count()

    total_companies = Company.query.count()

    total_drives = PlacementDrive.query.count()

    total_applications = Application.query.count()

    # ------------------------------------------------------
    # COMPANY STATISTICS
    # ------------------------------------------------------

    approved_companies = User.query.filter_by(

        role="COMPANY",

        is_approved=True

    ).count()

    pending_companies = User.query.filter_by(

        role="COMPANY",

        is_approved=False

    ).count()

    blacklisted_companies = User.query.filter_by(

        role="COMPANY",

        is_blacklisted=True

    ).count()

    # ------------------------------------------------------
    # STUDENT STATISTICS
    # ------------------------------------------------------

    active_students = User.query.filter_by(

        role="STUDENT",

        is_active=True

    ).count()

    blocked_students = User.query.filter_by(

        role="STUDENT",

        is_active=False

    ).count()

    # ------------------------------------------------------
    # DRIVE STATISTICS
    # ------------------------------------------------------

    approved_drives = PlacementDrive.query.filter_by(

        status="Approved"

    ).count()

    pending_drives = PlacementDrive.query.filter_by(

        status="Pending"

    ).count()

    rejected_drives = PlacementDrive.query.filter_by(

        status="Rejected"

    ).count()

    closed_drives = PlacementDrive.query.filter_by(

        status="Closed"

    ).count()

    # ------------------------------------------------------
    # APPLICATION STATISTICS
    # ------------------------------------------------------

    applied = Application.query.filter_by(

        status="Applied"

    ).count()

    shortlisted = Application.query.filter_by(

        status="Shortlisted"

    ).count()

    selected = Application.query.filter_by(

        status="Selected"

    ).count()

    rejected = Application.query.filter_by(

        status="Rejected"

    ).count()

    # ------------------------------------------------------
    # PLACEMENT PERCENTAGE
    # ------------------------------------------------------

    placement_percentage = 0

    if total_students > 0:

        placement_percentage = round(

            (selected / total_students) * 100,

            2

        )

    # ------------------------------------------------------
    # BRANCH STATISTICS
    # ------------------------------------------------------

    branch_statistics = []

    branches = (

        db.session.query(

            Student.branch,

            func.count(Student.user_id)

        )

        .group_by(

            Student.branch

        )

        .all()

    )

    for branch, total in branches:

        placed = (

            Application.query

            .join(Student)

            .filter(

                Student.branch == branch,

                Application.status == "Selected"

            )

            .count()

        )

        branch_statistics.append({

            "branch": branch,

            "students": total,

            "placed": placed,

            "placement_percentage":

                round(

                    (placed / total) * 100,

                    2

                )

                if total > 0

                else 0

        })

    # ------------------------------------------------------
    # COMPANY HIRING STATISTICS
    # ------------------------------------------------------

    company_statistics = []

    companies = Company.query.order_by(

        Company.company_name

    ).all()

    for company in companies:

        total_selected = (

            Application.query

            .join(PlacementDrive)

            .filter(

                PlacementDrive.company_id == company.user_id,

                Application.status == "Selected"

            )

            .count()

        )

        total_company_drives = PlacementDrive.query.filter_by(

            company_id=company.user_id

        ).count()

        company_statistics.append({

            "company_name": company.company_name,

            "total_drives": total_company_drives,

            "selected_students": total_selected

        })

    # ------------------------------------------------------
    # MONTHLY USER REGISTRATIONS
    # ------------------------------------------------------

    monthly_registrations = []

    monthly_data = (

        db.session.query(

            func.strftime(

                "%Y-%m",

                User.created_at

            ),

            func.count(User.user_id)

        )

        .group_by(

            func.strftime(

                "%Y-%m",

                User.created_at

            )

        )

        .order_by(

            func.strftime(

                "%Y-%m",

                User.created_at

            )

        )

        .all()

    )

    for month, count in monthly_data:

        monthly_registrations.append({

            "month": month,

            "registrations": count

        })

    # ------------------------------------------------------
    # FINAL RESPONSE
    # ------------------------------------------------------

    return {

        "total_students": total_students,

        "active_students": active_students,

        "blocked_students": blocked_students,

        "total_companies": total_companies,

        "approved_companies": approved_companies,

        "pending_companies": pending_companies,

        "blacklisted_companies": blacklisted_companies,

        "total_drives": total_drives,

        "approved_drives": approved_drives,

        "pending_drives": pending_drives,

        "rejected_drives": rejected_drives,

        "closed_drives": closed_drives,

        "total_applications": total_applications,

        "applied": applied,

        "shortlisted": shortlisted,

        "selected": selected,

        "rejected": rejected,

        "placement_percentage": placement_percentage,

        "branch_statistics": branch_statistics,

        "company_statistics": company_statistics,

        "monthly_registrations": monthly_registrations

    }, 200
    
    
    
# ==========================================================
# GET SINGLE PLACEMENT DRIVE DETAILS
# ==========================================================

def get_drive_details(drive_id):

    drive = db.session.get(

        PlacementDrive,

        drive_id

    )

    if not drive:

        return {

            "message": "Placement Drive not found"

        }, 404

    applicants = []

    for application in drive.applications:

        student = application.student

        applicants.append({

            "application_id": application.application_id,

            "student_id": student.user_id,

            "full_name": student.full_name,

            "roll_number": student.roll_number,

            "course": student.course,

            "branch": student.branch,

            "year": student.year,

            "graduation_year": student.graduation_year,

            "cgpa": student.cgpa,

            "phone": student.phone,

            "resume_path": student.resume_path,

            "status": application.status,

            "remarks": application.remarks,

            "application_date":
                application.application_date.strftime(
                    "%Y-%m-%d %H:%M"
                )
                if application.application_date
                else None,

            "interview_datetime":
                application.interview_datetime.strftime(
                    "%Y-%m-%d %H:%M"
                )
                if application.interview_datetime
                else None

        })

    return {

        "drive_id": drive.drive_id,

        "company_id": drive.company.user_id,

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
            else None,

        "total_applications": len(applicants),

        "applicants": applicants

    }, 200
    
# ==========================================================
# CREATE EXPORT JOB
# ==========================================================

def create_export_job(student_id):
    
    from tasks.export_tasks import export_applications_csv

    job = ExportJob(

        student_id=student_id,

        status="PENDING"

    )

    db.session.add(job)

    db.session.commit()

    export_applications_csv.delay(job.export_id)

    return {

        "message": "Export started",

        "export_id": job.export_id

    }, 202
    
# ==========================================================
# GET EXPORT STATUS
# ==========================================================

def get_export_status(export_id):

    job = db.session.get(

        ExportJob,

        export_id

    )

    if not job:

        return {

            "message": "Export job not found"

        }, 404

    return {

        "export_id": job.export_id,

        "status": job.status,

        "file_path": job.file_path,

        "error_message": job.error_message,

        "created_at": (
            job.created_at.strftime("%Y-%m-%d %H:%M:%S")
            if job.created_at
            else None
        ),

        "completed_at": (
            job.completed_at.strftime("%Y-%m-%d %H:%M:%S")
            if job.completed_at
            else None
        )

    }, 200
    
# ==========================================================
# DOWNLOAD EXPORT
# ==========================================================

def download_export(export_id):

    job = db.session.get(

        ExportJob,

        export_id

    )

    if not job:

        return {

            "message": "Export job not found"

        }, 404

    if job.status != "COMPLETED":

        return {

            "message": "Export not completed"

        }, 400
        
        
    if not os.path.exists(job.file_path):
        return {
            "message": "Export file not found"
        }, 404

    return send_file(

        job.file_path,

        as_attachment=True

    )
    
    
# ==========================================================
# GET ALL EXPORTS
# ==========================================================

def get_all_exports():

    jobs = ExportJob.query.order_by(

        ExportJob.created_at.desc()

    ).all()

    result = []

    for job in jobs:

        result.append({

            "export_id": job.export_id,

            "student_id": job.student_id,

            "status": job.status,

            "file_path": job.file_path,

            "error_message": job.error_message,

            "created_at": (
                job.created_at.strftime("%Y-%m-%d %H:%M:%S")
                if job.created_at
                else None
            ),

            "completed_at": (
                job.completed_at.strftime("%Y-%m-%d %H:%M:%S")
                if job.completed_at
                else None
            )

        })

    return result, 200


