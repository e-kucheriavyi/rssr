def validate_positive_int(value: int):
    if not type(value) is int:
        raise Exception('Value must be int')
    if value < 0:
        raise Exception('Value must be positive')
