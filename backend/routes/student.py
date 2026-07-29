from flask import Blueprint, request, jsonify,send_file
from extensions import db
import os
from models.notification import Notification
from models.student import Student
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


from services.student_service import (


    update_student_profile,
    get_student_profile,

    get_available_drives,

    get_drive_details,

    apply_for_drive,

    get_my_applications,

    withdraw_application,

    student_dashboard,

    export_my_applications,
    

)


from utils.decorators import student_required




student_bp = Blueprint(

    "student",

    __name__,

    url_prefix="/api/student"

)






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



@student_bp.route("/export-applications", methods=["POST"])
@jwt_required()
@student_required
def export_applications_route():

    data, status = export_my_applications()

    return jsonify(data), status
    
    



@student_bp.route(
"/profile",
    methods=["PUT"]
)
@jwt_required()
def update_profile():

    user_id = get_jwt_identity()

    data = request.get_json()

    response, status = update_student_profile(
        user_id,
        data
    )

    return jsonify(response), status





@student_bp.route(

    "/resume/download",

    methods=["GET"]

)
@jwt_required()
@student_required
def download_resume():

    import os
    from flask import send_file, jsonify

    user_id = get_jwt_identity()

    student = Student.query.filter_by(

        user_id=user_id

    ).first()

    if not student or not student.resume_path:

        return jsonify({

            "message":"Resume not found"

        }),404

    file_path = os.path.abspath(

        student.resume_path

    )

    if not os.path.exists(file_path):

        return jsonify({

            "message":"File not found"

        }),404

    return send_file(

        file_path,

        as_attachment=True

    )