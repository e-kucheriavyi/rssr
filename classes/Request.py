from classes.Client import Client
from classes.ClientEvent import ClientEvent


class Request:
    _id = ''

    _client = None
    _event = None

    _state = None

    _meta = None

    def __init__(
        self,
        id: str,
        state: State,
        client: Client,
        event: ClientEvent,
    ):
        if not id or not isinstance(id, str):
            raise Exception(f'Invalid request id: {id}')
        self._id = id

        if not client or not isinstance(client, Client):
            raise Exception(f'Invalid request client: {client}')
        self._client = client

        if not event or not isinstance(event, ClientEvent):
            raise Exception(f'Invalid request event: {event}')
        self._event = event

        self._meta = RequestMeta()

    @property
    def id(self):
        return self._id

    @property
    def client(self):
        return self._client

    @property
    def event(self):
        return self._event

    @property
    def rects_by_id(self):
        return self._meta.rects_by_id

    def get_rect(self, id: str):
        return self._meta.get_rect(id)

    def add_rect(self, id: str, rect):
        self._rects_by_id[id] = rect
