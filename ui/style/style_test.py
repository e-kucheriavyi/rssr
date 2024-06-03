import pytest

from .style import Style
from .color import Color


def test_style_validation():
    with pytest.raises(ValueError):
        Style(gap=-1)

    with pytest.raises(ValueError):
        Style(padding=-1)

    with pytest.raises(ValueError):
        Style(alignment='')

    with pytest.raises(ValueError):
        Style(direction='')

    with pytest.raises(ValueError):
        Style(fg=(255, 255, 255))

    with pytest.raises(ValueError):
        Style(bg=(255, 255, 255))


def test_style_copy():
    values = {
        'fg': Color(100, 200, 50, 15),
        'bg': Color(50, 200, 100, 15),
        'gap': 5,
        'padding': 6,
        'alignment': 'right',
        'direction': 'row',
    }
    s = Style(**values)

    c = s.copy()

    assert values['fg'].value == c.fg.value
    assert values['bg'].value == c.bg.value
    assert values['gap'] == c.gap
    assert values['padding'] == c.padding
    assert values['alignment'] == c.alignment
    assert values['direction'] == c.direction
