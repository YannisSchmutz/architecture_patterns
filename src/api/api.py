from fastapi import APIRouter

from api.endpoints import rooms
from api.endpoints import beds

api_router = APIRouter()
api_router.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
api_router.include_router(beds.router, prefix="/beds", tags=["beds"])
