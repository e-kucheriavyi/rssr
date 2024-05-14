from ui.components.Component import Component
from ui.effects import (Click, Hover)


class Button(Component):
    _name = 'button'

    _value = ''
    _click_callback=''
    _click_callback_args=None

    def __init__(self, text='', click_callback='', click_callback_args=None, **kwargs):
        super().__init__(**kwargs)
        self._value = text

        self._click_callback = click_callback
        self._click_callback_args = click_callback_args

        if len(self._effects) == 0:
            self._effects=[
                Hover(
                    style={
                        'bg': (200, 0, 200, 255),
                    },
                ),
                Click(
                    style={
                        'bg': (0, 200, 200, 255),
                    },
                    callback=click_callback,
                    callback_args=click_callback_args,
                ),
            ]

    @property
    def model(self):
        return ''

    @property
    def value(self):
        return self._value

    def instantiate(self, index, item):
        callback_args = {**self._click_callback_args}

        for key in callback_args:
            value = callback_args[key]
            if value == '%INDEX%':
                callback_args[key] = index
        instance = self.__class__(
            id=self._id.replace('%INDEX%', str(index)),
            text=self._value,
            style=self._initial_style,
            click_callback=self._click_callback,
            click_callback_args=callback_args,
        )
        return instance
