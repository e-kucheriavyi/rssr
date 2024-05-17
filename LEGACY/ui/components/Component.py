from ui.style import validate_style
from ui.shared import set_trbl


class Component:
    _id = ''
    _name = 'component'

    _parent = None
    _children = []

    _initial_style = {}
    _default_style = {
        'size': 1,
        'padding': 0,
        'direction': 'row',
        'gap': 0,
        'bg': 0,
        'fg': 255,
        'max_h': -1,
        'max_w': -1,
    }
    _style = {}

    _effects = []

    def __init__(
        self,
        id='',
        style=None,
        parent=None,
        children=None,
        effects=None,
    ):
        self._id = id
        self._parent = parent

        if children:
            for child in children:
                child.parent = self
            self._children = children

        if style and type(style) is dict:
            s = {**self._style, **style}
            validate_style(s)
            self._style = {**s}
            self._initial_style = {**s}

        if effects and type(effects) is list:
            self._effects = effects

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def get_children(self, state=None):
        if self._children:
            return self._children
        return []

    def set_child(self, i, child):
        return
        self._children[i] = child

    def add_child(self, child):
        child.parent = self
        self._children.append(child)

    def insert_child(self, index, child):
        child.parent = self
        self._children.insert(index, child)

    def remove_child(self, id='', index=-1):
        if id:
            self._children = [child for child in self._children if child.id != id]
            return
        if index == -1:
            return
        self._children = [child for (i, child) in enumerate(self._children) if i != index]

    @property
    def effects(self) -> list:
        return self._effects

    @property
    def initial_style(self) -> dict:
        return {**self._initial_style}

    @property
    def style(self) -> dict:
        return {**self._style}

    @style.setter
    def style(self, style):
        validate_style(style)
        self._style = {**style}

    def get_property(self, key: str):
        if key in self.style:
            return self.style[key]
        
        return self._default_style[key]

    def reset_style(self):
        self._style = {**self._initial_style}

    def get_wh(self, request, state, parent_rect, padding):
        w, h = 0, 0

        padding_top, padding_right, padding_bottom, padding_left = padding

        total_size = 0

        siblings = self._parent.get_children(state)

        for sibling in siblings:
            total_size += sibling.get_property('size')

        size_percent = self.get_property('size') / total_size

        parent_h = parent_rect['h'] - padding_bottom - padding_top
        parent_w = parent_rect['w'] - padding_left - padding_right

        direction = self._parent.get_property('direction')

        if direction == 'column':
            w = parent_w
            h = parent_h * size_percent
        elif direction == 'row':
            h = parent_h
            w = parent_w * size_percent

        max_h = self.get_property('max_h')

        if max_h != -1 and max_h < h:
            h = max_h

        max_w = self.get_property('max_w')

        if max_w != -1 and max_w < w:
            w = max_w

        return w, h

    def get_xy(self, request, state, parent_rect, padding):
        x, y = 0, 0

        padding_top, _, _, padding_left = padding

        direction = self._parent.get_property('direction')

        x = parent_rect['x'] + padding_left
        y = parent_rect['y'] + padding_top

        gap = self._parent.get_property('gap')

        siblings = self._parent.get_children(state)

        for (i, sibling) in enumerate(siblings):
            if sibling.id == self.id:
                if i == 0:
                    return x, y
                break
            sibling_rect = sibling.get_rect(request, state)
            if direction == 'column':
                y += sibling_rect['h'] + gap
            elif direction == 'row':
                x += sibling_rect['w'] + gap

        return x, y

    def get_rect(self, request, state):
        try:
            rect = request.get_rect(self.id)
            return rect
        except:
            pass

        if self._parent == None:
            rect = { 'x': 0, 'y': 0, 'w': request.width, 'h': request.height }
            request.add_rect(self.id, rect)
            return rect

        parent_rect = self._parent.get_rect(request, state)
        padding = set_trbl(self._parent.get_property('padding'))

        w, h = self.get_wh(request, state, parent_rect, padding)
        x, y = self.get_xy(request, state, parent_rect, padding)

        rect = { 'x': x, 'y': y, 'w': w, 'h': h }

        request.add_rect(self.id, rect)

        return rect

    def render(self, image):
        raise NotImplementedError()

    def instantiate(self, index, item):
        id = self._id.replace('%INDEX%', str(index))

        children = []

        for child in self.get_children():
            children.append(child.instantiate(index, item))

        instance = self.__class__(
            id=id,
            children=children,
            style=self._initial_style,
        )

        return instance

    def __str__(self):
        return f'{self._name} - {self._id}'
