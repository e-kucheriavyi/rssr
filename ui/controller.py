from classes import (Request, Response, Event)
from ui.shared import collide_rect


def check_component_effects(request, state, component):
    component.style = component.initial_style
    rect = component.get_rect(request, state)
    evt = {
        'type': request.event_type,
        'x': request.x,
        'y': request.y,
        'value': request.value,
    }

    if evt['type'] == 'click' and collide_rect(evt['x'], evt['y'], rect):
        state['focused'] = component.id

    if evt['type'] == 'key' and component.name == 'input' and state['focused'] == component.id:
        new_state = { **state['state'] }

        if component.model in new_state:
            new_state[component.model] = new_state[component.model] + evt['value']
            state['state'] = new_state

    for effect in component.effects:
        if request.event_type != effect.name:
            continue
        if not effect.check(component, rect, evt):
            continue
        style = effect.affect(request, state, component, evt)
        component.style = style
        if effect.name == 'click' and effect.callback:
            callback = state['methods'][effect.callback]
            e = Event(
                state=state['state'],
                effect=effect,
                target=component,
            )
            state['state'] = {**state['state'], **callback(e)}

    children = component.get_children(state)

    for (i, child) in enumerate(children):
        updated_child = check_component_effects(request, state, child)
        component.set_child(i, updated_child)

    return component


def update_state(request: Request, state: dict):
    root = state['root']
    new_root = check_component_effects(request, state, root)

    return state


def prepare_response(request: Request, state: dict):
    return None
