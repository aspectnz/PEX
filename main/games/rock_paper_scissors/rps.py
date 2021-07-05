import random

# Functions go here
def check_rounds():
    while True:
        response = input('How many rounds: ')

        round_error = 'Please type either <enter> or an integer that is more than 0'

        # If infinite mode not chosen, check response is an integer that is more than 0
        if response != '':
            try:
                response = int(response)

                # If response is too low, go back to start of loop
                if response < 1:
                    print(round_error)
                    continue
            # If response is not an integer, go back to start of loop
            except ValueError:
                print(round_error)
                continue

        return response

def choice_checker(question, valid_list, error):
    valid = False
    while not valid:
        # Ask use for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterate through list and if response is an item in the list (or the first letter of an item), the full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return response

        # output error if item is not list
        if response == 'r' or response == 'rock':
            return response
        elif response == 'p' or response == 'paper':
            return response
        elif response == 's' or response == 'scissors':
            return response

        elif response == 'quit':
            return response
        else:
            print(error)

# Main routine goes here

# List of valid responses
yes_no_list = ['yes', 'no']
rps_list = ['rock', 'paper', 'scissors', 'quit']

# Ask user if they have played before.
# If 'yes', show the instructions


# ask user for # of rounds, then loop...
rounds_played = 0
choose_instruction = 'Please choose rock (r), paper (p) or scissors (s)'

# Ask user for # of rounds, <enter? for infinite mode
rounds = check_rounds()

end_game = 'no'
while end_game == 'no':

    # Rounds Heading
    print()
    rounds_played += 1
    if rounds == '':
        heading = 'Continuous Mode: Round '+rounds_played

    else:
        heading = 'Round {} of {}'.format(rounds_played, rounds)

    print(heading)
    choose = input('{} or "quit" to end: '.format(choose_instruction))
    
    # End game if exit code is typed
    if choose == 'quit':
            break

# Ask user if they want to see their game history
#if yes, show the game history

# Show game statistics