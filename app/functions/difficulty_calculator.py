import math


def calculate_hard_difficulty(base_score):
    """Hard difficulty is calculated by taking the character's
    base characteristic score and multiplying it by 1/2.

    Args:
        base_score (float): The character's base score.

    Return:
        float: The hard difficulty score.
    """
    return math.trunc(base_score * (1/2))


def calculate_extreme_difficulty(base_score):
    """ Extreme difficulty is calculated by taking the character's
    base characteristic score and multiplying it by 1/5.

    Args:
        base_score (float): The character's base score.

    Return:
        float: The extreme difficulty score.
    """
    return math.trunc(base_score * (1/5))
