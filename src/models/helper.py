
from collections import namedtuple
from collections.abc import Mapping

def remove_invalid_variables(item):
    return item.startswith('_') or item.startswith('$') or '.' in item

def dic2object(mapping, name="root"):
    """
    Converts python Mapping to namedtuple recursively
    :param mapping: mapping to convert
    :param name: name to set as name of named tuple root
    :return: namedtuple with name <name> that corresponds with mapping <mapping>
    """
    if isinstance(mapping, Mapping):
        keys_filtered = list(filter(remove_invalid_variables, mapping.keys()))
        for item in keys_filtered:
            del mapping[item]
        mapping = {key: dic2object(value, key) for key, value in mapping.items()}
        return namedtuple(name, mapping.keys())(**mapping)
    elif isinstance(mapping, list):
        return tuple([dic2object(item, name) for item in mapping])
    else:
        return mapping
