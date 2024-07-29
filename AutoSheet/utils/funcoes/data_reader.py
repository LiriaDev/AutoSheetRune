import json

def read(arquivo):
    with open(f'{arquivo}.json', 'w') as f:
        data = json.load(f)

    return data