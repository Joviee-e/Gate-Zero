from flask import current_app

from models.shelter_model import ShelterModel


# ---------------------------------------------------
# LIST ALL PUBLIC SHELTERS
# ---------------------------------------------------
def list_shelters(filters=None):
    """
    Public listing of shelters
    """

    db = current_app.db
    shelter_collection = db["shelters"]

    query = {"status": "active"}

    if filters:
        city = filters.get("city")
        if city:
            query["city"] = city

    shelters = shelter_collection.find(query)

    return [
        ShelterModel.to_response(s)
        for s in shelters
    ]


# ---------------------------------------------------
# NEARBY SEARCH
# ---------------------------------------------------
def nearby_shelters(lng, lat, radius_km=10):
    """
    Geo search within radius (default 10km)
    """

    db = current_app.db
    shelter_collection = db["shelters"]

    query = {
        "status": "active",
        "location": {
            "$nearSphere": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [lng, lat]
                },
                "$maxDistance": radius_km * 1000
            }
        }
    }

    shelters = shelter_collection.find(query)

    return [
        ShelterModel.to_response(s)
        for s in shelters
    ]


# ---------------------------------------------------
# OFFLINE MODE CACHE
# ---------------------------------------------------
def offline_shelters(limit=100):
    """
    Returns limited shelters for offline cache
    """

    db = current_app.db
    shelter_collection = db["shelters"]

    shelters = shelter_collection.find(
        {"status": "active"}
    ).limit(limit)

    return [
        ShelterModel.to_response(s)
        for s in shelters
    ]
