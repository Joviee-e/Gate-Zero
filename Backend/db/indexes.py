from db.mongo import shelters_collection


def create_indexes():
    """
    Create required database indexes for Shelter Connect.
    """

    # Geo index for map + emergency queries
    shelters_collection.create_index([
        ("location", "2dsphere")
    ])

    # Frequently filtered fields
    shelters_collection.create_index("ngoId")
    shelters_collection.create_index("city")
    shelters_collection.create_index("emergencyEnabled")
    shelters_collection.create_index("availableBeds")
    shelters_collection.create_index("status")

    print("✅ Indexes created on shelters collection")


if __name__ == "__main__":
    create_indexes()
