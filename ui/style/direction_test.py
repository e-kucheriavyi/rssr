'''Tests for layout direction'''

import pytest

from .direction import validate_direction


def test_validate_direction():
    '''Tests for layout direction validator'''
    assert validate_direction('row') is True
    assert validate_direction('column') is True

    with pytest.raises(ValueError):
        validate_direction('bottom')
        validate_direction('any')
        validate_direction('')
