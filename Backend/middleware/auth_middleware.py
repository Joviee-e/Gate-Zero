from functools import wraps
from flask import request, jsonify, current_app, g
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from bson import ObjectId


# -------------------------------------------------
# JWT PROTECTED NGO ROUTES
# -------------------------------------------------

def jwt_required_ngo(fn):
    """
    Protects routes so only authenticated NGOs can access them.

    - Verifies JWT
    - Fetches NGO from MongoDB
    - Attaches NGO object to flask global context (g.ngo)
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            # Verify JWT token
            verify_jwt_in_request()

            # NGO id stored in token identity
            ngo_id = get_jwt_identity()

            if not ngo_id:
                return jsonify({"error": "Invalid token"}), 401

            db = current_app.db
            ngos_collection = db["ngos"]

            ngo = ngos_collection.find_one({
                "_id": ObjectId(ngo_id)
            })

            if not ngo:
                return jsonify({"error": "NGO not found"}), 404

            # Attach NGO to request context
            g.ngo = {
                "id": str(ngo["_id"]),
                "name": ngo.get("name"),
                "email": ngo.get("email"),
                "phone": ngo.get("phone"),
                "verified": ngo.get("verified", False)
            }

        except Exception as e:
            return jsonify({
                "error": "Authentication failed",
                "details": str(e)
            }), 401

        return fn(*args, **kwargs)

    return wrapper


# -------------------------------------------------
# OPTIONAL NGO ROLE CHECK (FUTURE-PROOF)
# -------------------------------------------------

def ngo_role_required(fn):
    """
    Extra protection layer if roles are introduced later.
    Currently just ensures NGO context exists.
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not hasattr(g, "ngo"):
            return jsonify({"error": "Unauthorized"}), 403

        return fn(*args, **kwargs)

    return wrapper
