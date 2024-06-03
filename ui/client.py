from rssr.shared import validate_positive_int


class Client:
    _width: int = 0
    _height: int = 0

    def __init__(self, width: int, height: int):
        validate_positive_int(width)
        validate_positive_int(height)

        self._width = width
        self._height = height

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def resolution(self) -> (int, int):
        return (self._width, self._height)
