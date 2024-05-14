from ui.types import validate_byte


def set_color(value: int|tuple) -> tuple:
    if type(value) is int:
        validate_byte(value)
        return (value, value, value, 255)

    if not type(value) is tuple:
        raise Exception('Color must be `int` or `tuple[int]`')

    for i in value:
        validate_byte(i)

    l = len(value)

    if l == 3:
        r, g, b = value
        return (r, g, b, 255)

    if l == 4:
        return value

    raise Exception('Color tuple must contain 3 (r, g, b) or 4 items (r, g, b, a)')
