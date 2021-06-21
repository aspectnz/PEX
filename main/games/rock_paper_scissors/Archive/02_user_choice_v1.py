# Functions go here
def choice_checker(question):
    valid = False
    while not valid:
        # Ask user for choice
        response = input(question).lower()
        if response == 'r' or response == 'rock':
            return response


# Main routine goes here

# Ask user for choice and check it's valid
user_choice = choice_checker('Choose rock/paper/scissors (r/p/s): ')



# print out choice for comparison purposes