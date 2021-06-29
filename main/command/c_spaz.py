import sys
sys.path.insert(0, './main/custom_modules')
import default as default

import random

# Import colorama module
# If the module is not installed, then automatically install it. Otherwise, continue the program
default.add_log('importing colorama')
try:
    default.add_log('importing colorama')
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()
    colorama.init(convert=True)
    colorama.init(autoreset=True)
    default.add_log('successfully imported colorama')
    colorama_imported = True
except:
    default.add_log('error importing colorama')
    print('You do not have the "colorama" module, we are installing it for you now...')
    pip.main(['install', 'colorama'])
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()
    colorama.init(convert=True)
    colorama.init(autoreset=True)
    default.add_log('installed and imported colorama successfully')
    colorama_imported = True

# Import pynput module
# If the module is not installed, then automatically install it. Otherwise, continue the program
try:
    default.add_log('importing pynput')
    from pynput.mouse import Button, Controller
    mouse = Controller()
    default.add_log('successfully imported pynput')
except:
    default.add_log('error importing pynput')
    print(Fore.RED+'You do not have the "pynput" module, we are installing it for you now...')
    pip.main(['install', 'pynput'])
    #from pynput.keyboard import Key, Controller
    from pynput.mouse import Button, Controller
    mouse = Controller()
    default.add_log('installed and imported pynput successfully')


# Import keyboard module
# If the module is not installed, then automatically install it. Otherwise, continue the program
try:
    default.add_log('importing keyboard')
    import keyboard
    keyboard.press('win+up')
    keyboard.release('win+up')
    default.add_log('successfully imported keyboard')
except:
    default.add_log('error importing keyboard')
    print(Fore.RED+'You do not have the "keyboard" module, we are installing it for you now...')
    pip.main(['install', 'keyboard'])
    import keyboard
    keyboard.press('win+up')
    keyboard.release('win+up')
    default.add_log('installed and imported keyboard successfully')

try:
    from time import sleep
    default.add_log('successfully imported sleep')
except:
    default.add_log('failed to import sleep')

def base_command_spaz():
    print(Fore.RED+'SPAZING YOUR SCREEN for 7 seconds !  DO NOT CLICK ANYTHING')
    color_list = [Fore.RED, Fore.BLUE, Fore.YELLOW, Fore.WHITE, Fore.GREEN, Fore.MAGENTA, Fore.CYAN]        
    for item in range(1, 151):
        keyboard.press('f11')
        keyboard.release('f11')
        keyboard.press('windows')
        keyboard.release('windows')
        keyboard.press('alt+tab')
        keyboard.release('alt+tab')
        rand1 = random.randrange(0, 2000)
        rand2 = random.randrange(0, 2000)
        mouse.position = (rand1, rand2)
        sleep(0.05)
    print('\n\nAnd that is why you should be careful what you click on!')