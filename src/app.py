import json

def party_responses():
    responses = []
    filename = 'party-responses.json'
    with open(filename, 'w') as f:
        json.dump(responses, f)

    count = 0
    while True:
        count += 1
        name = input('What is your name?\nEnter q at anytime to quit.\n')
        if name == 'q':
            break
        response = input('Can you come to the party?\nPlease enter yes or no.\n')
        if response == 'q':
            break
        else:
            person = {}
            person['id'] = str(count).zfill(3)
            person['name'] = name
            person['response'] = response
            print('Thank you! Your response has been recorded.')
            with open(filename, 'w') as f:
                responses.append(person)
                json.dump(responses, f, indent=4)
            print(responses)

party_responses()


