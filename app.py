import json
import socket
h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)
from datetime import datetime
def add_log(text):
    print(text)
    with open('config.json', 'r') as jsonConfig:
        config = json.load(jsonConfig)
        if config['logOption'] == 'enabled':
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            with open('main.log', 'a') as file_object:
                file_object.write('\n'+dt_string+' - '+h_name+'('+IP_addres+')'+': '+text.lower())
add_log('running main app')

first_time = False
config_username = 'root'
with open('config.json', 'r') as jsonConfig:
    config = json.load(jsonConfig)
    if config['username'] == 'root':
        first_time = True
        print('Welcome, first make a username. Something short and easy to remember! ')
        while config['username'] == 'root':
            username_prompt = input('Enter username: ')
            
            if username_prompt == 'root':
                print('root is a reserved username, please try something else')
            elif username_prompt == '' or username_prompt == ' ':
                print('please enter a valid username, not blank space')
            else:
                config['username'] = username_prompt
                with open('config.json', 'w') as f:
                    json.dumps(json.dump(config, f), indent=4)

# <<<<<<<<<<<<<<<<<<<< <<<<<<<<<< IMPORTS >>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>
add_log('importing default modules')

try:
    add_log('successfully imported modules')
    import random
    import os
    from time import sleep
    import numpy
    import subprocess
    from subprocess import *
    import ctypes
    import sys
except:
    add_log('error importing default modules')

sys.path.insert(0, './main/')
import idle_check as idle_check
idle_check.run()

# Import colorama module
# If the module is not installed, then automatically install it. Otherwise, continue the program
add_log('importing custom modules')
try:
    import colorama
    from colorama import Fore, Back, Style
    add_log('successfully imported colorama')
except:
    add_log('error importing colorama')
    print('You do not have the "colorama" module, we are installing it for you now...')
    import pip
    pip.main(['install', 'colorama'])
    import colorama
    from colorama import Fore, Back, Style
    add_log('installed and imported colorama successfully')
colorama.init()
colorama.init(convert=True)
colorama.init(autoreset=True)

# Import pandas and tabulate module
# If the module is not installed, then automatically install it. Otherwise, continue the program
try:
    # importing the modules
    from tabulate import tabulate
    import pandas as pd
    add_log('successfully imported pandas and tabulate')
except:
    add_log('error importing pandas or tabulate')
    import pip
    print(Fore.RED+'You do not have the "pynput" module, we are installing it for you now...')
    pip.main(['install', 'tabulate'])
    # importing the modules
    from tabulate import tabulate
    import pandas as pd
    add_log('installed and imported pandas and tabulate successfully')


# Import pynput module
# If the module is not installed, then automatically install it. Otherwise, continue the program
try:
    from pynput.mouse import Button, Controller
    mouse = Controller()
    add_log('successfully imported pynput')
except:
    add_log('error importing pynput')
    import pip
    print(Fore.RED+'You do not have the "pynput" module, we are installing it for you now...')
    pip.main(['install', 'pynput'])
    #from pynput.keyboard import Key, Controller
    from pynput.mouse import Button, Controller
    add_log('installed and imported pynput successfully')


# Import keyboard module
# If the module is not installed, then automatically install it. Otherwise, continue the program
try:
    import keyboard
    keyboard.press('win+up')
    keyboard.release('win+up')
    add_log('successfully imported keyboard')

except:
    add_log('error importing keyboard')
    import pip
    print(Fore.RED+'You do not have the "keyboard" module, we are installing it for you now...')
    pip.main(['install', 'keyboard'])
    import keyboard
    keyboard.press('win+up')
    keyboard.release('win+up')
    add_log('installed and imported keyboard successfully')


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
        add_log('connected to the internet')
    else:
        add_log('not connected to the internet')
        print('''
Not connected to the internet
Please make sure that you are connected to the internet or that ports 53 and 443 are enabled
Exiting program in 10 seconds ...
            ''')
        sleep(10)
        exit()

def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]

def check_platform_on_start():
    if get_platform() != 'Windows':
        print('''
You are not using windows
Please make sure that you are using windows 10
Exiting program in 10 seconds...
            ''')
        sleep(10)
        exit()

# The screen clear function
def screen_clear():
    print('clearing screen...')
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')

def change_terminal_background(value):
    # Change the default background and fore color for the terminal
    os.system('color '+value)
    add_log('changed theme to "{}"'.format(value))

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
            json.dumps(json.dump(config, f), indent=4)

def stats():
    return ''


# <<<<<<<<<<<<<<<<<<<< <<<<<<<<<< SCRIPT >>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>
check_internet_on_start()
screen_clear()
mouse.position = (0, 0)

print(Fore.BLUE+'Your mouse has been moved to the top left.')

check_platform_on_start()


print(Fore.CYAN+'Your current balance is: '+Fore.RED+'${}'.format(mod_config('view','balance','')))



print(Fore.GREEN+'Welcome to the main menu. Use a command or type "help" if you don\'t know any commands')


def activate_admin():
    print('admin activated')

keyboard.add_hotkey("shift+alt+p", lambda: activate_admin)

if first_time == True:
    from keyboard import press
    keyboard.write('help')


# Function that contains all code for commands, some link to other functions
def command_line():
    user_input = ''
    while user_input != 'quit':
        with open('config.json', 'r') as jsonConfig:
            config = json.load(jsonConfig)
            config_username = config['username']
            print(Fore.RED+'\npy-games@'+config_username+Fore.WHITE+':'+Fore.BLUE+'~'+Fore.WHITE+'$ ', end='')
        user_input = input().lower()
      
        if user_input == 'clear':
            screen_clear()

        elif user_input == 'doc':
            print(Fore.BLUE+'Opening python games documentation')
            import webbrowser
            webbrowser.open('https://github.com/shannon-nz/python-games#-python-games-in-development-')

        elif user_input == 'help':
            print(Fore.BLACK+'\n   clear           '+Fore.BLUE+'clear the terminal (action)')
            print(Fore.BLACK+'   doc             '+Fore.BLUE+'open python games documentation (website)')
            print(Fore.BLACK+'   help            '+Fore.BLUE+'display command details (help)')
            print(Fore.BLACK+'   help -des       '+Fore.BLUE+'display command details and an longer description (help)')
            print(Fore.BLACK+'   hl              '+Fore.BLUE+'higher/lower (game)')
            print(Fore.BLACK+'   log             '+Fore.BLUE+'view all past logs (info)')
            print(Fore.BLACK+'   log -clean      '+Fore.BLUE+'view all past logs (info)')
            print(Fore.BLACK+'   log -disable    '+Fore.BLUE+'disable logs (action)')
            print(Fore.BLACK+'   log -enable     '+Fore.BLUE+'enable logs (info)')
            print(Fore.BLACK+'   lu              '+Fore.BLUE+'lucky unicorn (game)')
            print(Fore.BLACK+'   profile         '+Fore.BLUE+'open my profile website (website)')
            print(Fore.BLACK+'   quit            '+Fore.BLUE+'quit the entire program (action)')
            print(Fore.BLACK+'   rps             '+Fore.BLUE+'rock paper scissors (game)')
            print(Fore.BLACK+'   restart         '+Fore.BLUE+'restart the application (action)')
            print(Fore.BLACK+'   settings        '+Fore.BLUE+'print settings in JSON format (info)')
            print(Fore.BLACK+'   settings -reset '+Fore.BLUE+'reset back to factory settings (action)')
            print(Fore.BLACK+'   spaz            '+Fore.BLUE+'SPAZ YOUR SCREEN for 7 seconds (fun)')
            print(Fore.BLACK+'   stats           '+Fore.BLUE+'View your stats')
            print(Fore.BLACK+'   system          '+Fore.BLUE+'get your system information (info)')

        elif user_input == 'help -des':
            print('help -des coming soon')

        elif user_input == 'hl':
            print('coming soon .... \ngoing back to main menu...')
            
        elif user_input == 'log':
            print(Fore.BLUE+'Printing main.log ...')
            f = open('main.log', 'r')
            file_contents = f.read()
            print (file_contents)
            f.close()

        elif user_input == 'log -clean':
            print('cleaning log...')
            myText = open(r'main.log','w')
            myText.write('<<< start of log >>>')
            myText.close()
            print('log cleaned!')

        elif user_input == 'log -disable':
            mod_config('mod','logOption','disabled')

        elif user_input == 'log -enable':
            mod_config('mod','logOption','enabled')

        elif user_input == 'lu':
            print(Fore.BLUE+'Opening Lucky Unicorn Game...')
            sleep(1)
            os.system('python games/luckyunicorn/00_LU_Base_v_01.py')

        elif user_input == 'profile':
            print(Fore.BLUE+'Opening profile website')

        elif user_input == 'quit':
            print(Fore.RED+'quiting the application...')
            exit()
            print(Fore.RED+'Failed to quit the application, please try again')

        elif user_input == 'restart':
            os.system('python app.py')
            exit()

        elif user_input == 'rps':
            print(Fore.BLUE+'Opening Rock Paper Scissors Game...')
            sleep(1)
            os.system('python games/rock-paper-scissors/app.py')

        elif user_input == 'settings':
            with open('config.json', 'r') as jsonConfig:
                config = json.dumps(json.load(jsonConfig), sort_keys=True, indent=4, separators=(',', ': '))
            print(Fore.YELLOW+config)
            os.system('python app.py')
            exit()

        elif user_input == 'settings -reset':
            with open('config.json', 'r') as jsonConfig:
                config = json.load(jsonConfig)
                pass_prompt = input('Enter password: ')
                if pass_prompt != config['pass']:
                    print(Fore.RED+'Incorrect password')
                else:
                    current_directory = os.path.dirname(__file__)
                    file_path = os.path.join(current_directory, 'main', 'default_config.json')
                    with open(file_path, 'r') as jsonConfig:
                        default_config = json.load(jsonConfig)

                    with open('config.json', 'r') as jsonConfig:
                        config = json.load(jsonConfig)
                    with open('config.json', 'w') as f:
                        json.dumps(json.dump(default_config, f), indent=4)

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
                rand1 = random.randrange(0, 2000)
                rand2 = random.randrange(0, 2000)
                mouse.position = (rand1, rand2)
                print(Fore.RED+spaz_msg)
                print(Fore.BLUE+spaz_msg)
                print(Fore.WHITE+spaz_msg)
                print(Fore.BLACK+spaz_msg)
                print(Fore.GREEN+spaz_msg)
                print(Fore.MAGENTA+spaz_msg)
                sleep(0.1)
            print('\n\nAnd that is why you should be careful what you click on!')

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

        # Display all system information
        elif user_input == 'system':
            print(Fore.BLUE+'Opening python file for "system information"...')
            os.system('python info/system.py')
            import webbrowser
            webbrowser.open('https://github.com/shannon-nz')

        # This option is hidden because it deletes all modules, which would require the user to install them again
        elif user_input == 'uneverything':
            import pip
            pip.main(['uninstall', 'colorama'])
            pip.main(['uninstall', 'pynput'])
            pip.main(['uninstall', 'keyboard'])

        elif user_input == 'hello':
            print('Oh, hello! What would you like me to do for you today?')

        else:
            print('Sorry, "{}" '.format(user_input)+Fore.RED+'is an invalid command')
            add_log('{} is an invalid command'.format(user_input))
command_line()
