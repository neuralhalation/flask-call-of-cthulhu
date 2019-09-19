import app.functions.add_remove as ar


def hit_points(current_points, max_points=20):
    """Returns a character's hit points.

    Args:
        current_points (int): The current number of hit points a character has.
        max_points (int): The maximum points possible.

    Return:
        dict: A character's hit points.
    """
    return ar.new("hit_points", current=current_points, max=max_points)
