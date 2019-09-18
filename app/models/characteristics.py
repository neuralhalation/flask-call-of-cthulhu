from app.functions.difficulty_calculator import (
    calculate_hard_difficulty,
    calculate_extreme_difficulty,
)


def build_characteristics(
    strength,
    dexterity,
    intelligence,
    constitution,
    apptitude,
    power,
    size,
    education,
    move_rate,
):
    """Creates a characteristics object for the character based on their base
    score.

    Args:
        strength (int): The whole number representing the percentile score for
        strength.
        dexterity (int): The whole number representing the percentile score for
        dexterity.
        intelligence (int): The whole number representing the percentile score
        for intelligence.
        constitution (int): The whole number representing the percentile score
        for constitution.
        apptitude (int): The whole number representing the percentile score for
        apptitude.
        power (int): The whole number representing the percentile score for
        power.
        size (int): The whole number representing the percentile score for
        size.
        education (int): The whole number representing the percentile score for
        education.
        move_rate (int): The whole number representing the percentile score for
        move rate.

    Return:
        dict: A character's basic characteristic scores with difficulties.
    """
    return {
        "strength": {
            "normal": strength,
            "hard": calculate_hard_difficulty(strength),
            "extreme": calculate_extreme_difficulty(strength),
        },
        "dexterity": {
            "normal": dexterity,
            "hard": calculate_hard_difficulty(dexterity),
            "extreme": calculate_extreme_difficulty(dexterity),
        },
        "intelligence": {
            "normal": intelligence,
            "hard": calculate_hard_difficulty(intelligence),
            "extreme": calculate_extreme_difficulty(intelligence),
        },
        "constitution": {
            "normal": constitution,
            "hard": calculate_hard_difficulty(constitution),
            "extreme": calculate_extreme_difficulty(constitution),
        },
        "apptitude": {
            "normal": apptitude,
            "hard": calculate_hard_difficulty(apptitude),
            "extreme": calculate_extreme_difficulty(apptitude),
        },
        "power": {
            "normal": power,
            "hard": calculate_hard_difficulty(power),
            "extreme": calculate_extreme_difficulty(power),
        },
        "size": size,
        "education": {
            "normal": education,
            "hard": calculate_hard_difficulty(education),
            "extreme": calculate_extreme_difficulty(education),
        },
        "move_rate": {
            "normal": move_rate,
            "hard": calculate_hard_difficulty(move_rate),
            "extreme": calculate_extreme_difficulty(move_rate),
        },
    }
