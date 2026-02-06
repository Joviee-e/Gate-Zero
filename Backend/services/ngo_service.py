from flask import current_app
from bson import ObjectId
from datetime import datetime

from utils.password import hash_password, verify_password
from utils.jwt_handler import create_access_token


# ---------------------------------------------------
# REGISTER NGO
# ---------------------------------------------------
def register_ngo(data):
    """
    Register a new NGO
    """

    db = current_app.db
    ngo_collection = db["ngos"]

    existing = ngo_collection.find_one({"email": data.get("email")})
    if existing:
        raise ValueError("Email already registered")

    ngo_doc = {
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "password": hash_password(data.get("password")),
        "verified": False,
        "createdAt": datetime.utcnow(),
    }

    result = ngo_collection.insert_one(ngo_doc)

    return str(result.inserted_id)


# ---------------------------------------------------
# LOGIN NGO
# ---------------------------------------------------
def login_ngo(data):
    """
    Authenticate NGO and return JWT token
    """

    db = current_app.db
    ngo_collection = db["ngos"]

    ngo = ngo_collection.find_one({"email": data.get("email")})

    if not ngo:
        return None

    if not verify_password(data.get("password"), ngo.get("password")):
        return None

    return create_access_token(str(ngo["_id"]))


# ---------------------------------------------------
# GET NGO BY ID
# ---------------------------------------------------
def get_ngo_by_id(ngo_id):
    """
    Fetch NGO using Mongo ObjectId
    """

    db = current_app.db
    ngo_collection = db["ngos"]

    ngo = ngo_collection.find_one({"_id": ObjectId(ngo_id)})

    if ngo:
        ngo["_id"] = str(ngo["_id"])

    return ngo


# ---------------------------------------------------
# UPDATE NGO PROFILE
# ---------------------------------------------------
def update_ngo_profile(ngo_id, update_data):
    """
    Update NGO details like name, phone
    """

    allowed = ["name", "phone"]

    payload = {
        k: v for k, v in update_data.items()
        if k in allowed
    }

    if not payload:
        return 0

    db = current_app.db
    ngo_collection = db["ngos"]

    result = ngo_collection.update_one(
        {"_id": ObjectId(ngo_id)},
        {"$set": payload}
    )

    return result.modified_count


# ---------------------------------------------------
# GET NGO BY EMAIL
# ---------------------------------------------------
def get_ngo_by_email(email):
    """
    Fetch NGO using email
    """

    db = current_app.db
    ngo_collection = db["ngos"]

    ngo = ngo_collection.find_one({"email": email})

    if ngo:
        ngo["_id"] = str(ngo["_id"])

    return ngo


# ---------------------------------------------------
# LIST ALL NGOs (ADMIN / FUTURE)
# ---------------------------------------------------
def list_all_ngos():
    """
    Returns all NGOs in the system
    """

    db = current_app.db
    ngo_collection = db["ngos"]

    ngos = list(ngo_collection.find())

    for ngo in ngos:
        ngo["_id"] = str(ngo["_id"])

    return ngos
