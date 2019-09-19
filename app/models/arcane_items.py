import app.functions.add_remove as ar


def arcane_item(name, description):
    return ar.new("arcane_item", name=name, description=description)


def add_arcane_item(arcane_item, arcane_items=[]):
    return ar.add_to_list(arcane_item, arcane_items)


def remove_arcane_item(name, arcane_items):
    return ar.remove_by_obj_key_and_val_key("arcane_item", "name", name, arcane_items)

