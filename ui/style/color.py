'''Color class'''

from rssr.shared import validate_positive_int


class Color:
    '''RGBA color used for fonts and backgrounds'''
    _r: int = 0
    _g: int = 0
    _b: int = 0
    _a: int = 0

    def __init__(self, r: int=0, g: int=0, b: int=0, a: int=255):
        Color.validate('r', r)
        Color.validate('g', g)
        Color.validate('b', b)
        Color.validate('a', a)

        self._r = r
        self._g = g
        self._b = b
        self._a = a

    @staticmethod
    def validate(key: str, value: int) -> bool:
        '''Validating channels'''
        validate_positive_int(value)
        if value > 255:
            raise ValueError(f'Color error. `{key}` must be lower than 255. Got {value}')
        return True

    @property
    def r(self) -> int:
        '''Redd channel'''
        return self._r

    @property
    def g(self) -> int:
        '''Green channel'''
        return self._g

    @property
    def b(self) -> int:
        '''Blue channel'''
        return self._b

    @property
    def a(self) -> int:
        '''Alpha channel'''
        return self._a

    @property
    def value(self) -> (int, int, int, int):
        '''Returning rgba values'''
        return (self._r, self._g, self._b, self._a)

    @property
    def normalized_value(self) -> (int, int, int, int):
        '''Returning normalized rgba values. 255 -> 1'''
        return (self._r / 255, self._g / 255, self._b / 255, self._a / 255)

    def copy(self):
        '''Creating full copy of an object'''
        return self.__class__(*self.value)
