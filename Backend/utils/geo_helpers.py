def build_point(lng: float, lat: float):
    """
    Returns GeoJSON Point
    """

    return {
        "type": "Point",
        "coordinates": [lng, lat]
    }
