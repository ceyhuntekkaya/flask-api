import json


def convert_object(obj):
    fields = {}
    for field in [x for x in obj.__dict__ if not x.startswith('_') and x != 'metadata']:
        data = obj.__getattribute__(field)
        try:
            json.dumps(data)
            fields[field] = data
        except TypeError:
            fields[field] = None
    return fields
