from components import Component


def get_element_by_id(root: Component, id: str):
    if root.id == id:
        return root

    for child in root.get_children():
        return get_element_by_id(child, id)

    return None
