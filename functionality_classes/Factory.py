import inspect
from Database import classes_generators
from classes import Player


def factory(class_in_use, generate=1 ,fill=False):
    if fill:
        for _ in range(generate):
            obj = create_object(class_in_use)
            for attribute in get_attrs(class_in_use):
                if attribute not in class_in_use.invalid_attributes:
                    while True:
                        attribute_type = type(getattr(obj, attribute))
                        try:
                            print(f"{obj.__class__.__name__}-id:{obj.id}")
                            user_input = attribute_type(input(f"A value for {attribute}: "))
                            setattr(obj, attribute, user_input)
                            break
                        except ValueError:
                            type_representation = str(attribute_type).split("'")[1]
                            print(f"the entered value, didn't match with the attribute({attribute}) type: {type_representation}.")
    else:
        for _ in range(generate):
            create_object(class_in_use)


def id_generator(class_in_use):
    letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "L", "M",
               "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    while True:
        yield f"{class_in_use.class_identifier}_{letters[class_in_use.current_letter]}{class_in_use.id_number:03}"
        # when the object reach the number 1000, so, the generation is changed, going to next letter
        if class_in_use.id_number == 1000:
            class_in_use.current_letter += 1
            class_in_use.id_number = 1
        else: # else, it just increase the number of the object id
            class_in_use.id_number += 1


# to get attributes from the class
def get_attrs(class_in_use):
    attrs = []
    sig = inspect.signature(class_in_use)
    for attribute_name, _ in sig.parameters.items():
        attrs.append(attribute_name)
    return attrs


def create_object(class_in_use):
    class_objects = class_in_use.objects
    class_identifier = class_in_use.class_identifier
    if class_identifier not in classes_generators: # check if class's generator already exists
        classes_generators[class_identifier] = id_generator(class_in_use) # if not, the generator is add
    id = next(classes_generators[class_identifier])
    #verify if the id generated don't exists
    if id not in class_objects: 
        key = class_in_use(id)
        class_objects[id] = key
    return class_objects[id]

factory(player, 5)
