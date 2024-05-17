from ui.shared import (
    set_color,
    set_trbl,
)
from ui.types import (
    validate_positive_int,
    validate_alignment,
    validate_direction,
)


def validate_style(style:dict):
    validators = {
        'bg': set_color,
        'fg': set_color,
        'padding': set_trbl,
        'size': validate_positive_int,
        'gap': validate_positive_int,
        'direction': validate_direction,
        'alignment': validate_alignment,
    }

    for key in style:
        if key not in validators:
            continue
        validators[key](style[key])
