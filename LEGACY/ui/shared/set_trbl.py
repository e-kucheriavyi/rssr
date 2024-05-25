from ui.types.positive_int import validate_positive_int


def set_trbl(value) -> tuple:
    '''
    trbl == top_right_bottom_left
    Sets value for 4-directional params. E. g. padding.
    There are three possible args:
    1. Value itself — 4, 2 etc. In that case it will be set to all 4 directions.
    2. Tuple of 2 items — vertical and horizontal.
    3. Tuple of 4 items — top, right, bottom, left.
    '''
    if type(value) is int:
        validate_positive_int(value)
        return (value, value, value, value)

    if not type(value) is tuple:
        raise Exception('Value must should be `int` or `tuple` of ints')

    for i in value:
        validate_positive_int(i)

    l = len(value)

    if l == 2:
        v, h = value
        return (v, h, v, h)

    if l == 4:
        return value

    raise Exception('Value tuple must contain 2 (v, h) or 4 items (top, right, bottom, left)')
