ALIGNMENT_TYPES = ('start', 'center', 'end', 'between')


def validate_alignment(value: str):
    if value not in ALIGNMENT_TYPES:
        raise Exception('Invalid alignment type')
