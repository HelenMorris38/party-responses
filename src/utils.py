import json
from os import path

def party_responses(name, response):
    """This function takes two strings, adds them to a dictionary with the keys of name and response, then appends this dictionary to a list.
    The list of dictionaries is saved in a JSON file.
    Args:
        name (string)
        response (string)
    """
    responses = []
    filename = 'party-responses.json'
    if not path.isfile(filename):
        with open(filename, 'w') as f:
            json.dump(responses, f, indent=4)
    
    with open(filename) as f:
        responses = json.load(f)
        person = {}
        person['name'] = name.title()
        person['response'] = response
        responses.append(person)

    with open(filename, 'w') as f:
        json.dump(responses, f, indent=4)