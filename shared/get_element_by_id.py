'''Finging element by it's ID'''

# from components import Component


def get_element_by_id(root, element_id: str):
    '''Finging element by it's ID'''
    if root.id == element_id:
        return root

    for child in root.get_children():
        return get_element_by_id(child, element_id)

    raise ValueError(f'Component with id `{element_id}` not found')
