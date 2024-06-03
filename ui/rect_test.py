'''Rect tests'''

import pytest

from .rect import Rect


def test_rect():
    '''Testing valid rect values'''

    values = (22, 35, 14, 17)

    r = Rect(*values)

    assert r.rect == values
    assert r.position == (22, 35)
    assert r.dimensions == (14, 17)

    assert r.x == 22
    assert r.y == 35
    assert r.width == 14
    assert r.height == 17


def test_rect_validation():
    '''Testing rect validation'''

    with pytest.raises(ValueError):
        Rect(-1, 0, 0, 0)

    with pytest.raises(ValueError):
        Rect(0, -1, 0, 0)

    with pytest.raises(ValueError):
        Rect(0, 0, -1, 0)

    with pytest.raises(ValueError):
        Rect(0, 0, 0, -1)


def test_rect_collision():
    '''Testing rect collisions'''

    r = Rect(5, 5, 20, 20)
    for x in range(r.x, r.x + r.width):
        for y in range(r.y, r.y + r.height):
            assert r.collide(x, y) is True

    assert r.collide(r.x - 1, r.y + 1) is False
    assert r.collide(r.x + 1, r.y - 1) is False


def test_rect_collision_validation():
    '''Testing validation for rect collision'''

    with pytest.raises(ValueError):
        Rect(5, 5, 20, 20).collide(-1, 10)

    with pytest.raises(ValueError):
        Rect(5, 5, 20, 20).collide(10, -1)
