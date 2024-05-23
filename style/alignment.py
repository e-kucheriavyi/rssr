class Alignment:
    LEFT = 'left'
    RIGHT = 'right'
    CENTER = 'center'


def validadate_alignment(value: str):
    if not value in [Alignment.LEFT, Alignment.RIGHT, Alignment.CENTER]:
        raise ValueError(f'Invalid alignment: {value}')
