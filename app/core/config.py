import os

# Carrega variável de ambiente ou usa padrão
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "sqlite+aiosqlite:///./db.sqlite3"
)
