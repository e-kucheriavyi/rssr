from rssr.classes import (Request, Page)



def index(request: Request):
    return Page(
        title='Index page',
        state={
            'counter': 0,
        },
        methods={
            'handle_increment_click': lambda evt: { 'counter': evt.state['counter']+1 },
            'handle_decrement_click': lambda evt: { 'counter': evt.state['counter']-1 },
        },
        root=Layout(),
    )
