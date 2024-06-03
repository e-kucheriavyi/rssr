'''A validator for positive integers'''


def validate_positive_int(value: int) -> bool:
    '''Validating that the value is `int` and is positive'''
    if not isinstance(value, int):
        raise ValueError(f'Value must be int: {value}')
    if value < 0:
        raise ValueError(f'Value must be positive: {value}')
    return True
