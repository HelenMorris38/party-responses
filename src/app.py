from src.utils import party_responses

filename = 'party-responses.json'

while True:
    name = input('What is your name?\nEnter q at anytime to quit.\n')
    if name == 'q':
        break
    if name == "":
        name = input('Please enter your name again.\n')
    able_to_attend = input('Can you come to the party?\nPlease enter yes or no.\n')
    if able_to_attend == 'q':
        break
    else:
        party_responses(name, able_to_attend, filename)
        print('Thank you! Your response has been recorded.')