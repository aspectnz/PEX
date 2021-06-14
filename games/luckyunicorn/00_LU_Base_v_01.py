# <<<<<<<<<<<<<<<<<<<< <<<<<<<<<< IMPORTS >>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>
import socket
h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)

from datetime import datetime
def add_log(text):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open('main.log', 'a') as file_object:
        file_object.write('\n'+dt_string+' - '+h_name+'('+IP_addres+')'+': '+text.lower())
add_log('running luckyunicorn')
import random
import os
from time import sleep
import json
import colorama

colorama.init()
colorama.init(convert=True)
colorama.init(autoreset=True)
from colorama import *


# <<<<<<<<<<<<<<<<<<<< <<<<<<<<<< FUNCTIONS >>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>
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
    print('\n\n')
    statement_generator('How to Play', '=', '')
    print('''
Choose a starting amount (minimum $1, maximum $10).
Then press <enter> to play. You will get either a horse, a zebra, a donkey, or a unicorn.

It costs $1 per round. Depending on your prize you might win some of the money back. Here's the payout amounts ...
Unicorn: $5.00 (balance increases by $4.00)
Horse: $0.50 (balance decreases by $0.50)
Zebra: $0.50 (balance decreases by $0.50)
Donkey: $0.00 (balance decreases by $1.00)
$10 is recommended for a higher chance of winning unicorns. 

Can you avoid the donkey, get the unicorns and walk home with the money?

Hint: To quit while your ahead, type "quit" instead of pressing <enter>
\n
        '''
        )
    statement_generator('Let\'s get Started', '-', '')
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

def statement_generator(statement, decoration, value3):
    if decoration == 'cube':
        decoration = '■'
        sides = decoration * 4
        statement = "{} {} {}".format(Fore.BLUE+Style.DIM+sides, Fore.WHITE+Style.BRIGHT+statement, Fore.BLUE+Style.DIM+sides)
        top_bottom = decoration * (len(statement) - 27)
        print(Back.BLUE+Style.DIM+Fore.BLUE+top_bottom)
        print(Back.BLUE+statement)
        print(Back.BLUE+Style.DIM+Fore.BLUE+top_bottom)

        return ""

    else:
        if value3 == 'roundresult':
            minus_num = 25
        else:
            minus_num = 15

        sides = decoration * 3
        statement = "{} {} {}".format(Fore.BLACK+sides, Fore.WHITE+statement, Fore.BLACK+sides)
        top_bottom = decoration * (len(statement) - minus_num)

        print(Fore.BLACK+top_bottom)
        print(statement)
        print(Fore.BLACK+top_bottom)

        return ""

# <<<<<<<<<<<<<<<<<<<< <<<<<<<<<< SCRIPT >>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>

print('\n')
statement_generator('Welcome to the Lucky Unicorn Game', 'cube', '')

played_before = yes_no('Have you played the game before? (yes/no): ')

if played_before == 'no':
    instructions()

how_much = num_check('How much would you like to play with? (1 - 10): ', 0, 10)
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
    chosen_type = '*'
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
        chosen_type = 'U'
    # If the random # is between 6 and 36, user gets a donkey (subtract $1 from balance
    elif 6 <= chosen_num <= 36:
        chosen = 'donkey'
        donkey_count += 1
        balance -= 1
        chosen_type = 'D'
    # The token is either a horse or zebra...
    # In both cases, subtract $0.50 from the balance
    else:
        # If the number is even, set the chosen item to a horse
        if chosen_num % 2 == 0:
            chosen = 'horse'
            horse_count += 1
            chosen_type = 'H'
        # Otherwise set it to a zebra
        else:
            chosen = 'zebra'
            zebra_count += 1
            chosen_type = 'Z'
        balance -= 0.5

    round_result = Fore.GREEN+'You got a {}. Your in game balance is '.format(chosen)+Fore.RED+'${}'.format(balance)
    statement_generator(round_result, chosen_type, 'roundresult')

    if balance < 1:
        play_again = 'xxx'
        print('Sorry you have run out of money')
    else:
        print(Fore.YELLOW+'Press <Enter> to play again or "quit": ', end='')
        play_again = input()

    print()

print(Fore.BLUE+'\n\n\nHere are your stats')
print('''
       ● Unicorns: {}
       ● Donkey: {}
       ● Horses: {}
       ● Zebras: {}

'''.format(unicorn_count, donkey_count, horse_count, zebra_count))

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


print('Opening the main menu... \n')
#sleep(1)
os.system('python app.py')


