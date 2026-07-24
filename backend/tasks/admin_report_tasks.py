import csv
import os
from datetime import datetime
from zoneinfo import ZoneInfo

from celery_worker import celery
from extensions import db

from models.export_job import ExportJob
from models.placement_drive import PlacementDrive


@celery.task(
    name="tasks.admin_report_tasks.generate_monthly_report"
)
def generate_monthly_report(export_id, admin_user_id):

    job = db.session.get(
        ExportJob,
        export_id
    )

    if not job:
        return {"message": "Export job not found"}

    try:

        job.status = "PROCESSING"
        db.session.commit()

        output = []

        drives = PlacementDrive.query.all()

        BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        EXPORT_DIR = os.path.abspath(
            os.path.join(BASE_DIR, "..", "exports")
        )

        os.makedirs(EXPORT_DIR, exist_ok=True)

        filename = (
            f"placement_report_"
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
        ) as csv_file:

            writer = csv.writer(csv_file)

            writer.writerow([
                "Drive ID",
                "Company",
                "Job Title",
                "Applications",
                "Applied",
                "Shortlisted",
                "Selected",
                "Rejected",
                "Deadline"
            ])

            for drive in drives:

                applied = 0
                shortlisted = 0
                selected = 0
                rejected = 0

                for app in drive.applications:

                    if app.status == "Applied":
                        applied += 1

                    elif app.status == "Shortlisted":
                        shortlisted += 1

                    elif app.status == "Selected":
                        selected += 1

                    elif app.status == "Rejected":
                        rejected += 1

                writer.writerow([
                    drive.drive_id,
                    drive.company.company_name,
                    drive.job_title,
                    len(drive.applications),
                    applied,
                    shortlisted,
                    selected,
                    rejected,
                    drive.application_deadline
                ])

        job.status = "COMPLETED"
        job.file_path = file_path
        job.completed_at = datetime.now(
            ZoneInfo("Asia/Kolkata")
        ).replace(tzinfo=None)

        db.session.commit()

        return {
            "message": "Monthly report generated",
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