def remove_id(json):
    remove_key(json, 'id')


def remove_key(json, key, converter=None):
    value = json.get(key)
    if value is not None:
        del json[key]
        if converter:
            value = converter(value)
        return value
