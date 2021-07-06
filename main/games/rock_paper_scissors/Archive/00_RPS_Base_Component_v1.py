import random

# Functions go here

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

def check_rounds():
    while True:
        response = input('How many rounds: ')

        round_error = 'Please type either <enter> or an integer that is more than 0\n'

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



# Main routine goes here

# List of valid responses
yes_no_list = ['yes', 'no']
rps_list = ['rock', 'paper', 'scissors', 'quit']

# Ask user if they have played before.
# If 'yes', show the instructions


# ask user for # of rounds, then loop...
 
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

choose_instruction = 'Choose rock/paper/scissors (r/p/s)'
# Ask user for # of rounds, <enter? for infinite mode
rounds = check_rounds()
end_game = 'no'
while end_game == 'no':
    # Rounds Heading
    print()
    if rounds == '':
        heading = 'Continuous Mode: Round '+rounds_played+1
    else:
        heading = f'Round {rounds_played+1} of {rounds}'
    print(heading)

    # Ask user for choice and check it's valid
    choose_error = 'Please choose from rock/paper/scissors or type "quit" to quit'
    choose = choice_checker(choose_instruction, rps_list, choose_error)

    # End game if exit code is typed
    if choose == 'quit':
        break


    # ***** rest of loop / game *****

    comp_choice = random.choice(rps_list[:-1])
    print(comp_choice)

    # Compare choices
    if comp_choice == user_choice:
        result = 'tie'
        rounds_drawn += 1
    elif user_choice == 'rock' and comp_choice == 'scissors':
        result = 'won'
    elif user_choice == 'paper' and comp_choice == 'rock':
        result = 'won'
    elif user_choice == 'scissors' and comp_choice == 'paper':
        result = 'won'
    else:
        result = 'lost'
        rounds_lost += 1

    if result == 'tie':
        feedback = 'It\'s a tie'
    else:
        feedback = f'{user_choice} vs {comp_choice} - you. {result}'

    print(f'You chose {user_choice}, the computer chose {comp_choice} \nResult: {result}')

    rounds_played += 1
    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break



# Ask user if they want to see their game history

#if yes, show the game history

# Show game statistics




# get computer choice
# compare choices
# End game if exit code is typed