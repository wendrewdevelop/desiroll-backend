from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socketio


# Cria a instância do Socket.IO
sio = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=[]
)

# Cria a instância do FastAPI
app = FastAPI()

# Monta o Socket.IO no caminho "/ws"
app.mount("/ws", socketio.ASGIApp(sio))

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas HTTP de exemplo
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Importa eventos para registrar os handlers no sio
# (certifique-se de que "events.py" importe "sio" de maneira correta)
from app.sockets import events

# Se preferir rodar diretamente via "python app/main.py":
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
