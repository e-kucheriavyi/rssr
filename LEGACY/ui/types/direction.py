DIRECTIONS = ('row', 'column')


def validate_direction(value: str):
    if value not in DIRECTIONS:
        raise Exception('Invalid direction')
