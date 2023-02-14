from functionality_classes.Database import players, parties
from patterns_classes.Creature_pattern import creature_pattern
from fuzzywuzzy import fuzz


class player(creature_pattern):
    class_identifier = "PL"
    current_letter = 0  # show in which generation the object are in.
    id_number = 0

    objects = players
    invalid_attributes = ["id"]

    def __init__(self, id, name: str = 'None', hp: int = 0, mp: int = 0, party=None):
        super().__init__(id, name, hp, mp)
        self.__party = party

    def party(self, value):
        pass

# funcionality functions

def find_similiar_and_id(input_string):
    best_match = ''
    best_score = 0
    for i in player.objects:
        obj = i.name
        obj_id = i.id
        score = fuzz.ratio(input_string, obj)
        if score > best_score:
            best_match = obj
            best_score = score
    return best_match, obj_id


    
        
            
