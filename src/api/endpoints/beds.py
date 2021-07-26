from fastapi import APIRouter, HTTPException, status, Path
import schemas
from crud import crud_bed as crud
from typing import List

router = APIRouter()


@router.post("/", response_model=schemas.Bed, status_code=status.HTTP_201_CREATED)
async def create_bed(payload: schemas.BedCreate) -> schemas.Bed:

    print('**********')
    print('Bed create')
    print(payload)

    bed_id = await crud.post(payload)

    print(bed_id)

    response_object = {
        "id": bed_id,
        "roomId": payload.room_id,
    }
    return schemas.Bed.parse_obj(response_object)


@router.get("/{id}/", response_model=schemas.Bed, status_code=status.HTTP_200_OK)
async def read_bed(bed_id: int) -> schemas.Bed:
    bed = await crud.get(bed_id)
    if not bed:
        raise HTTPException(status_code=404, detail="Bed not found")
    return bed


@router.get("/", response_model=List[schemas.Bed])
async def read_all_beds() -> List[schemas.Bed]:
    return await crud.get_all()


@router.get("/by_room", response_model=List[schemas.Bed])
async def read_all_beds_by_room(room_id: int) -> List[schemas.Bed]:
    return await crud.get_all_by_room(room_id)


@router.delete("/{id}/", response_model=schemas.Bed)
async def delete_bed(id: int = Path(..., gt=0)) -> schemas.Bed:
    bed = await crud.get(id)
    if not bed:
        raise HTTPException(status_code=404, detail="Bed not found")

    await crud.delete(id)

    return bed

# TODO: Update