import os

import pandas as pd

from celery_app import celery

from models.application import Application
from models.placement_drive import PlacementDrive
from models.company import Company


@celery.task
def export_student_applications(student_id):

    applications = Application.query.filter_by(
        student_id=student_id
    ).all()

    rows = []

    for application in applications:

        drive = application.drive

        company = drive.company

        rows.append({

            "Application ID": application.id,

            "Company": company.company_name,

            "Role": drive.role,

            "Package": drive.package,

            "Location": drive.location,

            "Status": application.status,

            "Applied On": application.created_at

        })



    os.makedirs("exports", exist_ok=True)

    filename = f"exports/student_{student_id}_applications.csv"

    dataframe = pd.DataFrame(rows)

    dataframe.to_csv(

        filename,

        index=False

    )

    return filename