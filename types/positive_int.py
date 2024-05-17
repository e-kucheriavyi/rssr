def validate_positive_int(value: int):
    if not type(value) is int:
        raise Exception(f'Value must be int: {value}')
    if value < 0:
        raise Exception(f'Value must be positive: {value}')
