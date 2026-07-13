from datetime import datetime

from sqlalchemy import or_

from extensions import db

from models.user import User
from models.company import Company
from models.placement_drive import PlacementDrive
from models.application import Application
from models.student import Student



# ==========================================================
# COMPANY DASHBOARD
# ==========================================================

def get_dashboard(user_id):

    company = Company.query.filter_by(
        user_id=user_id
    ).first()

    if not company:

        return {
            "message":"Company not found"
        },404


    drives = PlacementDrive.query.filter_by(
        company_id=user_id
    ).all()


    drive_ids = [drive.id for drive in drives]


    applications = Application.query.filter(
        Application.drive_id.in_(drive_ids)
    ).all() if drive_ids else []


    recent = []

    for application in applications[-5:]:

        recent.append({

            "id": application.id,

            "student": application.student.full_name,

            "role": application.drive.role,

            "status": application.status

        })


    data = {

        "company_name": company.company_name,

        "total_drives": len(drives),

        "active_drives": len(
            [d for d in drives if d.status == "Approved"]
        ),

        "total_applications": len(applications),

        "shortlisted": len(
            [a for a in applications if a.status == "Shortlisted"]
        ),

        "selected": len(
            [a for a in applications if a.status == "Selected"]
        ),

        "recent_applications": recent

    }

    return data,200

# ==========================================================
# COMPANY PROFILE
# ==========================================================

def get_company_profile(user_id):

    company = Company.query.filter_by(
        user_id=user_id
    ).first()


    if not company:

        return {

            "message":"Company profile not found"

        },404



    return {

        "company_id":company.user_id,

        "company_name":company.company_name,

        "industry":company.industry,

        "location":company.location,

        "website":company.website,

        "hr_name":company.hr_name,

        "hr_email":company.hr_email

    },200





# ==========================================================
# CREATE PLACEMENT DRIVE
# ==========================================================

def create_drive(user_id,data):


    company = Company.query.filter_by(
        user_id=user_id
    ).first()



    if not company:

        return {

            "message":"Company not found"

        },404




    if not company.user.is_approved:


        return {

            "message":"Company approval pending"

        },403





    drive = PlacementDrive(

        company_id=company.user_id,

        role=data.get("role"),

        description=data.get("description"),

        package=data.get("package"),

        location=data.get("location"),

        eligibility=data.get("eligibility"),

        deadline=data.get("deadline"),

        status="Pending",

        created_at=datetime.utcnow()

    )


    db.session.add(drive)

    db.session.commit()



    return {

        "message":"Placement drive created successfully",

        "drive_id":drive.id

    },201






# ==========================================================
# GET COMPANY DRIVES
# ==========================================================

def get_company_drives(user_id):


    drives = PlacementDrive.query.filter_by(

        company_id=user_id

    ).all()



    data=[]


    for drive in drives:


        data.append({

            "id":drive.id,

            "role":drive.role,

            "package":drive.package,

            "location":drive.location,

            "deadline":drive.deadline,

            "status":drive.status

        })



    return data,200





# ==========================================================
# UPDATE DRIVE
# ==========================================================

def update_drive(user_id,drive_id,data):


    drive = PlacementDrive.query.filter_by(

        id=drive_id,

        company_id=user_id

    ).first()



    if not drive:


        return {

            "message":"Drive not found"

        },404




    drive.role=data.get(
        "role",
        drive.role
    )


    drive.description=data.get(
        "description",
        drive.description
    )


    drive.package=data.get(
        "package",
        drive.package
    )


    drive.location=data.get(
        "location",
        drive.location
    )


    drive.deadline=data.get(
        "deadline",
        drive.deadline
    )


    db.session.commit()



    return {

        "message":"Drive updated successfully"

    },200






# ==========================================================
# DELETE DRIVE
# ==========================================================

def delete_drive(user_id,drive_id):


    drive=PlacementDrive.query.filter_by(

        id=drive_id,

        company_id=user_id

    ).first()



    if not drive:


        return {

            "message":"Drive not found"

        },404



    db.session.delete(drive)

    db.session.commit()



    return {

        "message":"Drive deleted successfully"

    },200






# ==========================================================
# VIEW APPLICATIONS
# ==========================================================

def get_drive_applications(user_id,drive_id):


    drive=PlacementDrive.query.filter_by(

        id=drive_id,

        company_id=user_id

    ).first()



    if not drive:


        return {

            "message":"Drive not found"

        },404





    applications=Application.query.filter_by(

        drive_id=drive_id

    ).all()



    data=[]



    for application in applications:


        student=application.student



        data.append({

            "application_id":application.id,

            "student_id":student.user_id,

            "student_name":student.name,

            "branch":student.branch,

            "cgpa":student.cgpa,

            "resume":student.resume,

            "status":application.status

        })



    return data,200






# ==========================================================
# UPDATE APPLICATION STATUS
# ==========================================================

def update_application_status(

        user_id,

        application_id,

        status

):


    application=Application.query.get(
        application_id
    )



    if not application:


        return {

            "message":"Application not found"

        },404





    if application.drive.company_id != user_id:


        return {

            "message":"Unauthorized access"

        },403




    allowed=[

        "Shortlisted",

        "Rejected",

        "Selected"

    ]



    if status not in allowed:


        return {

            "message":"Invalid status"

        },400




    application.status=status


    db.session.commit()



    return {

        "message":"Application status updated"

    },200
    
    
    
    
# ==========================================================
# CLOSE PLACEMENT DRIVE
# ==========================================================

def close_drive(user_id, drive_id):


    drive = PlacementDrive.query.filter_by(

        id=drive_id,

        company_id=user_id

    ).first()



    if not drive:

        return {

            "message":"Drive not found"

        },404




    if drive.status == "Closed":

        return {

            "message":"Drive already closed"

        },400




    drive.status = "Closed"



    db.session.commit()



    return {

        "message":"Drive closed successfully"

    },200
    
    
    
    
# ==========================================================
# GET SELECTED STUDENTS
# ==========================================================

def get_selected_students(user_id):


    applications = Application.query.join(

        PlacementDrive,

        Application.drive_id == PlacementDrive.id

    ).filter(

        PlacementDrive.company_id == user_id,

        Application.status == "Selected"

    ).all()



    data = []



    for application in applications:


        student = application.student

        drive = application.drive



        data.append({

            "application_id": application.id,

            "student": student.full_name,

            "roll_number": student.roll_number,

            "branch": student.branch,

            "cgpa": student.cgpa,

            "role": drive.role,

            "package": drive.package,

            "selection_date": application.created_at

        })



    return data,200




# ==========================================================
# GET STUDENT DETAILS
# ==========================================================

def get_student_details(user_id, student_id):

    student = Student.query.filter_by(
        user_id=student_id
    ).first()

    if not student:

        return {
            "message":"Student not found"
        },404


    # Verify that this student has applied to one of the
    # current company's placement drives
    has_application = Application.query.join(
        PlacementDrive
    ).filter(
        Application.student_id == student.user_id,
        PlacementDrive.company_id == user_id
    ).first()

    if not has_application:

        return {
            "message":"Unauthorized access"
        },403


    return {

        "student_id":student.user_id,

        "full_name":student.full_name,

        "email":student.user.email,

        "phone":student.phone,

        "branch":student.branch,

        "year":student.year,

        "cgpa":student.cgpa,

        "skills":student.skills,

        "resume":student.resume_path

    },200