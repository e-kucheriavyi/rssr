'''Rect for components'''

from rssr.shared import validate_positive_int


class Rect:
    '''Any component's rectangle'''
    _x: int = 0
    _y: int = 0
    _width: int = 0
    _height: int = 0

    def __init__(self, x: int, y: int, width: int, height: int):
        validate_positive_int(x)
        validate_positive_int(y)
        validate_positive_int(width)
        validate_positive_int(height)

        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def collide(self, x: int, y: int) -> bool:
        '''Checking if point (x, y) is inside the rect'''
        validate_positive_int(x)
        validate_positive_int(y)

        if x < self._x or x > self._x + self._width:
            return False
        if y < self._y or y > self._y + self._height:
            return False
        return True

    @property
    def x(self) -> int:
        '''Rect's offset from screen left side'''
        return self._x

    @property
    def y(self) -> int:
        '''Rect's offset from screen top side'''
        return self._y

    @property
    def width(self) -> int:
        '''Rect's width'''
        return self._width

    @property
    def height(self) -> int:
        '''Rect's height'''
        return self._height

    @property
    def position(self) -> (int, int):
        '''Rect's position: (x, y)'''
        return (self._x, self._y)

    @property
    def dimensions(self) -> (int, int):
        '''Rect's dimensions: (width, height)'''
        return (self._width, self._height)

    @property
    def rect(self) -> (int, int, int, int):
        '''Full rect tuple'''
        return (self._x, self._y, self._width, self._height)
