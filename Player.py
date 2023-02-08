# from Database import players


class player:
    class_identifier = "PL"
    current_letter = 0  # show in which generation the object are in.
    id_number = 0
    # objects = players

    def __init__(self, id):
        self.__id = id


players = {}

def create_object(class_in_use, id):
    if id not in players:
        players[id] = class_in_use(id)
    return players[id]


create_object(player, "A1")
