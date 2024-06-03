from rssr.ui.ui_event import UIEvent
from rssr.ui.components import Component
from rssr.shared import get_element_by_id


class Page:
    _title = ''
    _focused = ''
    _state = None

    _methods: dict = None
    _root = None

    def __init__(self, title: str, root: Component, state: dict = None, methods: dict = None):
        if not title:
            raise ValueError('Page must have title')
        self._title = title

        if not root:
            raise ValueError(f'Page `{title}` must have root component')

        self._root = root

        self._state = {**state} if state else {}

        self._methods = methods if methods else {}

    @property
    def state(self):
        return self._state

    def set_state(self, new_state):
        self._state = {**self._state, **new_state}

    @property
    def root(self):
        return self._root

    @property
    def methods(self):
        return self._methods

    def call(self, method_name: str, event: UIEvent):
        '''Calling one of page methods and mutationg it's state'''
        method = self._methods[method_name]
        event.state = self._state
        new_state = method(event)
        self.set_state(new_state)

    @property
    def focused(self) -> str:
        '''Id of focused component'''
        return self._focused

    def focus(self, value: str):
        if not get_element_by_id(self._root, value):
            raise KeyError(f'["{self._title}" page]. Invalid focused element ID: {value}')
        self._focused = value
