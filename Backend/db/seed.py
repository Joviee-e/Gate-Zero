"""
Seed script for Shelter Connect.

Used only for development/demo to insert sample NGOs and shelters.
"""

from datetime import datetime
from bson import ObjectId

from db.mongo import ngos_collection, shelters_collection


def seed_data():
    ngos_collection.delete_many({})
    shelters_collection.delete_many({})

    ngo_id = ngos_collection.insert_one({
        "name": "Helping Hands NGO",
        "email": "help@ngo.org",
        "phone": "+91-9000000000",
        "verified": True,
        "createdAt": datetime.utcnow()
    }).inserted_id

    shelters_collection.insert_many([
        {
            "ngoId": ObjectId(ngo_id),
            "name": "Central Relief Shelter",
            "address": "MG Road",
            "city": "Mumbai",
            "phone": "+91-9111111111",
            "location": {
                "type": "Point",
                "coordinates": [72.8777, 19.0760]
            },
            "pricePerNight": 0,
            "capacity": 50,
            "availableBeds": 20,
            "emergencyEnabled": True,
            "features": ["food", "medical", "charging"],
            "status": "active",
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        },
        {
            "ngoId": ObjectId(ngo_id),
            "name": "West Side Shelter",
            "address": "Linking Road",
            "city": "Mumbai",
            "phone": "+91-9222222222",
            "location": {
                "type": "Point",
                "coordinates": [72.8295, 19.0596]
            },
            "pricePerNight": 0,
            "capacity": 30,
            "availableBeds": 5,
            "emergencyEnabled": False,
            "features": ["water", "toilet"],
            "status": "active",
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        }
    ])

    print("✅ Seed data inserted successfully")


if __name__ == "__main__":
    seed_data()
