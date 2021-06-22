import random

# Functions go here

# Main routine goes here

# List of valid responses
yes_no_list = ['yes', 'no']
rps_list = ['rock', 'paper', 'scissors', 'quit']

# Ask user if they have played before.
# If 'yes', show the instructions
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





# Loop for testing purposes
user_choice = ''
while user_choice != 'quit':
    # Ask user for choice and check it's valid
    user_choice = choice_checker('Choose rock/paper/scissors (r/p/s): ', rps_list, 'Please choose from rock/paper/scissors or type "quit" to quit')
    # print out choice for comparison purposes
    print('You chose '+user_choice)