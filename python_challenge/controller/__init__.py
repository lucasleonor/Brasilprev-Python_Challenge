def remove_id(json):
    if json.get('id') is not None:
        del json['id']
