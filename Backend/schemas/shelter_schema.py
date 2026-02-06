from marshmallow import Schema, fields, validate, validates_schema, ValidationError


# ---------------------------------------------------
# LOCATION SCHEMA (GeoJSON)
# ---------------------------------------------------
class LocationSchema(Schema):
    type = fields.Str(required=True)
    coordinates = fields.List(
        fields.Float(),
        required=True,
        validate=validate.Length(equal=2)
    )


# ---------------------------------------------------
# BASE SHELTER SCHEMA
# ---------------------------------------------------
class ShelterBaseSchema(Schema):
    """
    Common fields used in shelter creation & updates
    """

    name = fields.Str(required=True, validate=validate.Length(min=2, max=120))
    address = fields.Str(required=True, validate=validate.Length(min=5, max=250))
    city = fields.Str(required=True, validate=validate.Length(min=2, max=80))

    phone = fields.Str(
        required=True,
        validate=validate.Regexp(r"^[0-9]{10}$")
    )

    location = fields.Nested(LocationSchema, required=True)

    pricePerNight = fields.Int(validate=validate.Range(min=0))

    capacity = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )

    availableBeds = fields.Int(
        required=True,
        validate=validate.Range(min=0)
    )

    features = fields.List(fields.Str())


# ---------------------------------------------------
# CREATE SHELTER
# ---------------------------------------------------
class CreateShelterSchema(ShelterBaseSchema):
    pass


# ---------------------------------------------------
# UPDATE SHELTER
# ---------------------------------------------------
class UpdateShelterSchema(Schema):

    name = fields.Str(validate=validate.Length(min=2, max=120))
    address = fields.Str(validate=validate.Length(min=5, max=250))
    city = fields.Str(validate=validate.Length(min=2, max=80))
    phone = fields.Str(validate=validate.Regexp(r"^[0-9]{10}$"))

    location = fields.Nested(LocationSchema)

    pricePerNight = fields.Int(validate=validate.Range(min=0))
    capacity = fields.Int(validate=validate.Range(min=1))
    availableBeds = fields.Int(validate=validate.Range(min=0))

    emergencyEnabled = fields.Boolean()
    features = fields.List(fields.Str())
    status = fields.Str()


# ---------------------------------------------------
# BED UPDATE
# ---------------------------------------------------
class BedUpdateSchema(Schema):

    availableBeds = fields.Int(
        required=True,
        validate=validate.Range(min=0)
    )


# ---------------------------------------------------
# EMERGENCY TOGGLE
# ---------------------------------------------------
class EmergencyToggleSchema(Schema):

    status = fields.Boolean(required=True)
