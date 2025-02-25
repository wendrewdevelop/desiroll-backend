from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from socketio import AsyncServer

app = FastAPI()
sio = AsyncServer(async_mode='asgi', cors_allowed_origins=[])
app.mount("/ws", socketio.ASGIApp(sio))

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas HTTP
@app.get("/health")
async def health_check():
    return {"status": "ok"}