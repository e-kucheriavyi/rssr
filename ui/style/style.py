from typing import Union

from rssr.shared import validate_positive_int
from .color import Color
from .alignment import (AlignmentValue, validate_alignment)
from .direction import (DirectionValue, validate_direction)


class Style:
    _bg: Union[Color, None] = None
    _fg: Union[Color, None] = None

    _gap: int = 0
    _padding: int = 0

    _direction: DirectionValue = 'row'
    _alignment: AlignmentValue = 'center'

    def __init__(
        self,
        fg: Union[Color, None] = None,
        bg: Union[Color, None] = None,
        gap: int = 0,
        padding: int = 0,
        alignment: AlignmentValue = 'center',
        direction: DirectionValue = 'row',
    ):
        Style.validate_color('fg', fg)
        Style.validate_color('bg', bg)
        validate_positive_int(gap)
        validate_positive_int(padding)
        validate_alignment(alignment)
        validate_direction(direction)

        self._fg = fg
        self._bg = bg

        self._gap = gap
        self._padding = padding
        self._alignment = alignment
        self._direction = direction

    @staticmethod
    def validate_color(key: str, value: Union[Color, None]):
        if value and not isinstance(value, Color):
            raise ValueError(f'{key} must be Color object')
        return True

    @property
    def bg(self) -> Union[Color, None]:
        '''Background color'''
        return self._bg

    @property
    def fg(self) -> Union[Color, None]:
        '''Text color'''
        return self._fg

    @property
    def gap(self) -> int:
        '''Distance between children'''
        return self._gap

    @property
    def padding(self) -> int:
        '''Padding from container border to children'''
        return self._padding

    @property
    def alignment(self) -> AlignmentValue:
        return self._alignment

    @property
    def direction(self) -> DirectionValue:
        return self._direction

    def copy(self):
        return self.__class__(
            self.fg.copy() if self.fg else None,
            self.bg.copy() if self.bg else None,
            self.gap,
            self.padding,
            self.alignment,
            self.direction,
        )
