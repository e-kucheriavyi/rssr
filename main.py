'''Entry point for RSSR-app'''

import json

from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

# from rssr.ui.controller import update_state
# from rssr.ui.renderer import render_response
# from rssr.classes import Request, Response

from rssr.classes import (Request, Response, State)
from rssr.ui import (Client, ClientEvent)
from rssr.pages import PAGES
from rssr.templates import HTML


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')

USER_STATES = []


def get_state(user_id: str, page_slug: str):
    '''Getting or creating user's state'''
    for s in USER_STATES:
        if s.user_id == user_id:
            return s

    state = State(user_id=user_id, page=page_slug)

    USER_STATES.append(state)

    return state


def prepare_page(slug: str):
    '''Preparing page's HTML-template'''
    if not slug in PAGES:
        return '404'

    p = PAGES[slug]

    template = HTML.replace('%TITLE%', p['title'])
    return HTMLResponse(template)


@app.get('/')
async def home():
    '''Serving HTML-template'''
    return prepare_page('/')


@app.get('/{slug}')
async def page(slug: str):
    '''Serving HTML-template by slug'''
    return prepare_page(f'/{slug}')


@app.websocket('/ws')
async def websocket_endpoint(ws: WebSocket):
    '''Communicating with client via websockets'''
    await ws.accept()

    while True:
        d = await ws.receive_text()
        data = json.loads(d)

        client = Client(
            width=data['client']['w'],
            height=data['client']['h'],
        )
        event = ClientEvent(
            name=data['event']['type'],
            x=data['event']['x'],
            y=data['event']['y'],
            value=data['event']['value'],
        )
        state = State() # TODO
        request = Request(
            user_id=data['client']['id'],
            client=client,
            event=event,
            state=state,
        )

        new_state = update_state(request, state) # TODO
        image = render_response(request, new_state) # TODO

        response = Response(image, 0, 0) # TODO
        set_user_state(request.user_id, new_state) # TODO

        if not response:
            continue

        await ws.send_json(response.to_dict())
