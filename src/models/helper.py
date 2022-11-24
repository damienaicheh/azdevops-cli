
from collections import namedtuple
from collections.abc import Mapping

def dic2object(mapping, name="root"):
    """
    Converts python Mapping to namedtuple recursively
    :param mapping: mapping to convert
    :param name: name to set as name of named tuple root
    :return: namedtuple with name <name> that corresponds with mapping <mapping>
    """
    if isinstance(mapping, Mapping):
        mapping = {key: dic2object(value, key) for key, value in mapping.items()}
        return namedtuple(name, mapping.keys())(**mapping)
    elif isinstance(mapping, list):
        return tuple([dic2object(item, name) for item in mapping])
    else:
        return mapping
