import json


def fetch(data, locale):
    try:
        with open(f'./charlatan/json/{locale}/{data}.json') as file:
            config = json.load(file)
    except FileNotFoundError:
        with open(f'./charlatan/json/en_GB/{data}.json') as file:
            config = json.load(file)
    return config