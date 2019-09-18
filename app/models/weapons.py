from app.functions.difficulty_calculator import (
    calculate_hard_difficulty,
    calculate_extreme_difficulty,
)


def add_weapons(weapon, weapons=[]):
    new_weapons = []
    if weapon not in weapons:
        new_weapons = weapons.__add__([weapon])
    return new_weapons


def remove_weapon(weapon_name, weapons):
    return [w for w in weapons if w["weapon"]["name"] != weapon_name]


def weapon(name, regular, damage, attack_range, attacks, ammo, malfunction):
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
