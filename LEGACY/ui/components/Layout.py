from ui.components.Component import Component


class Layout(Component):
    _name = 'layout'

    _style = {
        'size': 1,
        'direction': 'column',
        'alignment': 'center',
    }

    _template = None
    _model = ''

    def __init__(self, model='', template=None, children=None, **kwargs):
        super().__init__(children=children, **kwargs)

        self._model = model
        self._template = template

        if model and not template or (not model and template):
            raise Exception(
                f'Layout "{self.id}" error: if you set model you have to set template and vise versa'
            )

        if model and template and children:
            raise Exception(
                f'Layout "{self.id}" error: you can either set children or model and template'
            )

    @property
    def template(self):
        return self._template

    @property
    def model(self):
        return self._model

    def get_children(self, state=None):
        if self._children:
            return self._children

        if not self.model or not state:
            return []

        items = state['state'][self.model]

        children = []

        for (i, item) in enumerate(items):
            child = self.template.instantiate(i, item)
            child.parent = self
            children.append(child)

        return children

