from app.functions.difficulty_calculator import (
    calculate_hard_difficulty,
    calculate_extreme_difficulty,
)
import app.functions.add_remove as ar


def add_weapons(weapon, weapons=[]):
    """Adds a weapon to the character's weapon inventory.

    Args:
        weapon (dict): A weapon object.
        weapons (list): The character's current inventory of weapons.

    Return:
        list: A list of the character's weapon inventory.
    """
    return ar.add_to_list(weapon, weapons)


def remove_weapon(weapon_name, weapons):
    """Removes a weapon from the character's weapon inventory.

    Args:
        weapon_name (str): The name of the weapon to be removed.
        weapons (list): The character's current inventory of weapons.

    Return:
        list: A list of the character's weapon inventory.
    """
    return ar.remove_by_obj_key_and_val_key("weapon", "name", weapon_name, weapons)


def weapon(name, regular, damage, attack_range, attacks, ammo, malfunction):
    """Creates a weapon object.

    Args:
        name (str): The name of the weapon.
        regular (int): The whole number representing the percentile of
        difficulty when using the weapon.
        damage (str): The dice damage dealt by the weapon.
        attacks (int): The number of attacks possible in a round with the 
        weapon.
        ammo (int): The amount of ammo available for that weapon.
        malfunction (int): The whole number representing the percentile chance
        of the weapon malfunctioning after a fumble.

    Return:
        dict: A weapon object.
    """
    return {
        "weapon": {
            "name": name,
            "regular": regular,
            "hard": calculate_hard_difficulty(regular),
            "extreme": calculate_extreme_difficulty(regular),
            "damage": damage,
            "attack_range": attack_range,
            "attacks": attacks,
            "ammo": ammo,
            "malfunction": malfunction,
        }
    }
