import math

def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: none", type(object))
    elif isinstance(object, float):
        if math.isnan(object):
            print("Cheese: nan", type(object))
    elif isinstance(object, int):
        print("Zero: 0", type(object))
    elif isinstance(object, str):
        print("Empty: ", type(object))
    elif isinstance(object, bool):
        print("Fake: False", type(object))
    else:
        print("Type not Found")
    return 0