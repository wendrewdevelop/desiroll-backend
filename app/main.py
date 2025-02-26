import os
import uvicorn
from fastapi.staticfiles import StaticFiles
from decouple import config
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from app.api.v1.endpoints import router as api_routes
from app.core.security import app
from app.core.config import Base
from app.db.session import postgresql, session

URL_local = "http://localhost:8000" if config("ENV") == "DEV" \
            else "https://luizahub.market.com.br"
origins = ["*"]

Base.metadata.create_all(bind=postgresql.get_engine())

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    DBSessionMiddleware,
    db_url=config("DB_URL")
)
app.add_middleware(
    SessionMiddleware,
    secret_key=config("SECRET_KEY"),
    same_site="Lax"
)

# assets_directory = os.path.join(os.path.dirname(__file__), "src/frontend/assets")
# assets_directory = os.path.abspath(assets_directory)
app.mount(
    "/assets", 
    StaticFiles(directory="src/frontend/assets"), 
    name="assets"
)

app.include_router(api_routes, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="localhost",
        port=8000,
        log_level="info",
        reload=True
    )