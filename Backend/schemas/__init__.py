from .ngo_schema import (
    NGORegisterSchema,
    NGOLoginSchema,
    NGOUpdateSchema,
)

from .shelter_schema import (
    CreateShelterSchema,
    UpdateShelterSchema,
    BedUpdateSchema,
    EmergencyToggleSchema,
)

from .emergency_schema import EmergencyQuerySchema

__all__ = [
    "NGORegisterSchema",
    "NGOLoginSchema",
    "NGOUpdateSchema",
    "CreateShelterSchema",
    "UpdateShelterSchema",
    "BedUpdateSchema",
    "EmergencyToggleSchema",
    "EmergencyQuerySchema",
]
