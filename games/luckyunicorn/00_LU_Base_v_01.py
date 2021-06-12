import random
import os
from time import sleep
import json
import colorama

colorama.init()
colorama.init(convert=True)
colorama.init(autoreset=True)
from colorama import *


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
    print('''
        **** How to Play ****
        \nYou may choose the amount of money you want to pay. This number should '
        'be within the range of 1 to 10. $10 is recommended for a higher chance of winning unicorns. 
        There are 4 tokens of which you have a chance winning. These tokens are:
        '\n   ◊ Donkey\n   ◊ Zebra\n   ◊ Horse\n   ◊ Unicorn (Winning Token)!
        \n \nEach round you will have a chance of winning one of these, Unicorn is the only one that '
        'will make you win. Each round requires you to press the <enter> key. To exit the game, type three x\'s like "xxx"
        '''
        )
    return ''

def num_check(question, low, high):
    error = 'Please enter a whole number between 1 and 10\n'

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


how_much = num_check('How much would you like to play with? (0 - 10): ', 0, 10)
with open('config.json', 'r') as jsonConfig:
    config = json.load(jsonConfig)

config['balance'] -= how_much

with open('config.json', 'w') as f:
    json.dump(config, f)
print('You will be spending ${}'.format(how_much))
print('Deducting ${} off balance.'.format(how_much))




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
    print(Fore.BLUE+'→ Round #{}'.format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # If the random # is between 1 and 5, user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = '♪ UNICORN ♪'
        unicorn_count += 1
        balance += 4
    # If the random # is between 6 and 36, user gets a donkey (subtract $1 from balance
    elif 6 <= chosen_num <= 36:
        chosen = 'donkey'
        donkey_count += 1
        balance -= 1
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
        balance -= 0.5

    print(Fore.GREEN+'You got a {}. Your in game balance is '.format(chosen)+Fore.RED+'${}'.format(balance))

    if balance < 1:
        play_again = 'xxx'
        print('Sorry you have run out of money')
    else:
        print(Fore.BLACK+'Press <Enter> to play again or "quit": ', end='')
        play_again = input()

    print()


print('\n\n\n***** Here are your stats *****')

print('       ● Unicorns: {}'.format(unicorn_count))
print('       ● Donkey: {}'.format(donkey_count))
print('       ● Horses: {}'.format(horse_count))
print('       ● Zebras: {}'.format(zebra_count))

made_or_lost = balance - how_much
if made_or_lost > 0:
    change_msg = 'won'
    change_msg_color = Fore.GREEN
else:
    change_msg = 'lost'
    change_msg_color = Fore.RED
    made_or_lost = made_or_lost * -1

print(change_msg_color+'\nYou have '+change_msg+': ${} after {} rounds'.format(made_or_lost, rounds_played))

with open('config.json', 'r') as jsonConfig:
    config = json.load(jsonConfig)

new_balance = config['balance'] + balance

config['balance'] = new_balance

with open('config.json', 'w') as f:
    json.dump(config, f)


print('Opening the main menu in 5s..... \n')
sleep(1) 
os.system('python app.py')


