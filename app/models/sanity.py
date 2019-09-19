import app.functions.add_remove as ar


def sanity(current_points, max_points=99):
    """Creates the sanity score for a character.

    Args:
        current_points (int): The number of points the character currently has.
        max_points (int): The maximum number of points possible.

    Return:
        dict: The sanity score for a character.
    """
    return ar.new("sanity", current=current_points, max=max_points)
