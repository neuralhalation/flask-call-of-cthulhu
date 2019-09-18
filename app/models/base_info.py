def base_info(name, player, occupation, age, gender, residence, birthplace):
    """Creates the basic info of the character.

    Args:
        name (str): The character's name.
        player (str): The player's name.
        occupation (str): The player's occupation.
        age (int): The age of the character.
        gender (string): The gender the character identifies as.
        residence (string): The character's place of residence.
        birthplace (string): The character's place of birth.

    Return:
        dict: The basic character information.
    """
    return {
        "base_info": {
            "name": name,
            "player": player,
            "occupation": occupation,
            "age": age,
            "gender": gender,
            "residence": residence,
            "birthplace": birthplace,
        }
    }
