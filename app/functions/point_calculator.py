def add_points(current_total, points_added, max_possible):
    """Adds points to a character's score.

    Args:
        current_total (int): The current number of points.
        points_added (int): The points to add.
        max_possible (int): The maximum points possible for the trait.

    Return:
        int: The new number of points.
    """
    if current_total + points_added > max_possible:
        return max_possible
    else:
        return current_total + points_added


def subtract_points(current_total, points_subtracted, min_possible=0):
    """Subtracts points from a character's score.

    Args:
        current_total (int): The current number of points.
        points_subtracted (int): The points to subtract.
        min_possible (int): The minimum points possible.

    Return:
        int: The new number of points.
    """
    if current_total - points_subtracted < min_possible:
        return min_possible
    else:
        return current_total - points_subtracted
