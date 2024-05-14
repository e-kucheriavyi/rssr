class Request:
    id: str = ''
    page: str = ''

    width: int = 0
    height: int = 0

    event_type: str = ''
    value: str = ''
    x: int = 0
    y: int = 0

    raw: dict = None

    filename: str = ''

    _rects_by_id: dict = None

    def __init__(self, data):
        self.raw = data

        self.id = data['client']['id']
        self.page = data['client']['page']
        self.width = data['client']['w']
        self.height = data['client']['h']
        self.event_type = data['event']['type']
        if self.event_type == 'key':
            self.value = data['event']['value']
        if self.event_type in ['move', 'click']:
            self.x = data['event']['x']
            self.y = data['event']['y']

        self.filename = f'sessions/{self.id}.png'

        self._rects_by_id = {}

    @property
    def rects_by_id(self):
        return self._rects_by_id

    def get_rect(self, id):
        return self._rects_by_id[id]

    def add_rect(self, id, rect):
        self._rects_by_id[id] = rect
