from email.mime import application

from sqlalchemy import func

from extensions import db

from models.company import Company
from models.student import Student
from models.application import Application
from models.placement_drive import PlacementDrive

from datetime import datetime

def get_dashboard(user_id):

    company = Company.query.filter_by(
        user_id=user_id
    ).first()

    if not company:

        return {
            "message": "Company not found"
        }, 404

    drives = PlacementDrive.query.filter_by(
        company_id=user_id
    ).all()

    drive_ids = [

        drive.drive_id

        for drive in drives

    ]


    if drive_ids:

        applications = Application.query.filter(

            Application.drive_id.in_(drive_ids)

        ).all()

    else:

        applications = []


    recent_applications = []

    for application in sorted(

        applications,

        key=lambda x: x.application_date,

        reverse=True

    )[:5]:

        recent_applications.append({

            "id": application.application_id,

            "student": application.student.full_name,

            "role": application.drive.job_title,

            "status": application.status

        })


    dashboard = {

        "company_name": company.company_name,

        "total_drives": len(drives),

        "active_drives": len([

            drive

            for drive in drives

            if drive.status == "Approved"

        ]),

        "total_applications": len(applications),

        "shortlisted": len([

            application

            for application in applications

            if application.status == "Shortlisted"

        ]),

        "selected": len([

            application

            for application in applications

            if application.status == "Selected"

        ]),

        "recent_applications": recent_applications

    }

    return dashboard, 200



def get_company_profile(user_id):

    company = Company.query.filter_by(

        user_id=user_id

    ).first()


    if not company:

        return {

            "message": "Company profile not found"

        }, 404


    return {

        "company_id": company.user_id,

        "company_name": company.company_name,

        "industry": company.industry,

        "location": company.location,

        "website": company.website,

        "description": company.description,

        "hr_name": company.hr_name,

        "hr_email": company.hr_email,

        "hr_phone": company.hr_phone,

        "approval_date": company.approval_date,

        "created_at": company.created_at,

        "email": company.user.email,

        "is_approved": company.user.is_approved,

        "is_active": company.user.is_active,

        "is_blacklisted": company.user.is_blacklisted

    }, 200
    
    
    

def create_drive(user_id, data):

    company = Company.query.filter_by(
        user_id=user_id
    ).first()

    if not company:

        return {
            "message": "Company not found"
        }, 404

    if not company.user.is_approved:

        return {
            "message": "Company approval pending"
        }, 403
    
    application_deadline = None

    if data.get("application_deadline"):
        application_deadline = datetime.strptime(
            data.get("application_deadline"),
            "%Y-%m-%d"
        ).date()


    interview_date = None

    if data.get("interview_date"):
        interview_date = datetime.strptime(
            data.get("interview_date"),
            "%Y-%m-%d"
        ).date()

    drive = PlacementDrive(

        company_id=company.user_id,

        job_title=data.get("job_title"),

        job_description=data.get("job_description"),

        eligible_branches=data.get("eligible_branches"),

        eligible_cgpa=data.get("eligible_cgpa"),

        eligible_year=data.get("eligible_year"),

        application_deadline=application_deadline,

        interview_date=interview_date,

        interview_location=data.get("interview_location"),

        salary_package=data.get("salary_package"),

        status="Pending"

    )

    db.session.add(drive)

    db.session.commit()

    return {

        "message": "Placement drive created successfully",

        "drive_id": drive.drive_id

    }, 201



def get_company_drives(user_id):

    drives = PlacementDrive.query.filter_by(

        company_id=user_id

    ).order_by(

        PlacementDrive.created_at.desc()

    ).all()

    data = []

    for drive in drives:

        data.append({

            "drive_id": drive.drive_id,

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

            "created_at": drive.created_at,

            "total_applications": len(drive.applications)

        })

    return data, 200



def update_drive(user_id, drive_id, data):

    drive = PlacementDrive.query.filter_by(

        drive_id=drive_id,

        company_id=user_id

    ).first()

    if not drive:

        return {

            "message": "Drive not found"

        }, 404


    drive.job_title = data.get(

        "job_title",

        drive.job_title

    )

    drive.job_description = data.get(

        "job_description",

        drive.job_description

    )

    drive.eligible_branches = data.get(

        "eligible_branches",

        drive.eligible_branches

    )

    drive.eligible_cgpa = data.get(

        "eligible_cgpa",

        drive.eligible_cgpa

    )

    drive.eligible_year = data.get(

        "eligible_year",

        drive.eligible_year

    )

    drive.application_deadline = data.get(

        "application_deadline",

        drive.application_deadline

    )

    drive.interview_date = data.get(

        "interview_date",

        drive.interview_date

    )

    drive.interview_location = data.get(

        "interview_location",

        drive.interview_location

    )

    drive.salary_package = data.get(

        "salary_package",

        drive.salary_package

    )

    db.session.commit()

    return {

        "message": "Drive updated successfully"

    }, 200



def delete_drive(user_id, drive_id):

    drive = PlacementDrive.query.filter_by(

        drive_id=drive_id,

        company_id=user_id

    ).first()

    if not drive:

        return {

            "message": "Drive not found"

        }, 404

    db.session.delete(drive)

    db.session.commit()

    return {

        "message": "Drive deleted successfully"

    }, 200
    
    

def get_drive_applications(user_id):

    applications = (
        Application.query
        .join(PlacementDrive)
        .filter(
            PlacementDrive.company_id == user_id
        )
        .order_by(
            Application.application_date.desc()
        )
        .all()
    )

    data = []

    for application in applications:

        student = application.student
        drive = application.drive

        data.append({

            "application_id": application.application_id,

            "drive_id": drive.drive_id,

            "job_title": drive.job_title,

            "student_id": student.user_id,

            "full_name": student.full_name,

            "roll_number": student.roll_number,

            "branch": student.branch,

            "course": student.course,

            "graduation_year": student.graduation_year,

            "cgpa": student.cgpa,

            "skills": student.skills,

            "resume_path": student.resume_path,

            "application_date": application.application_date,

            "status": application.status,

            "remarks": application.remarks,

            "interview_datetime": application.interview_datetime

        })

    return data, 200



# def update_application_status(

#     user_id,

#     application_id,

#     status

# ):

#     application = Application.query.filter_by(

#         application_id=application_id

#     ).first()


#     if not application:

#         return {

#             "message": "Application not found"

#         }, 404

#     print("Logged in company:", user_id)
#     print("Drive company:", application.drive.company_id)

#     if application.drive.company_id != user_id:

#         return {

#             "message": "Unauthorized access"

#         }, 403


#     allowed_status = [

#         "Applied",

#         "Shortlisted",

#         "Rejected",

#         "Selected"

#     ]


#     if status not in allowed_status:

#         return {

#             "message": "Invalid status"

#         }, 400


#     application.status = status

#     db.session.commit()
#     print("Status updated successfully")

#     return {

#         "message": "Application status updated successfully"

#     }, 200

def update_application_status(user_id, application_id, status):

    print("STEP 1")

    application = Application.query.filter_by(
        application_id=application_id
    ).first()

    print("STEP 2")

    if not application:
        print("Application not found")
        return {"message": "Application not found"}, 404

    print("Logged in company:", user_id, type(user_id))
    print("Drive company:", application.drive.company_id, type(application.drive.company_id))

    if application.drive.company_id != user_id:
        print("Unauthorized")
        return {"message": "Unauthorized access"}, 403

    print("STEP 3")

    allowed_status = [
        "Applied",
        "Shortlisted",
        "Rejected",
        "Selected"
    ]

    print("Incoming status:", status)

    if status not in allowed_status:
        print("Invalid status")
        return {"message": "Invalid status"}, 400

    print("STEP 4")

    application.status = status

    print("STEP 5")

    db.session.commit()

    print("STEP 6")

    return {
        "message": "Application status updated successfully"
    }, 200



def close_drive(user_id, drive_id):

    drive = PlacementDrive.query.filter_by(

        drive_id=drive_id,

        company_id=user_id

    ).first()


    if not drive:

        return {

            "message": "Drive not found"

        }, 404


    if drive.status == "Closed":

        return {

            "message": "Drive already closed"

        }, 400


    drive.status = "Closed"

    db.session.commit()

    return {

        "message": "Placement drive closed successfully"

    }, 200
    
    
    

def get_selected_students(user_id):

    applications = (
        Application.query
        .join(
            PlacementDrive,
            Application.drive_id == PlacementDrive.drive_id
        )
        .filter(
            PlacementDrive.company_id == user_id,
            Application.status == "Selected"
        )
        .order_by(
            Application.application_date.desc()
        )
        .all()
    )

    data = []

    for application in applications:

        student = application.student
        drive = application.drive

        data.append({

            "application_id": application.application_id,

            "student_id": student.user_id,

            "student_name": student.full_name,

            "roll_number": student.roll_number,

            "email": student.user.email,

            "phone": student.phone,

            "branch": student.branch,

            "course": student.course,

            "graduation_year": student.graduation_year,

            "cgpa": student.cgpa,

            "skills": student.skills,

            "resume_path": student.resume_path,

            "job_title": drive.job_title,

            "salary_package": drive.salary_package,

            "selection_date": application.application_date

        })

    return data, 200



def get_student_details(user_id, student_id):

    student = Student.query.filter_by(

        user_id=student_id

    ).first()

    if not student:

        return {

            "message": "Student not found"

        }, 404


    has_application = (
        Application.query
        .join(
            PlacementDrive,
            Application.drive_id == PlacementDrive.drive_id
        )
        .filter(
            Application.student_id == student.user_id,
            PlacementDrive.company_id == user_id
        )
        .first()
    )

    if not has_application:

        return {

            "message": "Unauthorized access"

        }, 403


    return {

        "student_id": student.user_id,

        "full_name": student.full_name,

        "roll_number": student.roll_number,

        "email": student.user.email,

        "phone": student.phone,

        "dob": student.dob,

        "course": student.course,

        "branch": student.branch,

        "year": student.year,

        "graduation_year": student.graduation_year,

        "cgpa": student.cgpa,

        "tenth_marks": student.tenth_marks,

        "twelfth_marks": student.twelfth_marks,

        "address": student.address,

        "skills": student.skills,

        "profile_completed": student.profile_completed,

        "resume_path": student.resume_path,

        "created_at": student.created_at

    }, 200