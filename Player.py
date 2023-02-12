from functionality_classes.Database import players
from patterns_classes.Creature_pattern import creature_pattern

class player(creature_pattern):
    class_identifier = "PL"
    current_letter = 0  # show in which generation the object are in.
    id_number = 0

    objects = players
    invalid_attributes = ["id"]

    def __init__(self, id, name: str = 'None', hp: int = 0, mp: int = 0, party=None):
        super().__init__(id, name, hp, mp)
        self.__party = party

    # Properties
