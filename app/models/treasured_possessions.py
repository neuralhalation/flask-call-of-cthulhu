import app.functions.add_remove as ar


def treasured_possession(possession_name, description):
    return ar.new("treasured_possession", name=possession_name, description=description)


def add_treasured_possession(possession, possessions=[]):
    return ar.add_to_list(possession, possessions)


def remove_treasured_possession(possession_name, possessions):
    return ar.remove_by_obj_key_and_val_key(
        "treasured_possession", "name", possession_name, possessions
    )

