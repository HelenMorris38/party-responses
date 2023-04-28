import json

with open('party-responses.json', 'r', encoding='utf-8') as responses:
    read_responses = json.load(responses)
    yes_count = 0
    no_count = 0
    waiting_response = 0
    for line in read_responses:
        print(line)
        if line['response'] == 'yes':
            yes_count += 1
        elif line['response'] == 'no':
            no_count += 1
        else:
            waiting_response += 1
    
    print(f'{yes_count} children are able to come to the party')
    print(f'{no_count} children are not able to come to the party')
    print(f'{waiting_response} children are still to reply')
