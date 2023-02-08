import inspect
from Player import player
from Database import players


def factory(class_in_use, fill=False):
    if fill:
        obj = create_object(class_in_use)
        for attribute in get_attrs(class_in_use):
            attribute_type = type(obj.attribute)
            if attribute not in class_in_use.invalid_attributes:
                setattr(obj, attribute, attribute_type(input(f"A value for {attribute}: ")))


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
    sig = inspect.signature(class_in_use)
    for name, param in sig.parameters.items():
        attrs.append(name)
    return attrs


def create_object(class_in_use):
    class_objects = class_in_use.objects

    id = next(id_generator(class_in_use))

    if id not in class_objects:
        key = class_in_use(id)
        class_objects[id] = key
    return class_objects[id]


factory(player, True)
