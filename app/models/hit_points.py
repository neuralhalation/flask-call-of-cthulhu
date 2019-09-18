def hit_points(current_points, max_points=20):
    """Returns a character's hit points.

    Args:
        current_points (int): The current number of hit points a character has.
        max_points (int): The maximum points possible.

    Return:
        dict: A character's hit points.
    """
    return {"hit_points": {"current": current_points, "max": max_points}}
