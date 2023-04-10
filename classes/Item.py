from functionality_classes.Database import items


class item:
    class_identifier = "IT"
    current_letter = 0  # show in which generation the object are in.
    id_number = 0

    objects_storage = items
    invalid_attributes = ["id"]

    items_ranks = {"F": ["F-", "F", "F+"], "D": ["D-", "D", "D+"], "C": ["C-", "C", "C+"],
                   "B": ["B-", "B", "B+"], "A": ["A-", "A", "A+"], "S": ["S-", "S", "S+"]}

    def __init__(self, id, name='N/A', rank='N/A', classification='N/A', value=0,
                 description='', lore=''):
        self.__id = id
        self.__name = name
        self.__rank = rank
        self.__classification = classification
        self.__value = value
        self.__description = description
        self.__lore = lore
        self.__effects = []
        self.__stats = []

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
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, value):
        if value in item.items_ranks.items():
            self.__rank = value
        else:
            print("Unknown rank")

    @property
    def classification(self):
        return self.__classification

    @classification.setter
    def classification(self, value):
        self.__classification = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def lore(self):
        return self.__lore

    @lore.setter
    def lore(self, value):
        self.__lore = value

    @property
    def effects(self):
        return self.__effects

    @effects.setter
    def effects(self, value):
        self.__effects.append(value)

    @property
    def stats(self):
        return self.__stats

    @stats.setter
    def stats(self, value):
        self.__stats.append(value)