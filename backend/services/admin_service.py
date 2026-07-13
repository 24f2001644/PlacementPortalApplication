from datetime import datetime

from sqlalchemy import or_, func

from extensions import db

from models.user import User
from models.student import Student
from models.company import Company
from models.placement_drive import PlacementDrive
from models.application import Application


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

            "approval_date": company.approval_date,

            "created_at": company.created_at,

            "email": user.email,

            "approved": user.is_approved,

            "blacklisted": user.is_blacklisted,

            "active": user.is_active

        })

    return result, 200


def approve_company(user_id):

    user = db.session.get(
        User,
        user_id
    )

    if not user or user.role != "COMPANY":

        return {

            "message": "Company not found"

        },404

    if user.is_approved:

        return {

            "message":"Already approved"

        },400

    user.is_approved = True

    company = db.session.get(
        Company,
        user_id
    )

    company.approval_date = datetime.utcnow()

    db.session.commit()

    return {

        "message":"Company approved successfully"

    },200
    
    
    
def reject_company(user_id):

    user = db.session.get(
        User,
        user_id
    )

    if not user:

        return {

            "message":"Company not found"

        },404

    db.session.delete(user)

    db.session.commit()

    return {

        "message":"Company rejected successfully"

    },200
    
    
def blacklist_company(user_id):

    user = db.session.get(
        User,
        user_id
    )

    if not user:

        return {

            "message":"Company not found"

        },404

    user.is_blacklisted = not user.is_blacklisted

    db.session.commit()

    return {

        "message":"Blacklist updated",

        "blacklisted":user.is_blacklisted

    },200
    
    
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

        result.append({

            "user_id": student.user_id,

            "full_name": student.full_name,

            "roll_number": student.roll_number,

            "email": user.email,

            "branch": student.branch,

            "course": student.course,

            "year": student.year,

            "cgpa": student.cgpa,

            "phone": student.phone,

            "resume": student.resume_path,

            "profile_completed": student.profile_completed,

            "active": user.is_active,

            "created_at": student.created_at

        })

    return result,200


def toggle_student_status(user_id):

    user = db.session.get(
        User,
        user_id
    )

    if not user or user.role != "STUDENT":

        return {

            "message":"Student not found"

        },404

    user.is_active = not user.is_active

    db.session.commit()

    return {

        "message":"Student status updated",

        "active":user.is_active

    },200
    
    
    
def get_all_drives(search=None):

    query = (
        PlacementDrive.query
        .join(Company)
    )

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

        company = drive.company

        total_applications = Application.query.filter_by(
            drive_id=drive.drive_id
        ).count()

        result.append({

            "drive_id": drive.drive_id,

            "company_id": company.user_id,

            "company_name": company.company_name,

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

            "applications": total_applications,

            "created_at": drive.created_at

        })

    return result,200



def approve_drive(drive_id):

    drive = db.session.get(
        PlacementDrive,
        drive_id
    )

    if not drive:

        return {

            "message":"Placement Drive not found"

        },404

    if drive.status == "Approved":

        return {

            "message":"Already approved"

        },400

    drive.status = "Approved"

    db.session.commit()

    return {

        "message":"Placement Drive approved successfully"

    },200
    
    
    
def reject_drive(drive_id):

    drive = db.session.get(
        PlacementDrive,
        drive_id
    )

    if not drive:

        return {

            "message":"Placement Drive not found"

        },404

    drive.status = "Rejected"

    db.session.commit()

    return {

        "message":"Placement Drive rejected"

    },200
    
    
    
def close_drive(drive_id):

    drive = db.session.get(
        PlacementDrive,
        drive_id
    )

    if not drive:

        return {

            "message":"Placement Drive not found"

        },404

    drive.status = "Closed"

    db.session.commit()

    return {

        "message":"Placement Drive closed"

    },200
    
    
    
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
    
    if status:

        query = query.filter(

        Application.status == status

    )

    if search:

        query = query.filter(

            or_(

                Student.full_name.ilike(
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

            "company":
                company.company_name,

            "job_title":
                drive.job_title,

            "drive_id":
                drive.drive_id,

            "status":
                application.status,

            "remarks":
                application.remarks,

            "application_date":
                application.application_date,

            "interview_datetime":
                application.interview_datetime,

            "updated_at":
                application.updated_at

        })

    return result,200


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

            "message":"Application not found"

        },404

    allowed_status = [

        "Applied",

        "Shortlisted",

        "Selected",

        "Rejected"

    ]

    if status not in allowed_status:

        return {

            "message":"Invalid Status"

        },400

    application.status = status

    application.updated_at = datetime.utcnow()

    db.session.commit()

    return {

        "message":"Application updated successfully",

        "status":status

    },200
    
    
    
def placement_statistics():

    # -------------------------------------------------------
    # Overall Counts
    # -------------------------------------------------------

    total_students = Student.query.count()

    total_companies = Company.query.count()

    total_drives = PlacementDrive.query.count()

    total_applications = Application.query.count()

    # -------------------------------------------------------
    # Companies
    # -------------------------------------------------------

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

    # -------------------------------------------------------
    # Students
    # -------------------------------------------------------

    active_students = User.query.filter_by(

        role="STUDENT",

        is_active=True

    ).count()

    blocked_students = User.query.filter_by(

        role="STUDENT",

        is_active=False

    ).count()

    # -------------------------------------------------------
    # Drives
    # -------------------------------------------------------

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

    # -------------------------------------------------------
    # Applications
    # -------------------------------------------------------

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

    # -------------------------------------------------------
    # Placement Percentage
    # -------------------------------------------------------

    placement_percentage = 0

    if total_students > 0:

        placement_percentage = round(

            (selected / total_students) * 100,

            2

        )

    # -------------------------------------------------------
    # Branch Statistics
    # -------------------------------------------------------

    branch_statistics = []

    branches = (

        db.session.query(

            Student.branch,

            func.count(Student.user_id)

        )

        .group_by(Student.branch)

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

            "placed": placed

        })

    # -------------------------------------------------------
    # Company Hiring Statistics
    # -------------------------------------------------------

    company_statistics = []

    companies = Company.query.all()

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

        total_drives_company = PlacementDrive.query.filter_by(

            company_id=company.user_id

        ).count()

        company_statistics.append({

            "company": company.company_name,

            "drives": total_drives_company,

            "selected": total_selected

        })

    # -------------------------------------------------------
    # Monthly Registrations
    # -------------------------------------------------------

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

        .all()

    )

    for month, count in monthly_data:

        monthly_registrations.append({

            "month": month,

            "registrations": count

        })

    # -------------------------------------------------------
    # Dashboard Response
    # -------------------------------------------------------

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

    },200
    
# ==========================================================
# GET SINGLE DRIVE DETAILS
# ==========================================================

def get_drive_details(drive_id):

    drive = PlacementDrive.query.get(drive_id)

    if not drive:

        return {

            "message": "Drive not found"

        },404

    applicants = []

    for application in drive.applications:

        student = application.student

        applicants.append({

            "application_id": application.application_id,

            "student_id": student.user_id,

            "name": student.full_name,

            "roll_number": student.roll_number,

            "branch": student.branch,

            "cgpa": student.cgpa,

            "status": application.status,

            "application_date": application.application_date

        })

    return {

        "drive_id": drive.drive_id,

        "company": drive.company.company_name,

        "job_title": drive.job_title,

        "salary_package": drive.salary_package,

        "eligible_cgpa": drive.eligible_cgpa,

        "eligible_branches": drive.eligible_branches,

        "application_deadline": drive.application_deadline,

        "status": drive.status,

        "applicants": applicants

    },200