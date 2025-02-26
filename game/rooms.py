rooms_data = {}

def create_room(room_id: str):
    if room_id not in rooms_data:
        rooms_data[room_id] = {
            "players": []
        }
    return rooms_data[room_id]

def add_player(room_id: str, player_id: str):
    if room_id in rooms_data:
        rooms_data[room_id]["players"].append(player_id)

# etc.
