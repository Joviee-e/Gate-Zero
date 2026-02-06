from bson import ObjectId


def is_valid_object_id(value: str) -> bool:
    try:
        ObjectId(value)
        return True
    except Exception:
        return False


def validate_coordinates(lng, lat):
    if lng < -180 or lng > 180:
        return False

    if lat < -90 or lat > 90:
        return False

    return True
