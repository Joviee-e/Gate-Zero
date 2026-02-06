from flask import Blueprint, request, jsonify, g

from middleware.auth_middleware import jwt_required_ngo
from services.shelter_service import (
    create_shelter,
    get_shelter_by_id,
    get_shelters_by_ngo,
    update_shelter,
    delete_shelter,
    update_available_beds,
    toggle_emergency_mode
)

shelter_bp = Blueprint("shelter_bp", __name__)


# ---------------------------------------------------
# CREATE SHELTER  (POST /api/shelters)
# ---------------------------------------------------
@shelter_bp.route("", methods=["POST"])
@jwt_required_ngo
def add_shelter():
    """
    NGO creates a new shelter
    """

    data = request.get_json()
    ngo_id = g.ngo["id"]

    if not data:
        return jsonify({"error": "Missing payload"}), 400

    shelter_id = create_shelter(ngo_id, data)

    return jsonify({
        "message": "Shelter created successfully",
        "shelter_id": shelter_id
    }), 201


# ---------------------------------------------------
# GET NGO SHELTERS
# ---------------------------------------------------
@shelter_bp.route("", methods=["GET"])
@jwt_required_ngo
def get_my_shelters():
    """
    Fetch all shelters belonging to logged-in NGO
    """

    ngo_id = g.ngo["id"]

    shelters = get_shelters_by_ngo(ngo_id)

    return jsonify({"shelters": shelters}), 200


# ---------------------------------------------------
# GET SINGLE SHELTER
# ---------------------------------------------------
@shelter_bp.route("/<shelter_id>", methods=["GET"])
@jwt_required_ngo
def get_shelter(shelter_id):
    """
    Fetch shelter details
    """

    shelter = get_shelter_by_id(shelter_id)

    if not shelter:
        return jsonify({"error": "Shelter not found"}), 404

    return jsonify(shelter), 200


# ---------------------------------------------------
# UPDATE SHELTER  (PUT /api/shelters/:id)
# ---------------------------------------------------
@shelter_bp.route("/<shelter_id>", methods=["PUT"])
@jwt_required_ngo
def edit_shelter(shelter_id):
    """
    Update shelter info
    """

    data = request.get_json()

    updated = update_shelter(shelter_id, data)

    if updated == 0:
        return jsonify({"error": "Shelter not updated"}), 400

    return jsonify({"message": "Shelter updated successfully"}), 200


# ---------------------------------------------------
# DELETE SHELTER
# ---------------------------------------------------
@shelter_bp.route("/<shelter_id>", methods=["DELETE"])
@jwt_required_ngo
def remove_shelter(shelter_id):
    """
    Delete a shelter
    """

    deleted = delete_shelter(shelter_id)

    if deleted == 0:
        return jsonify({"error": "Shelter not found"}), 404

    return jsonify({"message": "Shelter deleted successfully"}), 200


# ---------------------------------------------------
# UPDATE AVAILABLE BEDS
# ---------------------------------------------------
@shelter_bp.route("/<shelter_id>/beds", methods=["PATCH"])
@jwt_required_ngo
def update_beds(shelter_id):
    """
    Update available beds count
    """

    data = request.get_json()

    if not data or "availableBeds" not in data:
        return jsonify({"error": "availableBeds field required"}), 400

    updated = update_available_beds(
        shelter_id,
        data["availableBeds"]
    )

    if updated == 0:
        return jsonify({"error": "Beds not updated"}), 400

    return jsonify({"message": "Available beds updated"}), 200


# ---------------------------------------------------
# TOGGLE EMERGENCY MODE
# ---------------------------------------------------
@shelter_bp.route("/<shelter_id>/emergency", methods=["PATCH"])
@jwt_required_ngo
def emergency_toggle(shelter_id):
    """
    Turn emergency mode ON/OFF
    """

    data = request.get_json()

    if not data or "status" not in data:
        return jsonify({"error": "status field required"}), 400

    updated = toggle_emergency_mode(
        shelter_id,
        data["status"]
    )

    if updated == 0:
        return jsonify({"error": "Emergency status not updated"}), 400

    return jsonify({
        "message": "Emergency mode updated",
        "status": data["status"]
    }), 200
