from ui.components import (
    Layout,
    Text,
    Button,
)
from ui.effects import (
    Hover,
    Click,
)


INDEX_PAGE = {
    'title': 'RSSR Home page',
    'focused': '',
    'state': {
        'counter': 0,
    },
    'methods': {
        'handle_decrement_click': lambda e: {
            'counter': e.state['counter'] - 1,
        },
        'handle_increment_click': lambda e: {
            'counter': e.state['counter'] + 1,
        },
    },
    'root': Layout(
        id='root',
        style={
            'padding': 4,
            'direction': 'row',
            'gap': 8,
            'bg': (33, 33, 33, 255),
        },
        children=[
            Layout(id='spacing_left'),
            Layout(
                id='wrapper',
                style={
                    'padding': 4,
                    'direction': 'column',
                    'gap': 8,
                    'bg': (33, 33, 33, 255),
                },
                children=[
                    Text(
                        id='counter_text',
                        model='counter',
                        style={
                            'size': 4,
                            'fg': (255, 255, 255, 255),
                            'bg': (0, 0, 0, 0),
                        },
                    ),
                    Layout(
                        id='buttons_row',
                        style={
                            'padding': 4,
                            'direction': 'row',
                            'gap': 8,
                            'bg': (33, 33, 33, 255),
                        },
                        children=[
                            Button(
                                id='decrement_button',
                                text='-',
                                style={
                                    'size': 1,
                                    'padding': (4, 8),
                                    'direction': 'row',
                                    'fg': (255, 255, 255, 255),
                                    'bg': (200, 0, 0, 255),
                                },
                                click_callback='handle_decrement_click',
                            ),
                            Button(
                                id='increment_button',
                                text='+',
                                style={
                                    'padding': (4, 8),
                                    'direction': 'row',
                                    'fg': (255, 255, 255, 255),
                                    'bg': (0, 200, 0, 255),
                                },
                                click_callback='handle_increment_click',
                            ),
                        ],
                    ),
                ],
            ),
            Layout(id='spacing_right'),
        ],
    ),
}
