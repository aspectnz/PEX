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

def instructions():
    print('**** How to Play ****')
    print('\nThe rules of the game go here')
    return ''

# Main Routine goes here...
played_before = yes_no('Have you played the game before? ')

if played_before == 'no':
    instructions()

print('\nProgram Continues')