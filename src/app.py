import json
from os import path

def party_responses():
    responses = []
    filename = 'party-responses.json'
    if not path.isfile(filename):
        with open(filename, 'w') as f:
            json.dump(responses, f, indent=4)
    
    with open(filename) as f:
        responses = json.load(f)
    
    count = 0
    while True:
        count += 1
        name = input('What is your name?\nEnter q at anytime to quit.\n')
        if name == 'q':
            break
        able_to_attend = input('Can you come to the party?\nPlease enter yes or no.\n')
        if able_to_attend == 'q':
            break
        else:
            person = {}
            person['name'] = name
            person['response'] = able_to_attend
            print('Thank you! Your response has been recorded.')
            responses.append(person)
            print(responses)

    with open(filename, 'w') as f:
        json.dump(responses, f, indent=4)

party_responses()


