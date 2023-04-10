from functionality_classes.Database import players, parties
from patterns_classes.Creature_pattern import creature_pattern
from functionality_classes.general_features import find_similar_name


class player(creature_pattern):
    class_identifier = "PL"
    current_letter = 0  # show in which generation the object are in.
    id_number = 0

    objects_storage = players
    invalid_attributes = ["id"]

    def __init__(self, id, name: str = 'N/A', hp: int = 0, mp: int = 0, party=''):
        super().__init__(id, name, hp, mp)
        self.__party = party

    # internal functions

    # properties

    @property
    def party(self):
        return self.__party

    @party.setter
    def party(self, value):
        try:
            party_id = find_similar_name(value, parties)
            party_id.add_member(self)
            self.__party = party_id
        except AttributeError as e:
            print("Error setting party:", e)
