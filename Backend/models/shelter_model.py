from datetime import datetime
from bson import ObjectId


class ShelterModel:
    """
    Data helper class for Shelter documents.
    Handles formatting + serialization only.
    """

    @staticmethod
    def create(data: dict, ngo_id: str) -> dict:
        """
        Build a new shelter document for insertion.
        """

        return {
            "ngoId": ObjectId(ngo_id),
            "name": data.get("name"),
            "address": data.get("address"),
            "city": data.get("city"),
            "phone": data.get("phone"),
            "location": data.get("location"),  # GeoJSON Point
            "pricePerNight": data.get("pricePerNight", 0),
            "capacity": data.get("capacity"),
            "availableBeds": data.get("availableBeds"),
            "emergencyEnabled": data.get("emergencyEnabled", False),
            "features": data.get("features", []),
            "status": data.get("status", "active"),
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow(),
        }

    @staticmethod
    def update(data: dict) -> dict:
        """
        Prepare update payload for shelter.
        """

        update_fields = {}

        allowed = [
            "name",
            "address",
            "city",
            "phone",
            "location",
            "pricePerNight",
            "capacity",
            "availableBeds",
            "emergencyEnabled",
            "features",
            "status",
        ]

        for field in allowed:
            if field in data:
                update_fields[field] = data[field]

        update_fields["updatedAt"] = datetime.utcnow()

        return update_fields

    @staticmethod
    def to_response(shelter: dict) -> dict:
        """
        Convert Mongo shelter document to API-safe response.
        """

        return {
            "id": str(shelter["_id"]) if isinstance(shelter.get("_id"), ObjectId) else shelter.get("_id"),
            "ngoId": str(shelter.get("ngoId")) if isinstance(shelter.get("ngoId"), ObjectId) else shelter.get("ngoId"),
            "name": shelter.get("name"),
            "address": shelter.get("address"),
            "city": shelter.get("city"),
            "phone": shelter.get("phone"),
            "location": shelter.get("location"),
            "pricePerNight": shelter.get("pricePerNight"),
            "capacity": shelter.get("capacity"),
            "availableBeds": shelter.get("availableBeds"),
            "emergencyEnabled": shelter.get("emergencyEnabled"),
            "features": shelter.get("features"),
            "status": shelter.get("status"),
            "createdAt": shelter.get("createdAt"),
            "updatedAt": shelter.get("updatedAt"),
        }
