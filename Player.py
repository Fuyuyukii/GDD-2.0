from Database import players


class player:
    class_identifier = "PL"
    current_letter = 0  # show in which generation the object are in.
    id_number = 0
    objects = players

    def __init__(self, id, name:str=None):
        self.__id = id
        self.__name = name

    # Properties

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value 