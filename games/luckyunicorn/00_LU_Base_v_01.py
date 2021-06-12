import random
import os
from time import sleep
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
    print('\nYou may choose the amount of money you want to pay. This number should '
        'be within the range of 1 to 100. $100 is recommended for a higher chance of winning unicorns. ')
    print('There are 4 tokens of which you have a chance winning. These tokens are: '
        '\n   ◊ Donkey\n   ◊ Zebra\n   ◊ Horse\n   ◊ Unicorn (Winning Token)!')
    print('\n \nEach round you will have a chance of winning one of these, Unicorn is the only one that '
        'will make you win. Each round requires you to press the <enter> key. To exit the game, type three x\'s like "xxx"')
    return ''

def num_check(question, low, high):
    error = 'Please enter a whole number between 1 and 100\n'

    valid = False
    while not valid:
        try:
            # Ask the question
            response = int(input(question))
            # If the amount is too low / too high give
            if low < response <= high:
                return response

            # Output an error
            else:
                print(error)
        except ValueError:
            print(error)

# Main Routine goes here...
played_before = yes_no('Have you played the game before? (yes/no): ')

if played_before == 'no':
    instructions()

print('\nProgram Continues')


how_much = num_check('How much would you like to play with? (0 - 100): ', 0, 100)
print('You will be spending ${}'.format(how_much))




balance = how_much
rounds_played = 0

unicorn_count = 0
donkey_count = 0
horse_count = 0
zebra_count = 0

play_again = input('Press <Enter> to play').lower()
while play_again == '':
    # increase # of rounds played
    rounds_played += 1

    # print round number
    print('→ Round #{}'.format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # If the random # is between 1 and 5, user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = '♪ ♪ ♪ UNICORN ♪ ♪ ♪'
        unicorn_count += 1
        balance += 42.38564
    # If the random # is between 6 and 36, user gets a donkey (subtract $1 from balance
    elif 6 <= chosen_num <= 36:
        chosen = 'donkey'
        donkey_count += 1
        balance -= 12.31319
    # The token is either a horse or zebra...
    # In both cases, subtract $0.50 from the balance
    else:
        # If the number is even, set the chosen item to a horse
        if chosen_num % 2 == 0:
            chosen = 'horse'
            horse_count += 1
        # Otherwise set it to a zebra
        else:
            chosen = 'zebra'
            zebra_count += 1
        balance -= 5.53966

    print('You got a {}. Your balance is ${:.5f}'.format(chosen, balance))

    if balance < 1:
        play_again = 'xxx'
        print('Sorry you have run out of money')
    else:
        play_again = input('Press <Enter> to play again or "quit": ')

    print()


print('\n\n\n***** Here are your stats *****')

print('       ● Unicorns: {}'.format(unicorn_count))
print('       ● Donkey: {}'.format(donkey_count))
print('       ● Horses: {}'.format(horse_count))
print('       ● Zebras: {}'.format(zebra_count))


print('\nFinal balance: ${:.5f} after {} rounds'.format(balance, rounds_played))


print('Opening the main menu in 5s..... \n')
sleep(1) 
os.system('python app.py')

#last_input = ''
#while last_input != 'quit':
    #last_input = input('Type "quit" to quit the game or "run" to move into the next game: ');
    #if last_input == 'quit':
        #print('closing program')
    #elif last_input == 'run':
        #os.system('app.py 1')


