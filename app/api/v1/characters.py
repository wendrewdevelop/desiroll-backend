from fastapi import APIRouter, HTTPException
from app.db.models import Character
from pydantic import BaseModel
from typing import List
from beanie import PydanticObjectId


router = APIRouter(
    prefix="/characters", 
    tags=[
        "characters"
    ]
)

class CharacterResponse(BaseModel):
    id: str
    character_name: str
    race: str
    character_class: str
    level: int

@router.post("/", response_model=CharacterResponse)
async def create_character(character: Character):
    await character.insert()
    return character


@router.get("/{room_id}", response_model=List[CharacterResponse])
async def get_characters_by_room(room_id: str):
    characters = await Character.find(Character.room_id == room_id).to_list()
    return characters


@router.get("/{character_id}", response_model=CharacterResponse)
async def get_character(character_id: str):
    try:
        obj_id = PydanticObjectId(character_id)  # Converte string para ObjectId
    except Exception:
        raise HTTPException(status_code=400, detail="ID inválido")
    
    character = await Character.get(obj_id)
    if not character:
        raise HTTPException(status_code=404, detail="Personagem não encontrado")
    
    return character 