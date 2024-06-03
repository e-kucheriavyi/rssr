'''Base component'''


class Component:
    '''Base component class'''
    _id = ''
    _name = ''

    _parent = None
    _children: list = None

    _style: dict = None
    _initial_style: dict = None
    _default_style = {}

    _effects: list = None

    def __init__(
        self,
        component_id: str,
        parent = None,
        style: dict = None,
        effects: list = None,
        children: list = None,
    ):
        raise NotImplementedError()

    def get_property(self, key: str):
        raise NotImplementedError()

    @property
    def rect(self):
        raise NotImplementedError()

    def render(self):
        raise NotImplementedError()

    def instantiate(self):
        raise NotImplementedError()
        children = []

        for child in children:
            pass

        return self.__class__(
            component_id=self._id,
            parent=self._parent,
            children=children,
        )
