from flask import Blueprint, request, jsonify
from flask import send_file
from models.export_job import ExportJob
from flask_jwt_extended import jwt_required

from services.notification_service import (
    get_notifications,
    mark_notification_read,
    delete_notification,
    unread_count
)

from services.admin_service import (

    admin_dashboard,

    get_all_companies,
    approve_company,
    reject_company,
    blacklist_company,

    get_all_students,
    toggle_student_status,

    get_all_drives,
    approve_drive,
    reject_drive,
    close_drive,

    get_all_applications,
    update_application_status,

    placement_statistics,
    get_student_details,
    get_drive_details,
    create_export_job,
    get_export_status,
    get_all_exports,
    download_export,

    download_export

)

from utils.decorators import admin_required


# ==========================================================
# ADMIN BLUEPRINT
# ==========================================================

admin_bp = Blueprint(

    "admin",

    __name__,

    url_prefix="/api/admin"

)


# ==========================================================
# ADMIN DASHBOARD
# ==========================================================

@admin_bp.route(
    "/dashboard",
    methods=["GET"]
)
@jwt_required()
@admin_required
def dashboard():

    data, status_code = admin_dashboard()

    return jsonify(data), status_code


# ==========================================================
# COMPANY MANAGEMENT
# ==========================================================

@admin_bp.route(
    "/companies",
    methods=["GET"]
)
@jwt_required()
@admin_required
def companies():

    search = request.args.get("search")

    data, status_code = get_all_companies(search)

    return jsonify(data), status_code


@admin_bp.route(
    "/companies/<int:user_id>/approve",
    methods=["PUT"]
)
@jwt_required()
@admin_required
def approve_company_route(user_id):

    data, status_code = approve_company(user_id)

    return jsonify(data), status_code


@admin_bp.route(
    "/companies/<int:user_id>/reject",
    methods=["DELETE"]
)
@jwt_required()
@admin_required
def reject_company_route(user_id):

    data, status_code = reject_company(user_id)

    return jsonify(data), status_code


@admin_bp.route(
    "/companies/<int:user_id>/blacklist",
    methods=["PUT"]
)
@jwt_required()
@admin_required
def blacklist_company_route(user_id):

    data, status_code = blacklist_company(user_id)

    return jsonify(data), status_code


# ==========================================================
# STUDENT MANAGEMENT
# ==========================================================

@admin_bp.route(
    "/students",
    methods=["GET"]
)
@jwt_required()
@admin_required
def students():

    search = request.args.get("search")

    data, status_code = get_all_students(search)

    return jsonify(data), status_code


@admin_bp.route(
    "/students/<int:user_id>/toggle",
    methods=["PUT"]
)
@jwt_required()
@admin_required
def toggle_student(user_id):

    data, status_code = toggle_student_status(user_id)

    return jsonify(data), status_code




@admin_bp.route(
    "/students/<int:user_id>",
    methods=["GET"]
)
@jwt_required()
@admin_required
def student_details(user_id):

    data, status = get_student_details(user_id)

    return jsonify(data), status
# ==========================================================
# PLACEMENT DRIVE MANAGEMENT
# ==========================================================

@admin_bp.route(
    "/drives",
    methods=["GET"]
)
@jwt_required()
@admin_required
def drives():

    search = request.args.get("search")

    data, status_code = get_all_drives(search)

    return jsonify(data), status_code


@admin_bp.route(
    "/drives/<int:drive_id>/approve",
    methods=["PUT"]
)
@jwt_required()
@admin_required
def approve_drive_route(drive_id):

    data, status_code = approve_drive(drive_id)

    return jsonify(data), status_code


@admin_bp.route(
    "/drives/<int:drive_id>/reject",
    methods=["PUT"]
)
@jwt_required()
@admin_required
def reject_drive_route(drive_id):

    data, status_code = reject_drive(drive_id)

    return jsonify(data), status_code


@admin_bp.route(
    "/drives/<int:drive_id>/close",
    methods=["PUT"]
)
@jwt_required()
@admin_required
def close_drive_route(drive_id):

    data, status_code = close_drive(drive_id)

    return jsonify(data), status_code

@admin_bp.route(
    "/drives/<int:drive_id>",
    methods=["GET"]
)
@jwt_required()
@admin_required
def drive_details(drive_id):

    data,status = get_drive_details(drive_id)

    return jsonify(data),status
# ==========================================================
# APPLICATION MANAGEMENT
# ==========================================================

@admin_bp.route(
    "/applications",
    methods=["GET"]
)
@jwt_required()
@admin_required
def applications():

    search = request.args.get("search")

    status = request.args.get("status")

    data, code = get_all_applications(

        search,

        status

    )

    return jsonify(data), code


@admin_bp.route(
    "/applications/<int:application_id>/status",
    methods=["PUT"]
)
@jwt_required()
@admin_required
def update_application(application_id):

    body = request.get_json() or {}

    status = body.get("status")

    if not status:

        return jsonify({

            "message": "Status is required"

        }), 400

    data, status_code = update_application_status(

        application_id,

        status

    )

    return jsonify(data), status_code


# ==========================================================
# ANALYTICS
# ==========================================================

@admin_bp.route(
    "/statistics",
    methods=["GET"]
)
@jwt_required()
@admin_required
def statistics():

    data, status_code = placement_statistics()

    return jsonify(data), status_code

from extensions import db



# ==========================================================
# CREATE EXPORT
# ==========================================================

@admin_bp.route(
    "/exports",
    methods=["POST"]
)
@jwt_required()
@admin_required
def create_export():

    body = request.get_json(silent=True) or {}

    student_id = body.get("student_id")

    data, status = create_export_job(student_id)

    return jsonify(data), status


# ==========================================================
# GET ALL EXPORTS
# ==========================================================

@admin_bp.route(
    "/exports",
    methods=["GET"]
)
@jwt_required()
@admin_required
def exports():

    data, status = get_all_exports()

    return jsonify(data), status


# ==========================================================
# GET EXPORT STATUS
# ==========================================================

@admin_bp.route(
    "/exports/<int:export_id>",
    methods=["GET"]
)
@jwt_required()
@admin_required
def export_status_route(export_id):

    data, status = get_export_status(export_id)

    return jsonify(data), status


# ==========================================================
# DOWNLOAD EXPORT
# ==========================================================

@admin_bp.route(
    "/exports/<int:export_id>/download",
    methods=["GET"]
)
@jwt_required()
@admin_required
def download_export_route(export_id):

    return download_export(export_id)


