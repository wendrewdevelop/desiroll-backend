from beanie import Document
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Room(Document):
    name: str
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)
    is_active: bool = True  # Controle de acesso
    
    class Settings:
        name = "rooms"