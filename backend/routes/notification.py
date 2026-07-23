from flask import Blueprint, jsonify

from flask_jwt_extended import jwt_required
from flask import request
from utils.decorators import admin_required

from services.notification_service import (
    get_notifications,
    mark_notification_read,
    delete_notification,
    unread_count,
    create_notification
)
# ==========================================================
# NOTIFICATION BLUEPRINT
# ==========================================================

notification_bp = Blueprint(

    "notifications",

    __name__,

    url_prefix="/api/notifications"

)

@notification_bp.route("", methods=["POST"])
@jwt_required()
@admin_required
def send_notification():

    body = request.get_json()

    print(body)   # <-- add this

    data, status = create_notification(body)

    return jsonify(data), status
# ==========================================================
# GET ALL NOTIFICATIONS
# ==========================================================

@notification_bp.route(

    "",

    methods=["GET"]

)
@jwt_required()
def notifications():

    data, status = get_notifications()

    return jsonify(data), status


# ==========================================================
# MARK AS READ
# ==========================================================

@notification_bp.route(

    "/<int:notification_id>/read",

    methods=["PUT"]

)
@jwt_required()
def read_notification(notification_id):

    data, status = mark_notification_read(

        notification_id

    )

    return jsonify(data), status


# ==========================================================
# DELETE NOTIFICATION
# ==========================================================

@notification_bp.route(

    "/<int:notification_id>",

    methods=["DELETE"]

)
@jwt_required()
def remove_notification(notification_id):

    data, status = delete_notification(

        notification_id

    )

    return jsonify(data), status


# ==========================================================
# UNREAD COUNT
# ==========================================================

@notification_bp.route(

    "/unread-count",

    methods=["GET"]

)
@jwt_required()
def notification_count():

    data, status = unread_count()

    return jsonify(data), status


# ==========================================================
# CREATE NOTIFICATION (ADMIN)
# ==========================================================

# @notification_bp.route(
#     "",
#     methods=["POST"]
# )
# @jwt_required()
# @admin_required
# def send_notification():

#     body = request.get_json()

#     data, status = create_notification(body)

#     return jsonify(data), status



