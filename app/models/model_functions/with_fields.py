from app.functions.key_formatter import format_from_name
from wtforms import IntegerField
import app.functions.difficulty_calculator as dc


def with_fields(name, default_value):
    return {
        format_from_name(name): {
            "normal": IntegerField(f"Base - {name}", default=default_value),
            "hard": IntegerField(
                f"Hard - {name}", default=dc.calculate_hard_difficulty(default_value)
            ),
            "extreme": IntegerField(
                f"Extreme - {name}",
                default=dc.calculate_extreme_difficulty(default_value),
            ),
        }
    }
