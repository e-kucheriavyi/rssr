from ui.shared import collide_rect


class Effect:
    _name = 'effect'
    _style = {}
    _callback = ''
    _callback_args = None

    def __init__(self, style=None, callback='', callback_args=None):
        if not style:
            return
        if not type(style) is dict:
            raise Exception('Invalid event style')
        self._style = style

        self._callback = callback
        self._callback_args = callback_args

    @property
    def name(self):
        return self._name

    @property
    def callback(self):
        return self._callback

    @property
    def callback_args(self):
        return self._callback_args

    def check(self, component, rect: dict, event: dict) -> dict:
        if not component:
            raise Exception('No component to affect')
        if not event:
            raise Exception('No event')
        if not type(event['type']) is str:
            raise Exception('Invalid event type')
        if event['type'] != self._name:
            return False
        return collide_rect(event['x'], event['y'], rect)

    def affect(self, request, state, component, event: dict) -> dict:
        if self.check(component, component.get_rect(request, state), event):
            return {**component.style, **self._style}

        return {**component.style}
