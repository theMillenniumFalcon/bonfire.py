class Represents:
    """Handles representations for classes"""

    def __repr__(self):
        return represents(self)


def represents(obj: object) -> str:
    """
    Creates a string representing of an object.
    Args:
        obj (object): The object (class) that should be represented.
    Returns:
        str: A correct representation of the object inlcuding the object parameters.
    """
    items = [i for i in vars(obj).items() if not i[0].startswith("_")]
    return f"<{obj.__class__.__name__} {' '.join(list(map(lambda p: f'{p[0]}={p[1]}', items)))}>"