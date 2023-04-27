import json
from os.path import exists

def party_responses():
    responses = { "invites" : []}
    filename = 'party-responses.json'
    if not filename.exists():
        with open(filename, 'w') as f:
            json.dump(responses, f, indent=4)
    
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
            person['id'] = str(count).zfill(3)
            person['name'] = name
            person['response'] = able_to_attend
            responses['invites'].append(person)
            print('Thank you! Your response has been recorded.')
            # with open(filename, 'a') as f:
            #     responses['invites'].append(person)
            #     json.dump(responses['invites'], f, indent=4)
            # print(responses)
    




party_responses()


