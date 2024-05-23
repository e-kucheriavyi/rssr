import pixie
from math import ceil

from ui.shared import set_color


def create_image(w, h):
    return pixie.Image(w, h)


def normalize_color(color: tuple) -> tuple:
    return (color[0] / 255, color[1] / 255, color[2] / 255, color[3] / 255)


def draw_rect(image, x, y, w, h, color):
    paint = pixie.Paint(pixie.SOLID_PAINT)
    r, g, b, a = color
    paint.color = pixie.Color(r, g, b, a)

    ctx = image.new_context()
    ctx.fill_style = paint

    ctx.fill_rect(x, y, w, h)
    return image


def render_text(request, state, image, component, h_align=pixie.CENTER_ALIGN, v_align=pixie.CENTER_ALIGN):
    font = pixie.read_font('static/Roboto-Medium.ttf')
    font.size = 20

    if component.model:
        text = str(state['state'][component.model])
    else:
        text = component.value

    rect = component.get_rect(request, state)

    image = image.fill_text(
        font,
        text,
        transform = pixie.translate(rect['x'], rect['y']),
        bounds=pixie.Vector2(rect['w'], rect['h']),
        v_align=v_align,
        h_align=h_align,
    )
    return image


def render_component(request, state, image, component):
    rect = component.get_rect(request, state)

    if 'bg' not in component.style:
        color = (255, 255, 255, 255)
    else:
        color = set_color(component.get_property('bg'))

    normalized_color = normalize_color(color)

    image = draw_rect(image, rect['x'], rect['y'], rect['w'], rect['h'], normalized_color)

    if component.name in ['text', 'button', 'input']:
        h_align = pixie.LEFT_ALIGN if component.name == 'input' else pixie.CENTER_ALIGN
        render_text(request, state, image, component, h_align=h_align)

    children = component.get_children(state)

    for child in children:
        image = render_component(request, state, image, child)

    return image


def render_response(request, state: dict):
    image = create_image(request.width, request.height)

    root = state['root']

    image = render_component(request, state, image, root)

    image.write_file(request.filename)

    with open(request.filename, 'rb') as file:
        b = file.read()

    return b
