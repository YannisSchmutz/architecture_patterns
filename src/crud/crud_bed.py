from typing import List, Optional

import schemas
from models.bed import Bed


async def post(payload: schemas.BedCreate) -> int:

    bed = await Bed.create(
        room_id=payload.room_id,
    )

    return bed.id


async def get(id: int) -> Optional[Bed]:
    bed = await Bed.filter(id=id).first()
    if bed:
        return bed
    return None


async def get_all() -> List[Bed]:
    beds = await Bed.all()
    return beds


async def get_all_by_room(room_id: int) -> List[Bed]:
    beds = await Bed.filter(room_id=room_id)
    return beds


async def delete(id: int) -> int:
    bed = await Bed.filter(id=id).delete()
    return bed


async def delete_all() -> None:
    await Bed.all().delete()
    return None


# TODO: Update