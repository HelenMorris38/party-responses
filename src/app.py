from src.utils import party_responses, update_response

filename = 'party-responses.json'
welcome_question = input('Hello! Please press "y" if you would like to respond to a party invitation or "u" if you would like to update a previously submitted response.\nEnter q at anytime to quit.\n')

while True:
    if welcome_question == 'y':
        name = input('What is your name?\nEnter q at anytime to quit.\n')
        if name == 'q':
            break
        if name == "":
            name = input('Please enter your name again.\n')
        able_to_attend = input('Can you come to the party?\nPlease enter yes or no.\n')
        if able_to_attend == 'q':
            break
        else:
            id = party_responses(name, able_to_attend, filename)
            print(f'Thank you! Your response has been recorded. Please make a note of your id number in case you would like to update your response later. Your id number is {id}')
    if welcome_question == 'u':
        id = input('Please enter your id number:\n')
        if id == 'q':
            break
        updated_response = input('Can you come to the party?\nPlease enter yes or no.\n')
        if updated_response == 'q':
            break
        else:
            update_response(id, updated_response, filename)
            print(f'Thank you. Your response has been updated.\n')
            break

        
