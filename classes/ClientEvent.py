from types import (
    EVENT_NAMES,
    validate_positive_int,
)


class ClientEvent:
    _name = ''
    _x = 0
    _y = 0
    _value = ''

    def __init__(
        self,
        name: str,
        x: int = 0,
        y: int = 0,
        value: str = '',
    ):
        if not name or not isinstance(name, str):
            raise ValueError(f'Event name must be `str`: {name}')

        if not name in EVENT_NAMES:
            raise ValueError(f'Invalid event name: {name}')
        self._name = name

        if name == 'key':
            if not value or not isinstance(value, str):
                raise ValueError(f'Value must be str: {value}')
            self._value = value

        validate_positive_int(x)
        validate_positive_int(y)

        self._x = x
        self._y = y

    @property
    def name(self):
        return self._name

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def position(self):
        return (self._x, self._y)

    @property
    def value(self):
        return self._value
