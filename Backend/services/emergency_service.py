from flask import current_app
from datetime import datetime

from models.shelter_model import ShelterModel


# ---------------------------------------------------
# EMERGENCY MODE SEARCH
# ---------------------------------------------------
def get_emergency_shelters(lng, lat):
    """
    Returns top 3 nearest shelters with:

    - emergencyEnabled = true
    - availableBeds > 0
    - sorted by distance
    - includes distance in meters
    """

    db = current_app.db
    shelter_collection = db["shelters"]

    pipeline = [
        {
            "$geoNear": {
                "near": {
                    "type": "Point",
                    "coordinates": [lng, lat]
                },
                "distanceField": "distance",
                "spherical": True,
                "query": {
                    "emergencyEnabled": True,
                    "availableBeds": {"$gt": 0},
                    "status": "active"
                }
            }
        },
        {"$limit": 3}
    ]

    shelters = shelter_collection.aggregate(pipeline)

    results = []

    for shelter in shelters:
        shelter["distance"] = round(shelter.get("distance", 0), 2)
        results.append(
            ShelterModel.to_response(shelter) | {
                "distance": shelter["distance"]
            }
        )

    return results
