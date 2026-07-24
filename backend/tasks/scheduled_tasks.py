# from datetime import datetime, timedelta
# from zoneinfo import ZoneInfo

# from celery_worker import celery

# from models.student import Student
# from models.application import Application
# from models.placement_drive import PlacementDrive

# from tasks.notification_tasks import send_notification


# @celery.task(
#     name="tasks.scheduled_tasks.daily_reminder"
# )
# def daily_reminder():

#     today = datetime.now(
#         ZoneInfo("Asia/Kolkata")
#     ).date()

#     tomorrow = today + timedelta(days=1)

#     reminders = 0

#     drives = (
#         PlacementDrive.query
#         .filter(
#             PlacementDrive.status == "Approved"
#         )
#         .all()
#     )

#     for drive in drives:

#         if not drive.application_deadline:
#             continue

#         # if drive.application_deadline not in [today, tomorrow]:
#         #     continue

#         students = Student.query.all()

#         for student in students:

#             if (
#                 drive.eligible_year
#                 and student.year != drive.eligible_year
#             ):
#                 continue

#             if (
#                 drive.eligible_cgpa
#                 and (
#                     student.cgpa is None
#                     or student.cgpa < drive.eligible_cgpa
#                 )
#             ):
#                 continue

#             if (
#                 drive.eligible_branches
#                 and student.branch
#                 not in [
#                     branch.strip()
#                     for branch in drive.eligible_branches.split(",")
#                 ]
#             ):
#                 continue

#             already_applied = (
#                 Application.query.filter_by(
#                     student_id=student.user_id,
#                     drive_id=drive.drive_id
#                 ).first()
#             )
            

#             if already_applied:
#                 continue

#             send_notification.delay(
#                 [student.user_id],
#                 "Placement Reminder",
#                 f"""You have not applied for

#             Company : {drive.company.company_name}

#             Role : {drive.job_title}

#             Deadline : {drive.application_deadline}

#             Apply before the deadline.""",
#                 "REMINDER"
#             )

#             reminders += 1

#     return {
#         "message": f"{reminders} reminders queued."
#     }


from datetime import date

from celery_worker import celery

from models.student import Student
from models.placement_drive import PlacementDrive
from models.application import Application
from tasks.notification_tasks import send_notification


@celery.task(
    name="tasks.scheduled_tasks.daily_reminder"
)
def daily_reminder():

    today = date.today()

    drives = PlacementDrive.query.filter_by(
        status="Approved"
    ).all()

    print("\n========== DAILY REMINDER DEBUG ==========")
    print("Today:", today)
    print("Approved Drives:", len(drives))

    reminder_count = 0

    for drive in drives:

        print("\n----------------------------------------")
        print("Drive:", drive.job_title)
        print("Company:", drive.company.company_name)
        print("Deadline:", drive.application_deadline)
        print("Eligible Branches:", drive.eligible_branches)
        print("Eligible Year:", drive.eligible_year)
        print("Eligible CGPA:", drive.eligible_cgpa)

        students = Student.query.all()

        print("Total Students:", len(students))

        for student in students:

            print("\nChecking Student:", student.full_name)
            print("User ID:", student.user_id)
            print("Branch:", student.branch)
            print("Year:", student.year)
            print("CGPA:", student.cgpa)

            # Year Check
            if (
                drive.eligible_year
                and student.year != drive.eligible_year
            ):
                print("❌ Skipped -> Year mismatch")
                continue

            # Branch Check
            if drive.eligible_branches:

                branches = [
                    b.strip()
                    for b in drive.eligible_branches.split(",")
                ]

                if student.branch not in branches:
                    print("❌ Skipped -> Branch mismatch")
                    continue

            # CGPA Check
            if (
                drive.eligible_cgpa
                and (
                    student.cgpa is None
                    or student.cgpa < drive.eligible_cgpa
                )
            ):
                print("❌ Skipped -> CGPA mismatch")
                continue

            # Already Applied Check
            already_applied = Application.query.filter_by(
                student_id=student.user_id,
                drive_id=drive.drive_id
            ).first()

            if already_applied:
                print("❌ Skipped -> Already applied")
                continue

            print("✅ Reminder will be sent!")

            send_notification.delay(
                [student.user_id],
                "Placement Reminder",
                f"""
You have not applied for:

Company : {drive.company.company_name}

Role : {drive.job_title}

Deadline : {drive.application_deadline}

Apply before the deadline.
""",
                "REMINDER"
            )

            reminder_count += 1

    print("\n====================================")
    print("TOTAL REMINDERS QUEUED:", reminder_count)
    print("====================================")

    return {
        "message": f"{reminder_count} reminders queued."
        
    }
    
    
    
    

from tasks.admin_report_tasks import generate_monthly_report
from models.export_job import ExportJob
from extensions import db


@celery.task(
    name="tasks.scheduled_tasks.monthly_report_scheduler"
)
def monthly_report_scheduler():

    # Choose your admin id
    admin_user_id = 1

    job = ExportJob(
        student_id=admin_user_id,
        status="PENDING"
    )

    db.session.add(job)
    db.session.commit()

    generate_monthly_report.delay(
        job.export_id,
        admin_user_id
    )

    return {
        "message": "Monthly report queued"
    }