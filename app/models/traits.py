import app.functions.add_remove as ar


def trait(trait_name, description):
    return ar.new("trait", name=trait_name, description=description)


def add_trait(trait, traits=[]):
    return ar.add_to_list(trait, traits)


def remove_trait(trait_name, traits):
    return ar.remove_by_obj_key_and_val_key("trait", "name", trait_name, traits)
