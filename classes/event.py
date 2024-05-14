from ui.effects import Effect
from ui.components import Component


class Event:
    _state: dict = None
    _effect: Effect = None
    _target: Component = None

    def __init__(self, state, effect, target):
        self._state = state
        self._effect = effect
        self._target = target

    @property
    def state(self):
        return self._state

    @property
    def effect(self):
        return self._effect

    @property
    def target(self):
        return self._target