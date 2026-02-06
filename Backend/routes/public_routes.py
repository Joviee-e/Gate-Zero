from flask import Blueprint, request, jsonify

from services.search_service import (
    list_shelters,
    nearby_shelters,
    offline_shelters
)

public_bp = Blueprint("public_bp", __name__)


# ---------------------------------------------------
# LIST ALL SHELTERS
# GET /api/shelters
# ---------------------------------------------------
@public_bp.route("/shelters", methods=["GET"])
def get_shelters():
    shelters = list_shelters(request.args)

    return jsonify({
        "shelters": shelters
    }), 200


# ---------------------------------------------------
# NEARBY SHELTERS
# GET /api/shelters/nearby
# ---------------------------------------------------
@public_bp.route("/shelters/nearby", methods=["GET"])
def get_nearby():
    lng = request.args.get("lng")
    lat = request.args.get("lat")

    if not lng or not lat:
        return jsonify({"error": "lng and lat required"}), 400

    shelters = nearby_shelters(float(lng), float(lat))

    return jsonify({
        "shelters": shelters
    }), 200


# ---------------------------------------------------
# OFFLINE CACHE MODE
# GET /api/shelters/offline
# ---------------------------------------------------
@public_bp.route("/shelters/offline", methods=["GET"])
def offline_mode():
    shelters = offline_shelters()

    return jsonify({
        "shelters": shelters
    }), 200
