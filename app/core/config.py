import os
from sqlalchemy.ext.declarative import declarative_base

# Carrega variável de ambiente ou usa padrão
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "sqlite+aiosqlite:///./db.sqlite3"
)
Base = declarative_base()
