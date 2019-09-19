def new(key, **kwargs):
    return {key: {kwargs}}


def add_to_list(obj, old_list):
    new_list = []
    if obj not in old_list:
        new_list = old_list.__add__([obj])
    return new_list


def remove_by_obj(obj, old_list):
    return [o for o in old_list if o != obj]


def remove_by_obj_key_and_val_key(obj_key, val_key, val, old_list):
    return [o for o in old_list if o[obj_key][val_key] != val]
