import json

from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from ui.controller import update_state
from ui.renderer import render_response
from classes import Request, Response

from pages import PAGES


app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

html = '''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8"/>
	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
	<title>%TITLE%</title>
	<style>body,.root{width:100%;height:100%;overflow:hidden;padding:0;margin:0;background:#333;}</style>
</head>
<body>
	<canvas class="root" id="root"></canvas>
	<script src="/static/main.js"></script>
</body>
</html>
'''


USER_STATES = {}


def set_parent(component, parent=None):
    component.parent = parent

    children = component.get_children()

    for child in children:
        set_parent(child, component)


def get_user_state(id: str, page: str) -> dict:
    if id not in USER_STATES:
        USER_STATES[id] = {'page': page, **PAGES[page]}

    state = USER_STATES[id]

    if state['page'] != page:
        state = {'page': page, **PAGES[page]}
        USER_STATES[id] = state

    set_parent(state['root'], None)

    return state


def set_user_state(id: str, state: str):
    USER_STATES[id] = state


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
        request = Request(json.loads(d))

        state = get_user_state(request.id, request.page)
        new_state = update_state(request, state)
        image = render_response(request, new_state)

        response = Response(image, 0, 0)
        set_user_state(request.id, new_state)

        if not response:
            continue

        await ws.send_json(response.to_dict())
