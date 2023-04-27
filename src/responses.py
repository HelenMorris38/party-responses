import json

with open('party-responses.json', 'r', encoding='utf-8') as responses:
    read_responses = json.load(responses)
    yes_count = 0
    no_count = 0
    for line in read_responses['invites']:
        if line['response'] == 'yes':
            yes_count += 1
        else:
            no_count += 1
    
    print(f'{yes_count} children are able to come to the party')
    print(f'{no_count} children are not able to come to the party')