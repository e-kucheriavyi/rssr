'''Testing Color'''

import pytest

from .color import Color


def test_color():
    '''Testing valid color values'''
    r, g, b, a = values = (233, 234, 235, 236)

    c = Color(*values)
    assert c.value == values
    assert c.r == r
    assert c.g == g
    assert c.b == b
    assert c.a == a


def test_color_validation():
    '''Testing color validation'''
    invalid_cases = (
        (256, 255, 255, 255),
        (255, 256, 255, 255),
        (255, 255, 256, 255),
        (255, 255, 255, 256),
        (-1, 0, 0, 0),
        (0, -1, 0, 0),
        (0, 0, -1, 0),
        (0, 0, 0, -1),
        (0.1, 0, 0, 0),
        (0, 0.1, 0, 0),
        (0, 0, 0.1, 0),
        (0, 0, 0, 0.1),
    )

    for c in invalid_cases:
        with pytest.raises(ValueError):
            Color(*c)


def test_color_normalization():
    '''Testing color normalization'''
    nomalized_100 = 0.39215686274509803

    assert Color(255, 255, 255, 255).normalized_value == (1, 1, 1, 1)
    assert Color(100, 100, 100, 100).normalized_value == (
        nomalized_100,
        nomalized_100,
        nomalized_100,
        nomalized_100,
    )
    assert Color(0, 0, 0, 0).normalized_value == (0, 0, 0, 0)


def test_color_copy():
    r, g, b, a = values = (10, 20, 30, 40)

    c = Color(*values).copy()

    assert c.value == values
    assert c.r == r
    assert c.g == g
    assert c.b == b
    assert c.a == a
