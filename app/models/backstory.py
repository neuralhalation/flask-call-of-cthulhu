def backstory(
    personal_description,
    ideology_beliefs,
    significant_people,
    meaningful_locations,
    treasured_possessions,
    traits,
    injuries_and_scars,
    phobias_and_manias,
    arcane_tomes_spells_artifacts,
    encounters,
):
    """Creates the backstory data structure.

    Args:
        personal_description (str): The description of the character.
        ideology_beliefsf (str): The beliefs of the character.
        significant_people (list): A list of people the character knows.
        meaningful_locations (list): A list of locations the character knows.
        treasured_possessions (list): A list of items.
        traits (list): A list of character traits.
        injuries_and_scars (list): A list of injuries and/or scars.
        phobias_and_manias (list): A list of phobias and/or manias.
        arcane_tomes_spells_artifacts (list): A list of arcane items.
        encounters (list): A list of encounters.

    Return:
        dict: A character's backstory.
    """
    return {
        "backstory": {
            "personal_description": personal_description,
            "ideology_beliefs": ideology_beliefs,
            "significant_people": significant_people,
            "meaningful_locations": meaningful_locations,
            "treasured_possessions": treasured_possessions,
            "traits": traits,
            "injuries_and_scars": injuries_and_scars,
            "phobias_and_manias": phobias_and_manias,
            "arcane_tomes_spells_artifacts": arcane_tomes_spells_artifacts,
            "encounters": encounters,
        }
    }
