def luck(current_points, max_points=99):
    """Generates the luck score for a character.

    Args:
        current_points (int): The current luck points a character has.
        max_points (int): The maximum number of points possible.

    Return:
        dict: The luck score of a character.
    """
    return {"luck": {"current": current_points, "max": max_points}}
