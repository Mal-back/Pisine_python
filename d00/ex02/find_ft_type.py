def all_thing_is_obj(object: any) -> int:
    object_name = type(object).__name__
    match object_name:
        case 'list':
            print("List : ", end='')
        case 'tuple':
            print("Tuple : ", end='')
        case 'set':
            print("Set : ", end='')
        case 'dict':
            print("Dict : ", end='')
        case 'str':
            print(f"{object} is in the kitchen : ", end='')
        case _:
            print("Type not found")
            return 42
    print(type(object))
    return 42
