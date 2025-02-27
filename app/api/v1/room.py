from fastapi import APIRouter, HTTPException
from app.db.models import Room
from pydantic import BaseModel


router = APIRouter(
    prefix="/rooms", 
    tags=[
        "rooms"
    ]
)

@router.post("/")
async def create_room(name: str):
    room = Room(name=name)
    await room.insert()
    return {"id": str(room.id), "name": name}

@router.delete("/{room_id}")
async def delete_room(room_id: str):
    room = await Room.get(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    
    # Deleta a sala e todos os personagens vinculados
    await Character.find(Character.room_id == room_id).delete()
    await room.delete()
    
    return {"message": "Room and characters deleted"}