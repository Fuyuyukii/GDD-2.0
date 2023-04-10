from classes.Item import item
from functionality_classes.Database import weapons, players
from functionality_classes.general_features import find_similar_name


class weapon(item):
    class_identifier = "WP"
    current_letter = 0  # show in which generation the object are in.
    id_number = 0

    objects_storage = weapons
    invalid_attributes = ["id"]

    def __init__(self, id, name='N/A', rank='N/A', value=0, description='', lore=''):
        super().__init__(id, name, rank, value, description, lore)
        self.__damage = 0
        self.__range = 0
        self.__classification = "Weapons"
        self.__size_categorie = 0
        self.__carrier = ""

    # properties

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    @property
    def size_category(self):
        return self.__size_categorie

    @size_category.setter
    def size_category(self, value):
        self.__size_categorie = value

    @property
    def carrier(self):
        return self.__carrier

    @carrier.setter
    def carrier(self, value):
        try:
            player_id = find_similar_name(value, players)
            player_id.inventory_add(self.id, self)
            self.__carrier = player_id
        except AttributeError as e:
            print("Error setting party:", e)
