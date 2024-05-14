from ui.components.Component import Component


class Text(Component):
    _name = 'text'

    _value = ''
    _model = ''

    def __init__(
        self,
        value=None,
        model=None,
        **kwargs,
    ):
        super().__init__(**kwargs)

        if value and model:
            raise Exception('Set either `value` or `model`')

        if value:
            self._value = value

        if model:
            self._model = model

    @property
    def model(self):
        return self._model

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def instantiate(self, index, item):
        id = self._id.replace('%INDEX%', str(index))
        value = self.value.replace('%ITEM%', item)
        instance = self.__class__(
            id=id,
            value=value,
        )

        return instance

    def __str__(self):
        return f'Text component {self._id} - {self._model} - {self._value}'
