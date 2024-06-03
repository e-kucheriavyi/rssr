from .effects import Effect
from .components import Component


class UIEvent:
    _state: dict = None
    _effect: Effect = None
    _target: Component = None

    def __init__(self, effect, target):
        self._state = state
        self._effect = effect
        self._target = target

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value: dict):
        self._state = {**value}

    @property
    def effect(self):
        return self._effect

    @property
    def target(self):
        return self._target
