# Import all nessesary modules
import random
import os
import os
from time import sleep
import numpy
from subprocess import *
import sys
import ctypes
import json
import socket


# import and run the idle_check.py file
sys.path.insert(0, './py/')
import idle_check as idle_check
idle_check.run()


def check_internet_connection():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        socket.create_connection(("1.1.1.1", 443))
        #socket.create_connection(("1.1.1.1", 8080))
        print('Connected to the internet')
    except OSError:
        print('''
            Not connected to the internet
            Please make sure that you are connected to the internet or that ports 53 and 443 are enabled
            Exiting program in 10s...
            ''')
        sleep(10)
        exit()


check_internet_connection()



# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')




# Change the default background and fore color for the terminal
# os.system('color f0')


# Import colorama module
# If the module is not installed, then automatically install it. Otherwise, continue the program
try:
    import colorama
    colorama.init()
    colorama.init(convert=True)
    colorama.init(autoreset=True)
    from colorama import *
except:
    print('You do not have the "colorama" module, we are installing it for you now...')
    import pip
    pip.main(['install', 'colorama'])
    import colorama
    colorama.init()
    colorama.init(convert=True)
    colorama.init(autoreset=True)
    from colorama import *

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


with open('config.json', 'r') as jsonConfig:
    config = json.load(jsonConfig)
    print(Fore.CYAN+'Your current balance is: '+Fore.RED+'${}'.format(config['balance']))

"""
config['key3'] = 'value3'

with open('config.json', 'w') as f:
    json.dump(config, f)

"""

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
    elif user_input == 'clear':
        print('')
    elif user_input == 'rps':
        print('')
    elif user_input == 'hl':
        print('')
    elif user_input == 'system':
        print(Fore.BLUE+'Opening python file for "system information"...')
        os.system('python info/system.py')
    elif user_input == 'profile':
        print(Fore.BLUE+'Opening profile website')
        import webbrowser
        webbrowser.open('https://github.com/shannon-nz')
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
        print(Fore.BLACK+'   clear '+Fore.BLUE+'= clear the terminal (action)')
        print(Fore.BLACK+'   lu '+Fore.BLUE+'= lucky unicorn (game)')
        print(Fore.BLACK+'   rps '+Fore.BLUE+'= rock paper scissors (game)')
        print(Fore.BLACK+'   hl '+Fore.BLUE+'= higher/lower (game)')
        print(Fore.BLACK+'   system '+Fore.BLUE+'= get your system information (info)')
        print(Fore.BLACK+'   profile '+Fore.BLUE+'= open my profile website (website)')
        print(Fore.BLACK+'   spaz '+Fore.BLUE+'= SPAZ YOUR SCREEN for 7 seconds (fun)')
        print(Fore.BLACK+'   restart '+Fore.BLUE+'= restart the application (action)')
        print(Fore.BLACK+'   quit '+Fore.BLUE+'= quit the entire program (action)')
        print(Fore.BLACK+'   help '+Fore.BLUE+'= display command details (help)')
    elif user_input == 'unha':
        import pip
        pip.main(['uninstall', 'colorama'])
        pip.main(['uninstall', 'pynput'])
        pip.main(['uninstall', 'keyboard'])
    else:
        print(Fore.RED+'Invalid Command')
