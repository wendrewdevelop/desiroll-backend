from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict
from beanie import Document, Indexed, PydanticObjectId
from uuid import UUID


class Skill(BaseModel):
    name: str  # Ex: "Arcanismo", "Atletismo"
    is_proficient: bool = False
    modifier: int = 0

class PersonalityTraits(BaseModel):
    traits: List[str] = []
    ideals: List[str] = []
    bonds: List[str] = []
    flaws: List[str] = []

class EquipmentItem(BaseModel):
    name: str
    quantity: int = 1
    description: Optional[str] = None

class Spell(BaseModel):
    name: str
    level: int
    description: str
    slots_total: int = 0
    slots_used: int = 0

class Feature(BaseModel):
    name: str
    description: str

class PhysicalAttributes(BaseModel):
    height: Optional[str] = None
    weight: Optional[str] = None
    eyes: Optional[str] = None
    skin: Optional[str] = None
    hair: Optional[str] = None
    appearance: Optional[str] = None

class Character(Document):
    # Identificação
    id: str = Field(
        default_factory=PydanticObjectId, 
        alias="_id"  # Mapeia para o campo _id do MongoDB
    )
    player_name: Indexed(str)
    character_name: Indexed(str)
    room_id: PydanticObjectId  # Sala vinculada
    
    # Atributos Principais
    race: str
    character_class: str
    level: int = 1
    background: str
    alignment: str
    experience_points: int = 0
    
    # Atributos Numéricos
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
    
    # Sistema de Jogo
    armor_class: int = 10
    initiative: int = 0
    speed: int = 30
    hit_points: int
    temporary_hit_points: int = 0
    death_saves: List[str] = []  # Ex: ["success", "failure"]
    
    # Listas Complexas
    skills: List[Skill] = []
    equipment: List[EquipmentItem] = []
    spells: List[Spell] = []
    features: List[Feature] = []
    
    # Subdocumentos
    personality: PersonalityTraits = PersonalityTraits()
    physical: PhysicalAttributes = PhysicalAttributes()
    
    # Metadados
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(
        json_encoders={
            PydanticObjectId: lambda v: str(v)
        },  # Converte ObjectId para string 
        populate_by_name=True  # Permite usar alias "_id" como "id"
    )
    class Settings:
        name = "characters"
        indexes = [
            "room_id",  # Index para consultas rápidas por sala
            "character_class",
            "level"
        ]

        