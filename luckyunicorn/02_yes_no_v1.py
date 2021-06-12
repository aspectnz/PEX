# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            response = 'yes'
            return response

        elif response == 'no' or response == 'n':
            response = 'no'
            return response

        else:
            print('Please answer yes / no')


# Main Routine goes here...
show_instructions = yes_no('Have you played the game before? ')
print('You chose {}'.format(show_instructions))

