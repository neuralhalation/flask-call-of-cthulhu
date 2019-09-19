import app.functions.add_remove as ar


def phobia_or_mania(name, description):
    return ar.new("phobia_or_mania", name=name, description=description)


def add_phobia_or_mania(phobia_or_mania, phobias_or_manias=[]):
    return ar.add_to_list(phobia_or_mania, phobias_or_manias)


def remove_phobia_or_mania(phobia_name, phobias_or_manias):
    return ar.remove_by_obj_key_and_val_key(
        "phobia_or_mania", "name", phobia_name, phobias_or_manias
    )
