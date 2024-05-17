class Rect:
    _x = 0
    _y = 0
    _width = 0
    _height = 0

    def __init__(self, x: int, y: int, width: int, height: int):
        validate_positive_int(x)
        validate_positive_int(y)
        validate_positive_int(width)
        validate_positive_int(height)

        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def collide(self, x: int, y: int):
        validate_positive_int(x)
        validate_positive_int(y)

        if x < self._x or x > self._x + self._width:
            return False
        if y < self._y or y > self._y + self._height:
            return False
        return True

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def position(self):
        return (self._x, self._y)

    @property
    def dimensions(self):
        return (self._width, self._height)

    @property
    def rect(self):
        return (self._x, self._y, self._width, self._height)
