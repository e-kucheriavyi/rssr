import json

from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

# from ui.controller import update_state
# from ui.renderer import render_response
# from classes import Request, Response

from pages import PAGES

from templates import html


def prepare_page(slug: str):
    if not slug in PAGES:
        return '404'

    p = PAGES[slug]

    template = html.replace('%TITLE%', p['title'])
    return HTMLResponse(template)


@app.get('/')
async def home():
    return prepare_page('/')


@app.get('/{slug}')
async def page(slug: str):
    return prepare_page(f'/{slug}')


@app.websocket('/ws')
async def websocket_endpoint(ws: WebSocket):
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
            id=data['client']['id'],
            client=client,
            event=event,
            state=state,
        )

        new_state = update_state(request, state) # TODO
        image = render_response(request, new_state) # TODO

        response = Response(image, 0, 0) # TODO
        set_user_state(request.id, new_state) # TODO

        if not response:
            continue

        await ws.send_json(response.to_dict())
