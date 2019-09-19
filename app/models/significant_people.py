import app.functions.add_remove as ar


def significant_person(npc_name, description):
    """Creates a new significant person/NPC for a character to know, keep track
    of.

    Args:
        npc_name (str): The name of the NPC.
        description (str): The description of the NPC.

    Return:
        dict: An NPC/Significant Person
    """
    return ar.new("significant_person", name=npc_name, description=description)


def add_significant_person(significant_person, significant_persons=[]):
    """Adds a significant person to the list of significant persons.

    Args:
        significant_person (dict): A significant person or NPC the character
        knows.
        significant_persons (list): A list of significant persons.

    Return:
        list: A list of significant persons.
    """
    return ar.add_to_list(significant_person, significant_persons)


def remove_significant_persons(person_name, significant_persons):
    """Removes a significant person from the list of significant persons.

    Args:
        person_name (str): The name of the person.
        significant_persons (list): The list of significant persons.

    Return:
        list: A new list of significant persons
    """
    return ar.remove_by_obj_key_and_val_key(
        "significant_person", "name", person_name, significant_persons
    )
