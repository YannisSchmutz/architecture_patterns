from typing import List

from fastapi_camelcase import CamelModel
from models.room import Room_pydantic


# Shared properties
class RoomBase(CamelModel):
    number: int
    floor: int


# Properties to receive on creation
class RoomCreate(RoomBase):
    number: int
    floor: int


# Properties shared by models stored in DB
class RoomInDBBase(CamelModel, Room_pydantic):
    pass


# Properties to return to client
class Room(RoomInDBBase):
    number: int
    floor: int


# Properties properties stored in DB
class RoomInDB(RoomInDBBase):
    pass
