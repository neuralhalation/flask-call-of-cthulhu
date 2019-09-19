import app.functions.add_remove as ar


def fellow_investigator(char_name, player_name):
    """Creates a new fellow investigator.

    Args:
        char_name (str): The fellow investigator character name.
        player_name (str): The fellow investigator player name.

    Return:
        dict: A fellow investigator
    """
    return ar.new(
        "fellow_investigator", character_name=char_name, player_name=player_name
    )


def add_fellow_investigators(investigator, investigators=[]):
    """Adds an investigator to the list of fellow investigators and returns
    a new list.

    Args:
        investigator (dict): A fellow investigator object.
        investigators (list): A list of fellow investigators.

    Return:
        list: A list of fellow investigators.
    """
    return ar.add_to_list(investigator, investigators)


def remove_fellow_investigators(char_name, investigators):
    """Removes a fellow investigator from the fellow investigators list.

    Args:
        char_name (str): The character name to be removed.
        investigators (list): A list of fellow investigators.
    """
    return ar.remove_by_obj_key_and_val_key(
        "fellow_investigator", "character_name", char_name, investigators
    )
