import csv

from io import StringIO

from datetime import datetime

from celery_worker import celery

from extensions import db

from models.export_job import ExportJob

from models.application import Application


@celery.task(
    name="tasks.export_tasks.export_applications_csv"
)
def export_applications_csv(job_id):


    job = ExportJob.query.get(job_id)


    if not job:

        return {
            "message": "Export job not found"
        }



    try:

        job.status = "PROCESSING"

        db.session.commit()



        applications = Application.query.all()



        output = StringIO()


        writer = csv.writer(output)


        writer.writerow([

            "Application ID",

            "Student",

            "Company",

            "Role",

            "Status",

            "Applied Date"

        ])




        for application in applications:


            writer.writerow([

                application.application_id,

                application.student.full_name,

                application.drive.company.company_name,

                application.drive.job_title,

                application.status,

                application.application_date

            ])




        filename = (

            f"applications_{datetime.utcnow().timestamp()}.csv"

        )



        file_path = (

            f"exports/{filename}"

        )



        with open(
            file_path,
            "w",
            newline=""
        ) as file:

            file.write(
                output.getvalue()
            )



        job.status = "COMPLETED"

        job.file_path = file_path

        job.completed_at = datetime.utcnow()



        db.session.commit()



        return {

            "message": "Export completed",

            "file": file_path

        }



    except Exception as e:


        job.status = "FAILED"

        db.session.commit()


        return {

            "error": str(e)

        }