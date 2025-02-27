from pydantic import BaseModel, Field
from pydantic.types import PydanticObjectId, List


class CharacterResponse(BaseModel):
    id: str  # Será populado automaticamente pelo alias _id
    player_name: str
    character_name: str
    room_id: str  # Convertido para string
    race: str
    character_class: str
    level: int
    background: str
    alignment: str
    experience_points: int
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
    armor_class: int
    initiative: int
    speed: int
    hit_points: int
    temporary_hit_points: int
    death_saves: List[str]
    skills: List[dict]  # Ou use um SkillResponse
    equipment: List[dict]  # Ou use um EquipmentResponse
    spells: List[dict]  # Ou use um SpellResponse
    features: List[dict]  # Ou use um FeatureResponse

    class Config:
        populate_by_name = True
        json_encoders = {
            PydanticObjectId: lambda v: str(v)
        }