import random
import os
from os import *
from time import sleep
import numpy
import pip
import subprocess
import sys


try:
    from pynput.mouse import Button, Controller
    mouse = Controller()
    mouse.position = (0, 0)
    print('Your mouse has been moved to the top left.')
except:
    print('You do not have the "pynput" module, we are installing it for you now...')
    pip.main(['install', 'pynput'])
    #from pynput.keyboard import Key, Controller
    from pynput.mouse import Button, Controller


try:
    import keyboard
    #keyboard.press('f11')
except:
    print('You do not have the "keyboard" module, we are installing it for you now...')
    pip.main(['install', 'keyboard'])
    import keyboard
    #keyboard.press('f11')

print("idlelib" in sys.modules)


def clear(): 
    # windows
    if name == 'nt':
        _ = system('cls')
    # mac and linux (os.name is 'posix')
    else:
        _ = system('clear')

keyboard.add_abbreviation("@email", "test@example.com")
#keyboard.on_release(lambda e: print(e.name))

print('Welcome to the main menu, listing commands...')

user_input = ''
while user_input != 'quit':
    user_input = input('\nType a command or "help": ')
  

    if user_input == 'lu':
        print('Opening Lucky Lucky Unicorn Game...')
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
        print('Opening python file for "system information"...')
        os.system('python info/system.py')
    elif user_input == 'clear':
        clear()
    elif user_input == 'profile':
        import webbrowser
        webbrowser.open('https://github.com/shannon-nz')
    elif user_input == 'spaz':
        print('SPAZING YOUR SCREEN for 7 seconds !')
        for item in range(1, 101):
            keyboard.press('f11')
            keyboard.release('f11')
            keyboard.press('windows')
            keyboard.release('windows')
            rand1 = random.randrange(0, 1300)
            rand2 = random.randrange(0, 1300)
            mouse.position = (rand1, rand2)
            sleep(0.05)
        print('\n\nAnd that is why you should be careful what you click on!')
    elif user_input == 'restart':
        os.system('python app.py')
    elif user_input == 'quit':
        print('quiting the application...')
        exit()
        print('Failed to quit the application, please try again')
    elif user_input == 'help':
        print('*** Here are the Commands ***')
        print('   lu = lucky unicorn (game)')
        print('   rps = rock paper scissors (game)')
        print('   hl = higher/lower (game)')
        print('   system = get your system information (info)')
        print('   clear = clear the screen (action)')
        print('   profile = Open my profile website (website)')
        print('   spaz = SPAZ YOUR SCREEN for 7 seconds (USE WITH CAUTION)')
        print('   restart = restart the application (action)')
        print('   quit = quit the entire program (action)')
        print('   help = display command details (help)')
    else:
        print('▼ INVALID COMMAND, PLEASE ENTER A VALID COMMAND ▼')
