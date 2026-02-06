from flask import Blueprint, request, jsonify

from services.emergency_service import get_emergency_shelters

emergency_bp = Blueprint("emergency_bp", __name__)


# ---------------------------------------------------
# EMERGENCY MODE
# GET /api/emergency
# ---------------------------------------------------
@emergency_bp.route("/emergency", methods=["GET"])
def emergency():
    lng = request.args.get("lng")
    lat = request.args.get("lat")

    if not lng or not lat:
        return jsonify({"error": "lng and lat required"}), 400

    shelters = get_emergency_shelters(
        float(lng),
        float(lat)
    )

    return jsonify({
        "count": len(shelters),
        "shelters": shelters
    }), 200
