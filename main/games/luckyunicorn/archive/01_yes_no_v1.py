
show_instructions = ''
while show_instructions.lower() != 'xxx':    
    # Ask the user if they have played before
    show_instructions = input('Have you played this game before? ').lower()

    # If they say yes, output 'program continues'
    # If they say no, output 'display instructions'
    # If the answer is invalid, print an error.

    if show_instructions == 'yes':
        print('program continues')

    elif show_instructions == 'y':
        print('program continues')

    elif show_instructions == 'no':
        print('display instructions')

    elif show_instructions == 'n':
        print('display instructions')

    else:
        print('Please answer yes / no')

