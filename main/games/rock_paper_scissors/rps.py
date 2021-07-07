import random
import os
import sys
from time import sleep

# Import colorama module
# If the module is not installed, then automatically install it. Otherwise, continue the program
try:
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()
    colorama.init(convert=True)
    colorama.init(autoreset=True)
    colorama_imported = True
except:
    pip.main(['install', 'colorama'])
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()
    colorama.init(convert=True)
    colorama.init(autoreset=True)
    colorama_imported = True

# Functions go here
# List of valid responses
yes_no_list = ['yes', 'no']
rps_list = ['rock', 'paper', 'scissors', 'quit']

def check_rounds():
    while True:
        response = input('How many rounds would you like to play or <enter> for infinite mode: ')

        round_error = 'Please type either <enter> or an integer that is more than 0\n'

        if response[0:4] == 'auto':
            number_of_rounds = int(response[5:len(response)])
            response = number_of_rounds
            print(Fore.BLUE+f'You will be playing {number_of_rounds} rounds ')

            rounds_played = 0
            rounds_lost = 0
            rounds_drawn = 0

            for item in range (0, number_of_rounds):
                choose = random.choice(rps_list[:-1])
                comp_choice = random.choice(rps_list[:-1])

                 # Compare choices
                if comp_choice == choose:
                    result = Fore.WHITE+'tie'
                    rounds_drawn += 1
                elif choose == 'rock' and comp_choice == 'scissors':
                    result = Fore.GREEN+'won'
                elif choose == 'paper' and comp_choice == 'rock':
                    result = Fore.GREEN+'won'
                elif choose == 'scissors' and comp_choice == 'paper':
                    result = Fore.GREEN+'won'
                else:
                    result = Fore.RED+'lost'
                    rounds_lost += 1

                if result == 'tie':
                    feedback = 'It\'s a tie'
                else:
                    feedback = f'{choose} vs {comp_choice} - you. {result}'

                if number_of_rounds == '':
                    heading = Fore.BLUE+f'Continuous Mode: Round {rounds_played+1}'
                else:
                    heading = Fore.BLUE+f'Round {rounds_played+1} of {number_of_rounds}'
                print(heading)

                print(Fore.WHITE+f'You chose {choose}, the computer chose {comp_choice} \nResult: {result}')
                rounds_played += 1

            sleep(1)
            # stats
            summary_prompt = input('Would you like to see your end results? (y/n): ')
            if summary_prompt == 'y' or summary_prompt == 'yes':
                rounds_won = rounds_played - rounds_lost - rounds_drawn
                percent_win = rounds_won / rounds_played * 100
                percent_lose = rounds_lost / rounds_played * 100
                percent_tie = rounds_drawn / rounds_played * 100

                # Find which number is most dominant
                if percent_win > percent_lose and percent_win > percent_tie:
                    dominant = Fore.GREEN+'win'
                elif percent_lose > percent_win and percent_lose > percent_tie:
                    dominant = Fore.RED+'lose'
                else:
                    dominant = 'tie'

                print(f'''
    Rounds Played: {rounds_played}
    {Fore.GREEN}Won: {percent_win:.2f}%
    {Fore.RED}Lost: {percent_lose:.2f}%
    {Fore.WHITE}Tied: {percent_tie:.2f}%
    According to the stats, you mostly {dominant}.
                ''')

            # Ask the user if they would like to play again
            play_again = input('Would you like to play again? (y/n): ')
            if play_again == 'y' or play_again == 'yes':
                os.system('python main/games/rock_paper_scissors/rps.py')

            exit()

        # If infinite mode not chosen, check response is an integer that is more than 0
        elif response != '':
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
        print(question, end="")

        response = input().lower()

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
        elif response == 'quit' or response == 'q':
            return response
        else:
            print(error)


# Main routine goes here

# Ask user if they have played before.
# If 'yes', show the instructions


# ask user for # of rounds, then loop...

choose_instruction = Fore.CYAN+'Choose rock/paper/scissors (r/p/s): '

# Ask user for # of rounds, <enter> for infinite mode
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

choose = ''
rounds = check_rounds()
while choose != 'quit':
    # Rounds Heading
    print()
    if rounds == '':
        heading = Fore.BLUE+f'Continuous Mode: Round {rounds_played+1}'
    else:
        heading = Fore.BLUE+f'Round {rounds_played+1} of {rounds}'
    print(heading)

    # Ask user for choice and check it's valid
    choose_error = 'Please choose from rock/paper/scissors or type "quit" to quit\n'
    
    choose = choice_checker(choose_instruction,rps_list,choose_error)
    # End game if exit code is typed
    if choose == 'quit':
        break


    # ***** rest of loop / game *****

    comp_choice = random.choice(rps_list[:-1])

    if choose == 'r':
        choose = 'rock'
    elif choose == 'p':
        choose = 'paper'
    elif choose == 's':
        choose = 'scissors'

    # Compare choices
    if comp_choice == choose:
        result = Fore.WHITE+'tie'
        rounds_drawn += 1
    elif choose == 'rock' and comp_choice == 'scissors':
        result = Fore.GREEN+'won'
    elif choose == 'paper' and comp_choice == 'rock':
        result = Fore.GREEN+'won'
    elif choose == 'scissors' and comp_choice == 'paper':
        result = Fore.GREEN+'won'
    else:
        result = Fore.RED+'lost'
        rounds_lost += 1

    if result == 'tie':
        feedback = 'It\'s a tie'
    else:
        feedback = f'{choose} vs {comp_choice} - you. {result}'

    print(Fore.WHITE+f'You chose {choose}, the computer chose {comp_choice} \nResult: {result}')

    rounds_played += 1
    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break



# Ask user if they want to see their game history

#if yes, show the game history

summary_prompt = input('Would you like to see your end results? (y/n): ')
if summary_prompt == 'y' or summary_prompt == 'yes':
    rounds_won = rounds_played - rounds_lost - rounds_drawn
    percent_win = rounds_won / rounds_played * 100
    percent_lose = rounds_lost / rounds_played * 100
    percent_tie = rounds_drawn / rounds_played * 100

    # Find which number is most dominant
    if percent_win > percent_lose and percent_win > percent_tie:
        dominant = Fore.GREEN+'win'
    elif percent_lose > percent_win and percent_lose > percent_tie:
        dominant = Fore.RED+'lose'
    else:
        dominant = 'tie'

    print(f'''
    Rounds Played: {rounds_played}
    {Fore.GREEN}Won: {percent_win:.0f}%
    {Fore.RED}Lost: {percent_lose:.0f}%
    {Fore.WHITE}Tied: {percent_tie:.0f}%
    According to the stats, you mostly {dominant}.
    ''')


# Ask the user if they would like to play again
play_again = input('Would you like to play again? (y/n): ')
if play_again == 'y' or play_again == 'yes':
    os.system('python rps.py')

print('Opening the main menu...')
exit()