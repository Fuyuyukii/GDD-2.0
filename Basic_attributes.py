class Basic_attributes:

    def __init__(self, id, name: str = 'None', hp: int = 0, mp: int = 0, party=None):
        self.__id = id
        self.__name = name
        self.__lvl = 1
        self.__party = party
        self.__experience = 0
        self.__inventory = list()
        self.__Max_hp = hp
        self.__hp = hp
        self.__Max_mp = mp
        self.__mp = mp

    # Attributes Properties

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
    def lvl(self):
        return self.__lvl

    @lvl.setter
    def lvl(self, value):
        self.__lvl = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @property
    def mp(self):
        return self.__mp

    @mp.setter
    def mp(self, value):
        self.__mp = value

    @property
    def Max_hp(self):
        return self.__Max_hp

    @Max_hp.setter
    def Max_hp(self, value):
        self.__Max_hp = value

    @property
    def Max_mp(self):
        return self.__Max_mp

    @Max_mp.setter
    def mp(self, value):
        self.__Max_mp = value

    # Attributes Properties

    @property
    def party(self):
        return self.__party

    @party.setter
    def party(self, value): # tem q dar um mexida nisso aqui, n ta feito direito
        self.__party = value

    @property
    def inventory(self):
        return self.__inventory

    def inventory_add(self, value):
        self.__inventory.append(value)
    
    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def gain_experience(self, value):
        self.__experience = value
