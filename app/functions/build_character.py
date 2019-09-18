def build_character(
    base_info,
    background,
    characteristics,
    fellow_investigators,
    hit_points,
    inventory,
    luck,
    magic,
    sanity,
    skills,
    weapons,
):
    """Builds a character object.

    Args:
        base_info (dict): The base character information.
        background (dict): The character background information.
        characteristics (dict): The character characteristics information.
        fellow_investigators (dict): The fellow investigators tied to the
        character.
        hit_points (dict): The character's hit point information.
        inventory (dict): The character's inventory information.
        luck (dict): The character's luck information.
        magic (dict): The character's magic information.
        sanity (dict): The character's sanity information.
        skills (dict): The character's skill information.
        weapons (dict): The character's weapons information.

    Return:
        dict: A completed character sheet.
    """
    return {
        "character": {
            base_info,
            background,
            characteristics,
            fellow_investigators,
            hit_points,
            inventory,
            luck,
            magic,
            sanity,
            skills,
            weapons,
        }
    }
