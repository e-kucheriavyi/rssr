'''Layout direction'''

from typing import Literal


DIRECTIONS = ('row', 'column')
type DirectionValue = Literal[DIRECTIONS]


def validate_direction(value: DirectionValue):
    '''Validation layout direction'''
    if not value in DIRECTIONS:
        raise ValueError(f'Invalid direction: {value}')
    return True
