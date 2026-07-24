import csv
import os
from io import StringIO
from datetime import datetime
from zoneinfo import ZoneInfo

from celery_worker import celery
from extensions import db

from models.export_job import ExportJob
from models.student import Student
from models.application import Application


@celery.task(
    name="tasks.student_export_tasks.export_my_applications_csv"
)
def export_my_applications_csv(export_id, student_user_id):

    job = db.session.get(
        ExportJob,
        export_id
    )

    if not job:
        return {
            "message": "Export job not found"
        }

    try:

        job.status = "PROCESSING"
        db.session.commit()

        student = db.session.get(
            Student,
            student_user_id
        )

        if not student:
            job.status = "FAILED"
            job.error_message = "Student not found"
            db.session.commit()

            return {
                "message": "Student not found"
            }

        applications = (
            Application.query
            .filter_by(student_id=student_user_id)
            .order_by(Application.application_date.desc())
            .all()
        )

        output = StringIO()
        writer = csv.writer(output)

        writer.writerow([
            "Application ID",
            "Student ID",
            "Student Name",
            "Company",
            "Placement Drive",
            "Status",
            "Applied Date"
        ])

        for application in applications:

            writer.writerow([
                application.application_id,
                student.user_id,
                student.full_name,
                application.drive.company.company_name,
                application.drive.job_title,
                application.status,
                application.application_date
            ])

        BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        EXPORT_DIR = os.path.abspath(
            os.path.join(BASE_DIR, "..", "exports")
        )

        os.makedirs(
            EXPORT_DIR,
            exist_ok=True
        )

        filename = (
            f"student_{student.user_id}_"
            f"{int(datetime.now(ZoneInfo('Asia/Kolkata')).timestamp())}.csv"
        )

        file_path = os.path.join(
            EXPORT_DIR,
            filename
        )

        with open(
            file_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            file.write(output.getvalue())

        job.status = "COMPLETED"
        job.file_path = file_path
        job.completed_at = datetime.now(
            ZoneInfo("Asia/Kolkata")
        ).replace(tzinfo=None)


        print("Student User ID:", student_user_id)
        print("Applications:", applications)
        print("Count:", len(applications))
        db.session.commit()
        
        from tasks.notification_tasks import send_notification

        send_notification.delay(
            [student_user_id],
            "CSV Export Ready",
            "Your placement applications CSV has been generated successfully.",
            "EXPORT"
        )

        return {
            "message": "Student export completed",
            "file": file_path
        }

    except Exception as e:

        db.session.rollback()

        job.status = "FAILED"
        job.error_message = str(e)

        db.session.commit()

        return {
            "message": str(e)
        }