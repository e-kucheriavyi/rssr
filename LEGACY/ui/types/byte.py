def validate_byte(value: int):
    if value < 0 or value > 255:
        raise Exception('Value must be between 0 and 255')
