# <<<<<<<<<<<<<<<<<<<< <<<<<<<<<< IMPORTS >>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>
import random
import os
import os
from time import sleep
import numpy
import subprocess
from subprocess import *
import sys
import ctypes
import json
import socket

sys.path.insert(0, './py/')
import idle_check as idle_check
idle_check.run()

# Import colorama module
# If the module is not installed, then automatically install it. Otherwise, continue the program
try:
    import colorama
    colorama.init()
    colorama.init(convert=True)
    colorama.init(autoreset=True)
    from colorama import Fore, Back, Style
except:
    print('You do not have the "colorama" module, we are installing it for you now...')
    import pip
    pip.main(['install', 'colorama'])
    import colorama
    colorama.init()
    colorama.init(convert=True)
    colorama.init(autoreset=True)
    from colorama import Fore, Back, Style

# Import pandas and tabulate module
# If the module is not installed, then automatically install it. Otherwise, continue the program
try:
    # importing the modules
    from tabulate import tabulate
    import pandas as pd
except:
    import pip
    print(Fore.RED+'You do not have the "pynput" module, we are installing it for you now...')
    pip.main(['install', 'tabulate'])
    # importing the modules
    from tabulate import tabulate
    import pandas as pd


# Import pynput module
# If the module is not installed, then automatically install it. Otherwise, continue the program
try:
    from pynput.mouse import Button, Controller
    mouse = Controller()
    mouse.position = (0, 0)
    print(Fore.BLUE+'Your mouse has been moved to the top left.')
except:
    import pip
    print(Fore.RED+'You do not have the "pynput" module, we are installing it for you now...')
    pip.main(['install', 'pynput'])
    #from pynput.keyboard import Key, Controller
    from pynput.mouse import Button, Controller
    from pynput import mouse

""" This is annoying
for item in range(1, 100):
    sleep(0.5)
    mouse.position = (0, 0)
"""

# Import keyboard module
# If the module is not installed, then automatically install it. Otherwise, continue the program
try:
    import keyboard
    keyboard.press('win+up')
    keyboard.release('win+up')
except:
    import pip
    print(Fore.RED+'You do not have the "keyboard" module, we are installing it for you now...')
    pip.main(['install', 'keyboard'])
    import keyboard
    keyboard.press('win+up')
    keyboard.release('win+up')


# <<<<<<<<<<<<<<<<<<<< <<<<<<<<<< FUNCTIONS >>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>

def check_internet_connection():
    try:
        # connect to the host -- tells us if the host is actually reachable
        socket.create_connection(("1.1.1.1", 443))
        return True
    except OSError:
        return False

def check_internet_on_start():
    if(check_internet_connection() == True):
        print('Connected to the internet')
    else:
        print('''
            Not connected to the internet
            Please make sure that you are connected to the internet or that ports 53 and 443 are enabled
            Exiting program in 10s...
            ''')
        sleep(10)
        exit()


def change_terminal_background(value): 
    # Change the default background and fore color for the terminal
    os.system('color '+value)

def mod_config(option, value, newval):
    if option == 'view':
        with open('config.json', 'r') as jsonConfig:
            config = json.load(jsonConfig)
        return config[value]
            
    elif option == 'mod':  
        with open('config.json', 'r') as jsonConfig:
            config = json.load(jsonConfig)
        config[value] = newval
        with open('config.json', 'w') as f:
            json.dump(config, f)


# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')


def stats():
    return ''


# <<<<<<<<<<<<<<<<<<<< <<<<<<<<<< SCRIPT >>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>

check_internet_on_start()


print(Fore.CYAN+'Your current balance is: '+Fore.RED+'${}'.format(mod_config('view','balance','')))



print(Fore.GREEN+'Welcome to the main menu, listing commands...')

user_input = ''
while user_input != 'quit':
    print('\nType a command or "help": ', end='')
    user_input = input()
  
    if user_input == 'clear':
        print('clearing screen...')
        screen_clear()

    elif user_input == 'lu':
        print(Fore.BLUE+'Opening Lucky Lucky Unicorn Game...')
        sleep(1)
        print('\n********** LUCKY UNICORN **********')
        os.system('python games/luckyunicorn/00_LU_Base_v_01.py')

    elif user_input == 'rps':
        print('coming soon .... \ngoing back to main menu...')

    elif user_input == 'hl':
        print('coming soon .... \ngoing back to main menu...')

    elif user_input == 'stats':
        # creating a DataFrame
        dict = {'Stats':['Connected to Internet', 'Balance'],
                'Result':[
                    check_internet_connection(),
                    '${}'.format(mod_config('view','balance',''))
                ]}
        df = pd.DataFrame(dict)
        # displaying the DataFrame
        print(tabulate(df, headers = 'keys', tablefmt = 'psql'))

    elif user_input == 'system':
        print(Fore.BLUE+'Opening python file for "system information"...')
        os.system('python info/system.py')
    elif user_input == 'profile':
        print(Fore.BLUE+'Opening profile website')
        import webbrowser
        webbrowser.open('https://github.com/shannon-nz')
    elif user_input == 'doc':
        print(Fore.BLUE+'Opening python games documentation')
        import webbrowser
        webbrowser.open('https://github.com/shannon-nz/python-games#-python-games-in-development-')
    elif user_input == 'spaz':
        print(Fore.RED+'SPAZING YOUR SCREEN for 7 seconds !  DO NOT CLICK ANYTHING')
        for item in range(1, 50):
            print(Fore.RED+'WARNING, IT IS ABOUT TO GET MAD !!!  DO NOT CLICK ANYTHING ')
            print(Fore.BLUE+'WARNING, IT IS ABOUT TO GET MAD !!!  DO NOT CLICK ANYTHING ')
            print(Fore.YELLOW+'WARNING, IT IS ABOUT TO GET MAD !!!  DO NOT CLICK ANYTHING ')
            print(Fore.WHITE+'WARNING, IT IS ABOUT TO GET MAD !!!  DO NOT CLICK ANYTHING ')
            print(Fore.BLACK+'WARNING, IT IS ABOUT TO GET MAD !!!  DO NOT CLICK ANYTHING ')
            print(Fore.GREEN+'WARNING, IT IS ABOUT TO GET MAD !!!  DO NOT CLICK ANYTHING ')
            print(Fore.MAGENTA+'WARNING, IT IS ABOUT TO GET MAD !!!  DO NOT CLICK ANYTHING ')
            print(Fore.CYAN+'WARNING, IT IS ABOUT TO GET MAD !!!')
        spaz_msg = 'SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ '
        for item in range(1, 21):
            keyboard.press('f11')
            keyboard.release('f11')
            keyboard.press('windows')
            keyboard.release('windows')
            keyboard.press('alt+tab')
            keyboard.release('alt+tab')
            rand1 = random.randrange(0, 1900)
            rand2 = random.randrange(0, 1900)
            mouse.position = (rand1, rand2)
            print(Fore.RED+spaz_msg)
            print(Fore.BLUE+spaz_msg)
            print(Fore.YELLOW+spaz_msg)
            print(Fore.WHITE+spaz_msg)
            print(Fore.BLACK+spaz_msg)
            print(Fore.GREEN+spaz_msg)
            print(Fore.MAGENTA+spaz_msg)
            print(Fore.CYAN+spaz_msg)
            sleep(0.1)
        print('\n\nAnd that is why you should be careful what you click on!')
    elif user_input == 'restart':
        os.system('python app.py')
    elif user_input == 'quit':
        print(Fore.RED+'quiting the application...')
        exit()
        print(Fore.RED+'Failed to quit the application, please try again')
    elif user_input == 'help':
        print(Fore.BLACK+'   clear     '+Fore.BLUE+'clear the terminal (action)')
        print(Fore.BLACK+'   lu        '+Fore.BLUE+'lucky unicorn (game)')
        print(Fore.BLACK+'   rps       '+Fore.BLUE+'rock paper scissors (game)')
        print(Fore.BLACK+'   hl        '+Fore.BLUE+'higher/lower (game)')
        print(Fore.BLACK+'   stats     '+Fore.BLUE+'View your stats')
        print(Fore.BLACK+'   system    '+Fore.BLUE+'get your system information (info)')
        print(Fore.BLACK+'   profile   '+Fore.BLUE+'open my profile website (website)')
        print(Fore.BLACK+'   doc       '+Fore.BLUE+'open python games documentation (website)')
        print(Fore.BLACK+'   spaz      '+Fore.BLUE+'SPAZ YOUR SCREEN for 7 seconds (fun)')
        print(Fore.BLACK+'   restart   '+Fore.BLUE+'restart the application (action)')
        print(Fore.BLACK+'   quit      '+Fore.BLUE+'quit the entire program (action)')
        print(Fore.BLACK+'   help      '+Fore.BLUE+'display command details (help)')
        print(Fore.BLACK+'   help-des  '+Fore.BLUE+'display command details and an longer description (help)')
    elif user_input == 'unha':
        import pip
        pip.main(['uninstall', 'colorama'])
        pip.main(['uninstall', 'pynput'])
        pip.main(['uninstall', 'keyboard'])
    else:
        print(Fore.RED+'Invalid Command')
