from app.main import sio
from game import dice, rooms  # Exemplo de import da lógica de jogo


@sio.event
async def connect(sid, environ):
    print(f"Client connected: {sid}")

@sio.event
async def disconnect(sid):
    print(f"Client disconnected: {sid}")

@sio.on("join_room")
async def handle_join(sid, data):
    room_id = data["room_id"]
    await sio.save_session(sid, {"room_id": room_id})
    sio.enter_room(sid, room_id)
    # Notifica todos na sala que alguém entrou
    await sio.emit("user_joined", {"room_id": room_id, "sid": sid}, room=room_id)

@sio.on("roll_dice")
async def handle_dice_roll(sid, data):
    session_data = await sio.get_session(sid)
    notation = data["notation"]
    result = dice.roll(notation)
    # Emite o resultado para todos na sala
    await sio.emit(
        "dice_result",
        {
            "user": session_data.get("user", sid),
            "notation": notation,
            "result": result
        },
        room=session_data["room_id"]
    )
