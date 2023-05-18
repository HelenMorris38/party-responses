import json

with open('party-responses.json', 'r', encoding='utf-8') as responses:
    read_responses = json.load(responses)
    yes_count = 0
    no_count = 0
    waiting_response = 0
    for person in read_responses:
        if person['response'] == 'yes':
            yes_count += 1
        elif person['response'] == 'no':
            no_count += 1
        else:
            waiting_response += 1
if yes_count == 1:
    print(f'{yes_count} child is able to come to the party')
else:
    print(f'{yes_count} children are able to come to the party')
if no_count == 1:
    print(f'{no_count} child is not able to come to the party')
else:
    print(f'{no_count} children are not able to come to the party')
if waiting_response == 1:
    print(f'{waiting_response} child is still to reply')
else:
    print(f'{waiting_response} children are still to reply')
