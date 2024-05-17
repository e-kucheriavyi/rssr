class State:
    _page: str = ''
    _rects_by_id = None

    def __init__(self, page: str):
        self._rects_by_id = {}

    @property
    def rects_by_id(self):
        return self._rects_by_id

    def get_rect(self, id):
        return self._rects_by_id[id]

    def add_rect(self, id, rect):
        self._rects_by_id[id] = rect
