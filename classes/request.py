from rssr.ui.client import Client
from rssr.ui.client_event import ClientEvent
from rssr.classes.state import State


class Request:
    _user_id = ''

    _client = None
    _event = None

    _state = None

    _meta = None

    _rects_by_id = None

    def __init__(
        self,
        user_id: str,
        state: State,
        client: Client,
        event: ClientEvent,
    ):
        if not user_id or not isinstance(user_id, str):
            raise ValueError(f'Invalid request id: {id}')
        self._user_id = user_id

        if not client or not isinstance(client, Client):
            raise ValueError(f'Invalid request client: {client}')
        self._client = client

        if not event or not isinstance(event, ClientEvent):
            raise ValueError(f'Invalid request event: {event}')
        self._event = event

        self._rects_by_id = {}

    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def client(self) -> Client:
        return self._client

    @property
    def event(self) -> ClientEvent:
        return self._event

    @property
    def rects_by_id(self):
        return self._rects_by_id

    def get_rect(self, rect_id: str):
        return self._rects_by_id[rect_id]

    def add_rect(self, rect_id: str, rect):
        self._rects_by_id[rect_id] = rect
