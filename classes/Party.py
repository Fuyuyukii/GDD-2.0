from functionality_classes.Database import parties


class party:
    class_identifier = "PT"
    current_letter = 0  # show in which generation the object are in.
    id_number = 0

    objects_storage = parties
    invalid_attributes = ["id"]

    def __init__(self, id, name='N/A'):
        self.__id = id
        self.__name = name
        self.__members = {}

    # internal functions

    def add_member(self, member):
        self.__members[member.id] = member

    # properties

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

    @property
    def members(self):
        return self.__members
