@sio.on("join_room")
async def handle_join(sid, data):
    room_id = data["room_id"]
    await sio.save_session(sid, {"room_id": room_id})
    sio.enter_room(sid, room_id)
    await sio.emit("user_joined", data, room=room_id)

@sio.on("roll_dice")
async def handle_dice_roll(sid, data):
    session = await sio.get_session(sid)
    # Lógica de rolagem
    result = dice.roll(data["notation"])
    await sio.emit("dice_result", {
        "user": session["user"],
        "result": result
    }, room=session["room_id"])