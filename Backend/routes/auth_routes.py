from flask import Blueprint, request, jsonify

from services.ngo_service import (
    register_ngo,
    login_ngo
)

auth_bp = Blueprint("auth_bp", __name__)


# ---------------------------------------------------
# REGISTER NGO
# POST /api/auth/register
# ---------------------------------------------------
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing payload"}), 400

    ngo_id = register_ngo(data)

    return jsonify({
        "message": "NGO registered successfully",
        "ngo_id": ngo_id
    }), 201


# ---------------------------------------------------
# LOGIN NGO
# POST /api/auth/login
# ---------------------------------------------------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing payload"}), 400

    token = login_ngo(data)

    if not token:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({
        "access_token": token
    }), 200
