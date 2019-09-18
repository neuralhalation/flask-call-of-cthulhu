def magic_points(current_points, max_points=24):
    """Creates the number of magic points a character has.

    Args:
        current_points (int): The current number of points the character has.
        max_points (int): The maximum points possible.

    Return:
        dict: The magic points of a character.
    """
    return {"magic_points": {"current": current_points, "max": max_points}}
