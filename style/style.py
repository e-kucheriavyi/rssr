from style.color import Color
from style.alignment import (Alignment, validadate_alignment)
from style.direction import (Direction, validadate_direction)


class Style:
    _bg = None
    _fg = None

    _gap = 0
    _padding = 0

    _direction = None
    _alignment = None

    def __init__(
        self,
        fg = None,
        bg = None,
        gap = 0,
        padding = 0,
        alignment = Alignment.CENTER,
        direction = Direction.ROW,
    ):
        Style.validate_color('fg', fg)
        Style.validate_color('bg', bg)
        validate_positive_int(gap)
        validate_positive_int(padding)
        validadate_alignment(alignment)
        validate_direction(direction)

        self._fg = fg
        self._bg = bg

        self._gap = gap
        self._padding = padding
        self._alignment = alignment
        self._direction = direction

    @staticmethod
    def validate_color(key: str, value: Color):
        if color and not isinstance(value, Color):
            raise ValueError(f'{key} must be Color object')

    @property
    def bg(self):
        return self._bg

    @property
    def fg(self):
        return self._fg

