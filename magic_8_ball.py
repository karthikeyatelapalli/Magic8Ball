# Magic 8-ball
'''This code is a straightforward implementation of the Magic 8-ball, a well-known toy. It enables users
to ask questions, chooses a random response from a list of potential responses, and then invites them to ask
additional questions. Until the user specifies that they do not wish to answer any more questions, the while
loop in the code will continue to take user input. The responses—which might be positive, negative, or
neutral—are chosen at random from a list of 20 alternative replies. This software is a lighthearted and
entertaining approach to communicate with users and give them a little entertainment.'''

import random
# It imports the random module
def print_response(number):
    responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes - definitely.', 'You may rely on it.',
                 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
                 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.',
                 'Concentrate and ask again.', 'Don\'t count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 
                 'Very doubtful.']
    # This is the list of possible responses
    print(responses[number])

def main():
    while True:
        ask_question = input('What is your question? ')
        #  This generates a random number between 0 and 19
        response_number = random.randint(0, 19)
        # It prints the response
        print_response(response_number)
        repeat = input('Would you like to ask another question? ')
        if repeat.lower() == 'no':
            break
        # Ends the loop if person types no

main()
# This starts the program
