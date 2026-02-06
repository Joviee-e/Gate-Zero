import sys
from getpass import getpass

from config import Config
from pymongo import MongoClient
from datetime import datetime

from utils.password import hash_password


def main():
    print("\n=== Create NGO Admin ===\n")

    name = input("NGO Name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone (10 digits): ").strip()
    password = getpass("Password: ")

    if not name or not email or not password:
        print("❌ Missing required fields")
        sys.exit(1)

    client = MongoClient(Config.MONGO_URI)
    db = client[Config.DB_NAME]
    ngos = db["ngos"]

    existing = ngos.find_one({"email": email})
    if existing:
        print("❌ Email already exists")
        sys.exit(1)

    ngo_doc = {
        "name": name,
        "email": email,
        "phone": phone,
        "password": hash_password(password),
        "verified": True,
        "createdAt": datetime.utcnow(),
    }

    result = ngos.insert_one(ngo_doc)

    print("\n✅ NGO admin created")
    print("ID:", str(result.inserted_id))


if __name__ == "__main__":
    main()
