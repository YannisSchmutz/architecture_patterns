from fastapi_camelcase import CamelModel
from models.bed import Bed_pydantic


# Shared properties
class BedBase(CamelModel):
    pass


# Properties to receive on creation
class BedCreate(BedBase):
    room_id: int


# Properties shared by models stored in DB
class BedInDBBase(CamelModel, Bed_pydantic):
    pass


# Properties to return to client
class Bed(BedInDBBase):
    room_id: int


# Properties properties stored in DB
class BedInDB(BedInDBBase):
    room_id: int
