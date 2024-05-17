from ui.Event import Event
from ui.components import (
    Layout,
    Button,
    Text,
    Input,
)


def remove_item(e: Event):
    index = e.effect.callback_args['index']
    items = e.state['items']

    return {
        'items': [x for (i, x) in enumerate(items) if i != index]
    }


def add_item(e: Event):
    items = e.state['items']
    return {
        'items': items + [e.state['input_value']],
        'input_value': '',
    }


def handle_input(e: Event):
    if True:
        pass
    return {}


TODO_PAGE = {
    'title': 'RSSR Todo page',
    'focused': '',
    'state': {
        'items': [],
        'input_value': '',
    },
    'methods': {
        'remove_item': remove_item,
        'handle_add_click': add_item,
        'handle_input': handle_input,
    },
    'root': Layout(
        id='root',
        style={
            'direction': 'column',
        },
        children=[
            Layout(
                id='items_comntainer',
                model='items',
                style={
                    'size': 10,
                    'direction': 'column',
                    'gap': 4,
                    'padding': 8,
                },
                template=Layout(
                    id='item_%INDEX%',
                    style={
                        'max_h': 40,
                        'direction': 'row',
                    },
                    children=[
                        Text(
                            id='item_%INDEX%_text',
                            value='%ITEM%',
                        ),
                        Button(
                            id='item_%INDEX%_remove_button',
                            text='Remove',
                            style={ 'bg': (200, 0, 0, 255) },
                            click_callback='remove_item',
                            click_callback_args={ 'index': '%INDEX%' },
                        ),
                    ],
                ),
            ),
            Layout(
                id='form',
                style={
                    'padding': 8,
                    'gap': 8,
                    'direction': 'row',
                },
                children=[
                    Input(
                        id='todo_input',
                        model='input_value',
                        style={
                            'bg': (2, 2, 220, 255),
                            'fg': (255, 255, 255, 255),
                        },
                    ),
                    Button(
                        id='todo_add_button',
                        text='Add item',
                        style={ 'bg': (0, 200, 0, 255) },
                        click_callback='handle_add_click',
                    ),
                ]
            ),
        ],
    ),
}
