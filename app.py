import random
import os
from os import system, name

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
    pip.main(['install', 'pynput'])
    #from pynput.keyboard import Key, Controller
    from pynput.mouse import Button, Controller


try:
    import keyboard
    #keyboard.press('f11')
except:
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
        os.system('python luckyunicorn/00_LU_Base_v_01.py')
    elif user_input == 'help':
        print('*** Instructions ***')
        print('')
        print('*** Here are the Commands ***')
        print('   lu = lucky unicorn (game)')
        print('   rps = rock paper scissors (game)')
        print('   hl = higher/lower (game)')
        print('   clear = clear the screen (action)')
        print('   spaz = SPAZ YOUR SCREEN for 7 seconds (USE WITH CAUTION)')
        print('   restart = restart the application (action)')
        print('   quit = quit the entire program (action)')
        print('   help = display command details (help)')
    elif user_input == 'clear':
        clear()
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
    elif user_input == 'logout':
        print("Logging out of windows...")
        sleep(1)
        keyboard.press('windows')
        keyboard.press('l')
        keyboard.release('l')
        keyboard.release('windows')
    elif user_input == 'quit':
        print('quiting the application...')
        exit()
        print('Failed to quit the application, please try again')
    else:
        print('▼ INVALID COMMAND, PLEASE ENTER A VALID COMMAND ▼')
