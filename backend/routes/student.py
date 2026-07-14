from flask import Blueprint, request, jsonify
from extensions import db

from models.notification import Notification

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


from services.student_service import (

    get_student_profile,

    get_available_drives,

    get_drive_details,

    apply_for_drive,

    get_my_applications,

    withdraw_application,

    student_dashboard,

    export_student_csv
    

)


from utils.decorators import student_required





# ==========================================================
# STUDENT BLUEPRINT
# ==========================================================

student_bp = Blueprint(

    "student",

    __name__,

    url_prefix="/api/student"

)







# ==========================================================
# STUDENT PROFILE
# ==========================================================

@student_bp.route(

    "/profile",

    methods=["GET"]

)
@jwt_required()
@student_required
def profile():


    user_id = get_jwt_identity()



    data,status = get_student_profile(

        user_id

    )



    return jsonify(data),status







# ==========================================================
# AVAILABLE PLACEMENT DRIVES
# ==========================================================

@student_bp.route(

    "/drives",

    methods=["GET"]

)
@jwt_required()
@student_required
def available_drives():


    search=request.args.get(

        "search"

    )



    data,status=get_available_drives(

        search

    )



    return jsonify(data),status







# ==========================================================
# APPLY FOR DRIVE
# ==========================================================

@student_bp.route(

    "/drives/<int:drive_id>/apply",

    methods=["POST"]

)
@jwt_required()
@student_required
def apply_drive(drive_id):


    user_id=get_jwt_identity()



    data,status=apply_for_drive(

        user_id,

        drive_id

    )



    return jsonify(data),status







# ==========================================================
# MY APPLICATIONS
# ==========================================================

@student_bp.route(

    "/applications",

    methods=["GET"]

)
@jwt_required()
@student_required
def applications():


    user_id=get_jwt_identity()



    data,status=get_my_applications(

        user_id

    )



    return jsonify(data),status







# ==========================================================
# WITHDRAW APPLICATION
# ==========================================================

@student_bp.route(

    "/applications/<int:application_id>/withdraw",

    methods=["DELETE"]

)
@jwt_required()
@student_required
def withdraw(application_id):


    user_id=get_jwt_identity()



    data,status=withdraw_application(

        user_id,

        application_id

    )



    return jsonify(data),status







# ==========================================================
# STUDENT DASHBOARD
# ==========================================================

@student_bp.route(

    "/dashboard",

    methods=["GET"]

)
@jwt_required()
@student_required
def dashboard():


    user_id=get_jwt_identity()



    data,status=student_dashboard(

        user_id

    )



    return jsonify(data),status




# ==========================================================
# DRIVE DETAILS
# ==========================================================

@student_bp.route(
    "/drives/<int:drive_id>",
    methods=["GET"]
)
@jwt_required()
@student_required
def drive_details(drive_id):

    user_id = get_jwt_identity()

    data,status = get_drive_details(
        drive_id
    )

    return jsonify(data),status


# ==========================================================
# EXPORT APPLICATIONS CSV
# ==========================================================

@student_bp.route(

    "/export",

    methods=["GET"]

)
@jwt_required()
@student_required
def export_applications_csv():


    user_id = get_jwt_identity()


    return export_student_csv(

        user_id

    )
    
    
    
@student_bp.route("/notifications", methods=["GET"])
@jwt_required()
def get_notifications():

    user_id = get_jwt_identity()

    notifications = Notification.query.filter_by(
        user_id=user_id
    ).order_by(
        Notification.created_at.desc()
    ).all()

    return jsonify([
        {
            "id": n.notification_id,
            "title": n.title,
            "message": n.message,
            "type": n.notification_type,
            "read": n.is_read,
            "created_at": n.created_at
        }
        for n in notifications
    ])
    
    
@student_bp.route(
    "/notifications/<int:id>/read",
    methods=["PUT"]
)
@jwt_required()
def mark_notification(id):

    user_id = get_jwt_identity()

    notification = Notification.query.filter_by(
        notification_id=id,
        user_id=user_id
    ).first()

    if not notification:
        return {"message": "Notification not found"},404

    notification.is_read=True

    db.session.commit()

    return {"message":"Notification updated"}



@student_bp.route(
    "/notifications/count",
    methods=["GET"]
)
@jwt_required()
def notification_count():

    user=get_jwt_identity()

    count=Notification.query.filter_by(
        user_id=user,
        is_read=False
    ).count()

    return {"count":count}