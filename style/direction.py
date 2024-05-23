class Direction:
    ROW = 'row'
    COLUMN = 'column'


def validadate_direction(value: str):
    if not value in [Direction.ROW, Direction.COLUMN]:
        raise ValueError(f'Invalid direction: {value}')
