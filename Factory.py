import inspect
from Player import player
from Database import players


# def factory(class_in_use, fill=False):
#     if fill:
        


def id_generator(class_in_use):
    letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    while True:
        yield f"{class_in_use.class_identifier}_{letters[class_in_use.current_letter]}{class_in_use.id_number}"
        if class_in_use.id_number == 100:
            class_in_use.current_letter += 1
            class_in_use.id_number += 1
        else:
            class_in_use.id_number += 1


def get_attrs(class_in_use):
    attrs = []
    sig = inspect.signature(class_in_use.__init__)
    for name, param in sig.parameters.items():
        attrs.append(name)
    return attrs


def create_object(class_in_use, id):
    if id not in class_in_use.objects:
        class_in_use.objects[id] = class_in_use(id)
    return class_in_use.objects[id]


factory(player, True)
