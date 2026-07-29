from flask import Blueprint, request, jsonify

from flask_jwt_extended import jwt_required

from services.auth_service import (
    login_user,
    register_student,
    register_company,
    get_profile,
    update_student_profile,
    upload_resume,
    update_company_profile
)


auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)



@auth_bp.post("/login")
def login():

    data = request.get_json()

    return login_user(data)



@auth_bp.post("/register/student")
def student_register():

    return register_student(
        request.form,
        request.files.get("resume")
    )



@auth_bp.post("/register/company")
def company_register():

    data = request.get_json()

    return register_company(data)




@auth_bp.get("/profile")
@jwt_required()
def profile():

    return get_profile()




@auth_bp.put("/student/profile")
@jwt_required()
def edit_student_profile():

    data = request.get_json()

    return update_student_profile(data)




@auth_bp.post("/student/resume")
@jwt_required()
def student_resume():

    return upload_resume(
        request.files.get("resume")
    )




@auth_bp.put("/company/profile")
@jwt_required()
def update_company():

    data = request.get_json()

    response, status = update_company_profile(
        data
    )

    return jsonify(response), status