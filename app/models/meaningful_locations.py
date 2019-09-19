import app.functions.add_remove as ar


def meaningful_location(location_name, description):
    return ar.new("meaningful_location", name=location_name, description=description)


def add_meaningful_location(location, locations=[]):
    return ar.add_to_list(location, locations)


def remove_meaningful_location(location_name, locations):
    return ar.remove_by_obj_key_and_val_key(
        "meaningful_location", "name", location_name, locations
    )
