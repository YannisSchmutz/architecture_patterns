from typing import List, Optional

import schemas
from models.room import Room


async def post(payload: schemas.RoomCreate) -> int:

    room = await Room.create(
        number=payload.number,
        floor=payload.floor,
    )

    return room.id


async def get(id: int) -> Optional[Room]:
    room = await Room.filter(id=id).first()
    if room:
        return room
    return None


async def get_all() -> List[Room]:
    rooms = await Room.all()
    return rooms


async def get_all_by_floor(floor: int) -> List[Room]:
    rooms = await Room.filter(floor=floor)
    return rooms


async def delete(id: int) -> int:
    room = await Room.filter(id=id).delete()
    return room


async def delete_all() -> None:
    await Room.all().delete()
    return None


# TODO: Update