from db.indexes import create_indexes


def main():
    print("\n=== Migrating Indexes ===")
    create_indexes()
    print("✅ Migration complete")


if __name__ == "__main__":
    main()
