from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from services.notification_service import (
    get_notifications,
    mark_notification_read,
    delete_notification,
    unread_count
)
from services.company_service import (
    
    get_dashboard,

    get_company_profile,

    create_drive,

    get_company_drives,

    update_drive,

    delete_drive,

    close_drive,
    
    get_student_details,

    get_drive_applications,

    update_application_status,

    get_selected_students

)


from utils.decorators import company_required



# ==========================================================
# COMPANY BLUEPRINT
# ==========================================================

company_bp = Blueprint(

    "company",

    __name__,

    url_prefix="/api/company"

)





# ==========================================================
# COMPANY PROFILE
# ==========================================================

@company_bp.route(

    "/profile",

    methods=["GET"]

)
@jwt_required()
@company_required
def profile():


    user_id = get_jwt_identity()


    data,status = get_company_profile(

        user_id

    )


    return jsonify(data),status






# ==========================================================
# CREATE PLACEMENT DRIVE
# ==========================================================

@company_bp.route(

    "/drives",

    methods=["POST"]

)
@jwt_required()
@company_required
def create_placement_drive():


    user_id=get_jwt_identity()


    data=request.get_json()



    result,status=create_drive(

        user_id,

        data

    )


    return jsonify(result),status







# ==========================================================
# GET COMPANY DRIVES
# ==========================================================

@company_bp.route(

    "/drives",

    methods=["GET"]

)
@jwt_required()
@company_required
def company_drives():


    user_id=get_jwt_identity()



    data,status=get_company_drives(

        user_id

    )


    return jsonify(data),status







# ==========================================================
# UPDATE DRIVE
# ==========================================================

@company_bp.route(

    "/drives/<int:drive_id>",

    methods=["PUT"]

)
@jwt_required()
@company_required
def update_placement_drive(drive_id):


    user_id=get_jwt_identity()


    data=request.get_json()



    result,status=update_drive(

        user_id,

        drive_id,

        data

    )


    return jsonify(result),status







# ==========================================================
# DELETE DRIVE
# ==========================================================

@company_bp.route(

    "/drives/<int:drive_id>",

    methods=["DELETE"]

)
@jwt_required()
@company_required
def remove_drive(drive_id):


    user_id=get_jwt_identity()



    result,status=delete_drive(

        user_id,

        drive_id

    )


    return jsonify(result),status







# ==========================================================
# VIEW DRIVE APPLICATIONS
# ==========================================================

@company_bp.route(
    "/applications",
    methods=["GET"]
)
@jwt_required()
@company_required
def company_applications():

    user_id = get_jwt_identity()

    data, status = get_drive_applications(user_id)

    return jsonify(data), status







# ==========================================================
# UPDATE APPLICATION STATUS
# ==========================================================

@company_bp.route(

    "/applications/<int:application_id>/status",

    methods=["PUT"]

)
@jwt_required()
@company_required
def change_application_status(application_id):


    user_id=int(get_jwt_identity())



    body=request.get_json()



    status=body.get(

        "status"

    )



    result,response_status=update_application_status(

        user_id,

        application_id,

        status

    )


    return jsonify(result),response_status



# ==========================================================
# CLOSE DRIVE
# ==========================================================

@company_bp.route(

    "/drives/<int:drive_id>/close",

    methods=["PUT"]

)
@jwt_required()
@company_required
def close_placement_drive(drive_id):


    user_id = get_jwt_identity()



    result,status = close_drive(

        user_id,

        drive_id

    )



    return jsonify(result),status



# ==========================================================
# SELECTED STUDENTS
# ==========================================================

@company_bp.route(

    "/selected-students",

    methods=["GET"]

)
@jwt_required()
@company_required
def selected_students():

    user_id = get_jwt_identity()

    data,status = get_selected_students(

        user_id

    )

    return jsonify(data),status



# ==========================================================
# STUDENT DETAILS
# ==========================================================

@company_bp.route(

    "/students/<int:student_id>",

    methods=["GET"]

)
@jwt_required()
@company_required
def student_details(student_id):


    user_id = get_jwt_identity()


    data,status = get_student_details(

        user_id,

        student_id

    )


    return jsonify(data),status



# ==========================================================
# COMPANY DASHBOARD
# ==========================================================

@company_bp.route(
    "/dashboard",
    methods=["GET"]
)
@jwt_required()
@company_required
def dashboard():

    user_id = get_jwt_identity()

    data,status = get_dashboard(user_id)

    return jsonify(data),status