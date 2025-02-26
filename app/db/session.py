from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL  # Exemplo: variável em config.py


engine = create_async_engine(
    DATABASE_URL, 
    echo=True
)
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Exemplo de dependência para FastAPI
async def get_db():
    async with async_session() as session:
        yield session
