from datetime import datetime
from bson import ObjectId


class NGOModel:
    """
    Data helper class for NGO documents.

    This does NOT handle auth or business logic — only
    formatting and validation of NGO records.
    """

    @staticmethod
    def create(data: dict) -> dict:
        """
        Build a new NGO document for insertion.
        """

        return {
            "name": data.get("name"),
            "email": data.get("email"),
            "phone": data.get("phone"),
            "verified": data.get("verified", False),
            "createdAt": datetime.utcnow(),
        }

    @staticmethod
    def to_response(ngo: dict) -> dict:
        """
        Convert Mongo NGO document to API-safe response.
        """

        return {
            "id": str(ngo["_id"]) if isinstance(ngo.get("_id"), ObjectId) else ngo.get("_id"),
            "name": ngo.get("name"),
            "email": ngo.get("email"),
            "phone": ngo.get("phone"),
            "verified": ngo.get("verified", False),
            "createdAt": ngo.get("createdAt"),
        }
