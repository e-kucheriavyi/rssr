def collide_rect(x, y, rect):
    if x < rect['x'] or x > rect['x'] + rect['w']:
        return False
    if y < rect['y'] or y > rect['y'] + rect['h']:
        return False
    return True
