import random
import os
from os import *
from time import sleep
import numpy
from subprocess import *
import sys
import ctypes
import json


config = {"key1": "value1", "key2": "value2"}

with open('config1.json', 'w') as f:
    json.dump(config, f)



with open('config.json', 'r') as f:
    config = json.load(f)

#edit the data
config['key3'] = 'value3'

#write it back to the file
with open('config.json', 'w') as f:
    json.dump(config, f)


# import and run the idle_check.py file
sys.path.insert(0, './py/')
import idle_check as idle_check
idle_check.run()



# Customise the terminal design
LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]
# Terminal font settings
font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.nFont = 12
font.dwFontSize.X = 11
font.dwFontSize.Y = 18
font.FontFamily = 54
font.FontWeight = 500
font.FaceName = ""

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(False), ctypes.pointer(font))


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
    #keyboard.press('f11')
except:
    import pip
    print(Fore.RED+'You do not have the "keyboard" module, we are installing it for you now...')
    pip.main(['install', 'keyboard'])
    import keyboard
    #keyboard.press('f11')



keyboard.add_abbreviation("@email", "test@example.com")
#keyboard.on_release(lambda e: print(e.name))

"""
Styling for colorama
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
"""

print(Fore.GREEN+'Welcome to the main menu, listing commands...')

user_input = ''
while user_input != 'quit':
    print('\nType a command or "help": ', end='')
    user_input = input()
  

    if user_input == 'lu' or 'lucky unicorn':
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
    elif user_input == 'clear':
        call('clear' if os.name =='posix' else 'cls')
        print('Cleared the screen')
    elif user_input == 'profile':
        print(Fore.BLUE+'Opening profile website')
        import webbrowser
        webbrowser.open('https://github.com/shannon-nz')
    elif user_input == 'spaz':
        print(Fore.RED+'SPAZING YOUR SCREEN for 7 seconds !')
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
        print(Fore.RED+'quiting the application...')
        exit()
        print(Fore.RED+'Failed to quit the application, please try again')
    elif user_input == 'help':
        print(Fore.BLACK+'   lu = '+Fore.BLUE+'lucky unicorn (game)')
        print(Fore.BLACK+'   rps = '+Fore.BLUE+'rock paper scissors (game)')
        print(Fore.BLACK+'   hl = '+Fore.BLUE+'higher/lower (game)')
        print(Fore.BLACK+'   system = '+Fore.BLUE+'get your system information (info)')
        print(Fore.BLACK+'   clear = '+Fore.BLUE+'clear the screen (action)')
        print(Fore.BLACK+'   profile = '+Fore.BLUE+'open my profile website (website)')
        print(Fore.BLACK+'   spaz = '+Fore.BLUE+'SPAZ YOUR SCREEN for 7 seconds (fun)')
        print(Fore.BLACK+'   restart = '+Fore.BLUE+'restart the application (action)')
        print(Fore.BLACK+'   quit = '+Fore.BLUE+'quit the entire program (action)')
        print(Fore.BLACK+'   help = '+Fore.BLUE+'display command details (help)')
    else:
        print(Fore.RED+'Invalid Command')
