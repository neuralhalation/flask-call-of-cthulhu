import app.functions.add_remove as ar


def encounter(description):
    return ar.new("encounter", description=description)


def add_encounter(encounter, encounters=[]):
    return ar.add_to_list(encounter, encounters)


def remove_encounter(encounter, encounters):
    return ar.remove_by_obj(encounter, encounters)
