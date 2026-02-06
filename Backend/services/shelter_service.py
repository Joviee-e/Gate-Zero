from flask import current_app
from bson import ObjectId
from datetime import datetime

from models.shelter_model import ShelterModel


# ---------------------------------------------------
# CREATE SHELTER
# ---------------------------------------------------
def create_shelter(ngo_id, shelter_data):
    """
    Create a new shelter under NGO
    """

    db = current_app.db
    shelter_collection = db["shelters"]

    shelter_doc = ShelterModel.create(
        shelter_data,
        ngo_id
    )

    result = shelter_collection.insert_one(shelter_doc)

    return str(result.inserted_id)


# ---------------------------------------------------
# GET SHELTER BY ID
# ---------------------------------------------------
def get_shelter_by_id(shelter_id):
    """
    Fetch shelter using ID
    """

    db = current_app.db
    shelter_collection = db["shelters"]

    shelter = shelter_collection.find_one({
        "_id": ObjectId(shelter_id)
    })

    if shelter:
        return ShelterModel.to_response(shelter)

    return None


# ---------------------------------------------------
# GET NGO SHELTERS
# ---------------------------------------------------
def get_shelters_by_ngo(ngo_id):
    """
    Fetch all shelters belonging to NGO
    """

    db = current_app.db
    shelter_collection = db["shelters"]

    shelters = shelter_collection.find({
        "ngoId": ObjectId(ngo_id)
    })

    return [
        ShelterModel.to_response(s)
        for s in shelters
    ]


# ---------------------------------------------------
# UPDATE SHELTER
# ---------------------------------------------------
def update_shelter(shelter_id, update_data):
    """
    Update shelter fields
    """

    db = current_app.db
    shelter_collection = db["shelters"]

    payload = ShelterModel.update(update_data)

    result = shelter_collection.update_one(
        {"_id": ObjectId(shelter_id)},
        {"$set": payload}
    )

    return result.modified_count


# ---------------------------------------------------
# DELETE SHELTER
# ---------------------------------------------------
def delete_shelter(shelter_id):
    """
    Remove a shelter
    """

    db = current_app.db
    shelter_collection = db["shelters"]

    result = shelter_collection.delete_one({
        "_id": ObjectId(shelter_id)
    })

    return result.deleted_count


# ---------------------------------------------------
# UPDATE AVAILABLE BEDS
# ---------------------------------------------------
def update_available_beds(shelter_id, beds_count):
    """
    Update availableBeds
    """

    db = current_app.db
    shelter_collection = db["shelters"]

    result = shelter_collection.update_one(
        {"_id": ObjectId(shelter_id)},
        {
            "$set": {
                "availableBeds": beds_count,
                "updatedAt": datetime.utcnow()
            }
        }
    )

    return result.modified_count


# ---------------------------------------------------
# TOGGLE EMERGENCY MODE
# ---------------------------------------------------
def toggle_emergency_mode(shelter_id, status):
    """
    Toggle emergencyEnabled
    """

    db = current_app.db
    shelter_collection = db["shelters"]

    result = shelter_collection.update_one(
        {"_id": ObjectId(shelter_id)},
        {
            "$set": {
                "emergencyEnabled": status,
                "updatedAt": datetime.utcnow()
            }
        }
    )

    return result.modified_count


# ---------------------------------------------------
# LIST ALL SHELTERS (ADMIN / FUTURE)
# ---------------------------------------------------
def list_all_shelters():
    """
    Returns all shelters
    """

    db = current_app.db
    shelter_collection = db["shelters"]

    shelters = shelter_collection.find()

    return [
        ShelterModel.to_response(s)
        for s in shelters
    ]
