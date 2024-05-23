from classs.ui_event import UIEvent
from shared import get_element_by_id


class Page:
    _title = ''
    _focused = ''
    _state = None

    _methods: dict = None
    _root = None

    def __init__(self, title: str, root, state: dict = None, methods: list = None):
        if not title:
            raise Exception('Page must have title')
        self._title = title

        if not root:
            raise Exception(f'Page "{title}" must have root component')

        self._root = root

        self._state = {**state} if state else {}

        self._methods = methods if methods else []

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
        method = self._methods[method_name]
        event.state = self._state
        new_state = method(event)
        self.set_state(new_state)

    @property
    def focused(self):
        return self._focused

    def focus(self, value: str):
        if not get_element_by_id(self._root, value):
            raise Exception(f'["{self._title}" page]. Invalid focused element ID: {value}')
        self._focused = value

    def instantiate(self):
        return self.__class__(
            title=self._title,
            state=self._state,
            root=self._root.instantiate(),
            methods=self._methods,
        )
