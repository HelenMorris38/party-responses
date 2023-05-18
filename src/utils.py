import json
from os import path

def create_json_file(filename):
    """Creates a JSON file with an empty list"""
    data = []
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def write_to_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def get_json_data(filename):
    with open(filename) as f:
        responses = json.load(f)
    return responses



def party_responses(name, response, filename):
    """This function takes two strings, adds them to a dictionary with the keys of name and response, then appends this dictionary to a list.
    The list of dictionaries is saved in a JSON file.
    Args:
        - name (string)
        - response (string)
    """
    if not path.isfile(filename):
        write_to_json(filename, [])
    
    responses = get_json_data(filename)
    person = {}
    person['id'] = str(len(responses) + 1).zfill(3)
    person['name'] = name.title()
    person['response'] = response
    responses.append(person)

    write_to_json(filename, responses)

def update_response(id, updated_response, filename):
    responses = get_json_data(filename)
    for person in responses:
        print(person)
        if id == person['id']:
            person['response'] = updated_response
    write_to_json(filename, responses)