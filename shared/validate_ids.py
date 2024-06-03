'''IDs validator'''


def validate_ids(root, state, ids = None):
    '''Validating that all components have IDs and that all IDs are unique'''
    if not root.id:
        raise Exception(f'Component without ID: {root.name}')

    if not ids:
        ids = [root.id]
    else:
        if root.id in ids:
            raise Exception(f'Component ID duplicate: {root.id}')
        ids.append(root.id)

    children = root.get_children(state)

    for child in children:
        validate_ids(child, state, ids)

    return True
