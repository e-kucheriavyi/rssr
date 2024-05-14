from ui.components.Component import Component
from ui.effects import Focus


class Input(Component):
    _name = 'input'
    _model = ''

    def __init__(self, model='', **kwargs):
        super().__init__(**kwargs)
        self._model = model

        if not self._effects:
            self._effects = [
                Focus(
                    style={
                        'bg': (200, 200, 200, 255),
                    },
                ),
            ]

    @property
    def model(self):
        return self._model
