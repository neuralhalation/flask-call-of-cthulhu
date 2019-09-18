def fellow_investigator(char_name, player_name):
    """Creates a new fellow investigator.

    Args:
        char_name (str): The fellow investigator character name.
        player_name (str): The fellow investigator player name.

    Return:
        dict: A fellow investigator
    """
    return {
        "fellow_investigator": {"character_name": char_name, "player_name": player_name}
    }


def add_fellow_investigators(investigator, investigators=[]):
    """Adds an investigator to the list of fellow investigators and returns
    a new list.

    Args:
        investigator (dict): A fellow investigator object.
        investigators (list): A list of fellow investigators.

    Return:
        list: A list of fellow investigators.
    """
    new_investigators = []
    if investigator not in investigators:
        new_investigators = investigators.__add__([investigator])
    return new_investigators


def remove_fellow_investigators(char_name, investigators):
    """Removes a fellow investigator from the fellow investigators list.

    Args:
        char_name (str): The character name to be removed.
        investigators (list): A list of fellow investigators.
    """
    return [i for i in investigators if i["fellow_investigator"]["name"] != char_name]
