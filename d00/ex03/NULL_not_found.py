def NULL_not_found(object: any) -> int:
    obj_name = type(object).__name__
    if obj_name == 'NoneType' and object is None:
        print(f"Nothing : {object} ", end='')
    elif obj_name == 'float' and object != object:
        print(f"Cheese : {object} ", end='')
    elif obj_name == 'int' and object == 0:
        print(f"Zero : {object} ", end='')
    elif obj_name == 'str' and object == '':
        print(f"Empty : {object} ", end='')
    elif obj_name == 'bool' and object is False:
        print(f"Fake : {object} ", end='')
    else:
        print("Type not Found")
        return 1
    print(type(object))
    return 0
