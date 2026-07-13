from datetime import datetime

from sqlalchemy import or_

from extensions import db

from models.student import Student
from models.placement_drive import PlacementDrive
from models.application import Application



import csv

from io import StringIO

from flask import Response

# ==========================================================
# STUDENT PROFILE
# ==========================================================

def get_student_profile(user_id):


    student = Student.query.filter_by(

        user_id=user_id

    ).first()



    if not student:

        return {

            "message":"Student profile not found"

        },404





    return {

        "student_id":student.user_id,

        "name":student.name,

        "phone":student.phone,

        "branch":student.branch,

        "cgpa":student.cgpa,

        "graduation_year":student.graduation_year,

        "resume":student.resume

    },200







# ==========================================================
# GET AVAILABLE PLACEMENT DRIVES
# ==========================================================

def get_available_drives(search=None):


    query = PlacementDrive.query.filter_by(

        status="Approved"

    )



    if search:


        query=query.filter(

            or_(

                PlacementDrive.role.ilike(

                    f"%{search}%"

                ),

                PlacementDrive.location.ilike(

                    f"%{search}%"

                )

            )

        )





    drives=query.all()



    data=[]



    for drive in drives:


        data.append({

            "drive_id":drive.id,

            "company":drive.company.company_name,

            "role":drive.role,

            "description":drive.description,

            "package":drive.package,

            "location":drive.location,

            "eligibility":drive.eligibility,

            "deadline":drive.deadline

        })




    return data,200







# ==========================================================
# APPLY FOR PLACEMENT DRIVE
# ==========================================================

def apply_for_drive(user_id,drive_id):


    student=Student.query.filter_by(

        user_id=user_id

    ).first()



    if not student:


        return {

            "message":"Student not found"

        },404






    drive=PlacementDrive.query.get(

        drive_id

    )



    if not drive:


        return {

            "message":"Drive not found"

        },404






    if drive.status!="Approved":


        return {

            "message":"Drive is not active"

        },400





    existing=Application.query.filter_by(

        student_id=user_id,

        drive_id=drive_id

    ).first()



    if existing:


        return {

            "message":"Already applied"

        },400







    application=Application(

        student_id=user_id,

        drive_id=drive_id,

        status="Applied",

        created_at=datetime.utcnow()

    )



    db.session.add(application)

    db.session.commit()



    return {

        "message":"Applied successfully",

        "application_id":application.id

    },201







# ==========================================================
# MY APPLICATIONS
# ==========================================================

def get_my_applications(user_id):


    applications=Application.query.filter_by(

        student_id=user_id

    ).all()



    data=[]



    for application in applications:


        drive=application.drive



        data.append({

            "application_id":application.id,

            "company":drive.company.company_name,

            "role":drive.role,

            "status":application.status,

            "applied_date":application.created_at

        })



    return data,200







# ==========================================================
# WITHDRAW APPLICATION
# ==========================================================

def withdraw_application(user_id,application_id):


    application=Application.query.filter_by(

        id=application_id,

        student_id=user_id

    ).first()



    if not application:


        return {

            "message":"Application not found"

        },404






    if application.status!="Applied":


        return {

            "message":

            "Cannot withdraw after processing"

        },400





    db.session.delete(application)

    db.session.commit()



    return {

        "message":"Application withdrawn"

    },200







# ==========================================================
# STUDENT DASHBOARD
# ==========================================================

# ==========================================================
# STUDENT DASHBOARD
# ==========================================================

def student_dashboard(user_id):


    student = Student.query.filter_by(

        user_id=user_id

    ).first()



    if not student:


        return {

            "message":"Student not found"

        },404





    # Total approved drives available

    total_drives = PlacementDrive.query.filter_by(

        status="Approved"

    ).count()





    # Student applications

    applications = Application.query.filter_by(

        student_id=user_id

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


    fields = [

        student.name,

        student.phone,

        student.branch,

        student.cgpa,

        student.graduation_year,

        student.resume

    ]



    completed = 0



    for field in fields:


        if field:


            completed += 1




    profile_completion = int(

        (completed / len(fields)) * 100

    )






    # ======================================================
    # RECENT APPLICATIONS
    # ======================================================


    recent_applications = []



    for application in applications[:5]:


        drive = application.drive



        recent_applications.append({


            "id": application.id,


            "company": drive.company.company_name,


            "role": drive.role,


            "status": application.status,


            "date": application.created_at.strftime(

                "%Y-%m-%d"

            )



        })







    # ======================================================
    # FINAL RESPONSE
    # ======================================================


    return {


        "name": student.name,


        "total_drives": total_drives,


        "applied_drives": applied_drives,


        "shortlisted": shortlisted,


        "selected": selected,


        "rejected": rejected,


        "profile_completion": profile_completion,


        "recent_applications": recent_applications



    },200
    
    
    
# ==========================================================
# GET SINGLE DRIVE DETAILS
# ==========================================================

def get_drive_details(drive_id):

    drive = PlacementDrive.query.get(

        drive_id

    )

    if not drive:

        return {

            "message":"Drive not found"

        },404



    if drive.status != "Approved":

        return {

            "message":"Drive is not available"

        },400



    return {

        "drive_id":drive.id,

        "company":drive.company.company_name,

        "role":drive.role,

        "description":drive.description,

        "package":drive.package,

        "location":drive.location,

        "eligibility":drive.eligibility,

        "deadline":

            drive.deadline.strftime("%Y-%m-%d")

            if drive.deadline

            else None

    },200
    
    
    
# ==========================================================
# EXPORT APPLICATIONS CSV
# ==========================================================

def export_student_csv(user_id):

    applications = Application.query.filter_by(

        student_id=user_id

    ).all()



    output = StringIO()

    writer = csv.writer(output)



    writer.writerow([

        "Company",

        "Role",

        "Status",

        "Applied Date"

    ])



    for application in applications:

        drive = application.drive

        company = drive.company



        writer.writerow([

            company.company_name,

            drive.role,

            application.status,

            application.created_at.strftime(

                "%Y-%m-%d %H:%M"

            )

            if application.created_at

            else ""

        ])



    csv_data = output.getvalue()

    output.close()



    return Response(

        csv_data,

        mimetype="text/csv",

        headers={

            "Content-Disposition":

            "attachment; filename=applications.csv"

        }

    )