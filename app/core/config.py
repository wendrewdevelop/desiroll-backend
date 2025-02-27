from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.db.models.room import Room
from app.db.models.character import Character


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Configuração do MongoDB
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(
        database=client.dnd_db,
        document_models=[Character, Room]
    )
    yield
    # Shutdown: Fechar conexão (opcional)
    client.close()


app = FastAPI(lifespan=lifespan)
Base = declarative_base()