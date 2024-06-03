'''Layout alignment'''

from typing import Literal


ALIGNMENTS = ('left', 'right', 'center')
type AlignmentValue = Literal[ALIGNMENTS]


def validate_alignment(value: AlignmentValue) -> bool:
    '''Validating alignment value'''
    if not value in ALIGNMENTS:
        raise ValueError(f'Invalid alignment: {value}')
    return True
