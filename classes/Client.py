from types import validate_positive_int


class Client:
    _width = 0
    _height = 0

    def __init__(self, width: int, height: int):
        validate_positive_int(width)
        validate_positive_int(height)

        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def resolution(self):
        return (self._width, self._height)
