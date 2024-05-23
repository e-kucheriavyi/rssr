class Color:
    _r = 0
    _g = 0
    _b = 0
    _a = 0

    def __init__(self, r=0, g=0, b=0, a=255):
        Color.validate('r', r)
        Color.validate('g', g)
        Color.validate('b', b)
        Color.validate('a', a)

        self._r = r
        self._g = g
        self._b = b
        self._a = a

    @staticmethod
    def validate(key: str, value: int):
        validate_positive_int(value)
        if value > 255:
            raise ValueError(f'Color error. `{key}` must be lower than 255')

    @property
    def r(self):
        return self._r

    @property
    def g(self):
        return self._g

    @property
    def b(self):
        return self._b

    @property
    def a(self):
        return self._a

    @property
    def value(self):
        return (self._r, self._g, self._b, self._a)

    @property
    def normalized_value(self):
        return (self._r / 255, self._g / 255, self._b / 255, self._a / 255)
