from fastapi import APIRouter, HTTPException, status, Path, Depends
import schemas
from crud import crud_room as crud
from typing import List

router = APIRouter()


@router.post("/", response_model=schemas.Room, status_code=status.HTTP_201_CREATED)
async def create_room(payload: schemas.RoomCreate) -> schemas.Room:
    room_id = await crud.post(payload)

    response_object = {
        "id": room_id,
        "number": payload.number,
        "floor": payload.floor,
    }
    return schemas.Room.parse_obj(response_object)


@router.get("/{id}/", response_model=schemas.Room, status_code=status.HTTP_200_OK)
async def read_room(room_id: int) -> schemas.Room:
    room = await crud.get(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room


@router.get("/", response_model=List[schemas.Room])
async def read_all_rooms() -> List[schemas.Room]:
    return await crud.get_all()


@router.delete("/{id}/", response_model=schemas.Room)
async def delete_room(id: int = Path(..., gt=0)) -> schemas.Room:
    room = await crud.get(id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    await crud.delete(id)

    return room

# TODO: Update