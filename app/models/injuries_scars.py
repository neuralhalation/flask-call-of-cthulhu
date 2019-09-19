import app.functions.add_remove as ar


def injury_or_scar(description):
    return ar.new("injury_or_scar", description=description)


def add_injury_or_scar(injury_or_scar, injuries_or_scars=[]):
    return ar.add_to_list(injury_or_scar, injuries_or_scars)


def remove_injury_or_scar(injury_or_scar, injuries_or_scars):
    return ar.remove_by_obj(injury_or_scar, injuries_or_scars)
