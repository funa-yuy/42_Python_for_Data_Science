#
# nanの扱い、is と == の違いを学ぶ
#

def NULL_not_found(object: any) -> int:
    # your code here
    object_type = type(object)

    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif object_type is float and object != object:
        # nanは、nanではない。nan == nanはFalse
        print(f"Cheese: {object} {type(object)}")
    elif object_type is int and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif object_type is str and object == "":
        print(f"Empty: {object} {type(object)}")
    elif object_type is bool and object is False:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
        return (1)
    return (0)
