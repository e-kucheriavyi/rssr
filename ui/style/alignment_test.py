'''Tests for layout alignment'''

import pytest

from .alignment import validate_alignment


def test_validate_alignment():
    '''Tests for layout alignment validator'''
    assert validate_alignment('left') is True
    assert validate_alignment('right') is True
    assert validate_alignment('center') is True

    with pytest.raises(ValueError):
        validate_alignment('middle')
        validate_alignment('bottom')
        validate_alignment('any')
        validate_alignment('')
