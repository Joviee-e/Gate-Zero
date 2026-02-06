from marshmallow import Schema, fields, validate


# ---------------------------------------------------
# EMERGENCY SEARCH QUERY PARAMS
# ---------------------------------------------------
class EmergencyQuerySchema(Schema):

    lng = fields.Float(required=True)
    lat = fields.Float(required=True)
