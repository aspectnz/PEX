print(
'''

█░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀ ░ ░ ░
█▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█ ▄ ▄ ▄

PLEASE WAIT A SECOND
''')
import json
import socket
h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)
from datetime import datetime
def add_log(text):
    print(text)
    with open('main/config.json', 'r') as jsonConfig:
        config = json.load(jsonConfig)
        if config['logOption'] == 'enabled':
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            with open('main/data.log', 'a') as file_object:
                file_object.write('\n'+dt_string+' - '+h_name+'('+IP_addres+')'+': '+text.lower())
add_log('running main app')

first_time = False
config_username = 'root'
with open('main/config.json', 'r') as jsonConfig:
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
                with open('main/config.json', 'w') as f:
                    json.dumps(json.dump(config, f), indent=4)

# <<<<<<<<<<<<<<<<<<<< <<<<<<<<<< IMPORTS >>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>
add_log('importing default modules')
import sys
try:
    add_log('successfully imported modules')
    import random
    import os
    from time import sleep
    import numpy
    import subprocess
    from subprocess import *
    import ctypes
    import pip
    from pip import *
except:
    add_log('error importing default modules')

sys.path.insert(0, './main/custom_modules')
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
    os.system('pip install colorama')
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
    print(Fore.RED+'You do not have the "pynput" module, we are installing it for you now...')
    os.system('pip install tabulate')
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
    print(Fore.RED+'You do not have the "pynput" module, we are installing it for you now...')
    os.system('pip install pynput')
    #from pynput.keyboard import Key, Controller
    from pynput.mouse import Button, Controller
    mouse = Controller()
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
    os.system('pip install keyboard')
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
        with open('main/config.json', 'r') as jsonConfig:
            config = json.load(jsonConfig)
        return config[value]
            
    elif option == 'mod':  
        with open('main/config.json', 'r') as jsonConfig:
            config = json.load(jsonConfig)
        config[value] = newval
        with open('main/config.json', 'w') as f:
            json.dumps(json.dump(config, f), indent=4)

def spaz_screen():
    print(Fore.RED+'SPAZING YOUR SCREEN for 7 seconds !  DO NOT CLICK ANYTHING')
    for item in range(1, 50):
        print(Fore.RED+'WARNING, IT IS ABOUT TO GET MAD !!!  DO NOT CLICK ANYTHING ')
        print(Fore.BLUE+'WARNING, IT IS ABOUT TO GET MAD !!!  DO NOT CLICK ANYTHING ')
        print(Fore.YELLOW+'WARNING, IT IS ABOUT TO GET MAD !!!  DO NOT CLICK ANYTHING ')
        print(Fore.WHITE+'WARNING, IT IS ABOUT TO GET MAD !!!  DO NOT CLICK ANYTHING ')
        print(Fore.GREEN+'WARNING, IT IS ABOUT TO GET MAD !!!  DO NOT CLICK ANYTHING ')
        print(Fore.MAGENTA+'WARNING, IT IS ABOUT TO GET MAD !!!  DO NOT CLICK ANYTHING ')
        print(Fore.CYAN+'WARNING, IT IS ABOUT TO GET MAD !!!')
    spaz_msg = 'SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ SPAZ '
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
        print(Fore.GREEN+spaz_msg)
    print('\n\nAnd that is why you should be careful what you click on!')

def download(url, filename):
    print(Fore.BLUE+'[*] Downloading '+filename+' from '+url)
    import requests
    filepath = 'downloads/'+filename
    with open(filepath, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')
        if total is None:
            f.write(response.content)
        else:
            print(Fore.BLUE+'preparing download...')
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                downloaded += len(data)
                f.write(data)
                done = int(100*downloaded/total)
                sys.stdout.write('\r[{}{}]'.format('/' * done, '.' * (50-done)))
                sys.stdout.flush()
    sys.stdout.write('\n')
    print(Fore.BLUE+'Download complete, please check the downloads folder')

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# When the command is valid but contains additional invalid text
def invalid_command_ext(command_string, user_input):
    invalid_text = user_input[len(command_string):len(user_input)]
    print(Fore.RED+'The "{}" command was identified, but contained invalid text "{}"'.format(command_string, invalid_text))

# Help command function
def base_command_help(user_input, command_string):
    # calculate where the dash should be (if there is)
    expected_dash = user_input[len(command_string)+1:len(command_string)+2]
    # base command
    if user_input == command_string:
        command_color = Fore.CYAN
        des_color = Fore.BLUE
        master_command_list = {
            'advanced': {
                'brief_description': 'display advanced commands',
                'description': ''
            },
            'clear':{
                'brief_description': 'clear the terminal',
                'description': ''
            },
            'doc':{
                'brief_description': 'open python games documentation on GitHub',
                'description': ''
            },
            'help':{
                'brief_description': 'display commands and functions',
                'description': ''
            },
            'help -cat':{
                'brief_description': 'display commands and functions, formatted into categories',
                'description': ''
            },
            'help -des':{
                'brief_description': 'display command details and an longer description',
                'description': ''
            },
            'help -des -cat':{
                'brief_description': 'display command details and an longer description, formatted into categories',
                'description': ''
            },
            'hl':{
                'brief_description': 'play higher/lower game',
                'description': ''
            },
            'log':{
                'brief_description': 'view all past logs',
                'description': ''
            },
            'log -clean':{
                'brief_description': 'view all past logs',
                'description': ''
            },
            'log -disable':{
                'brief_description': 'disable logs',
                'description': ''
            },
            'log -enable':{
                'brief_description': 'enable logs',
                'description': ''
            },
            'ls':{
                'brief_description': 'list directory',
                'description': ''
            },
            'lu':{
                'brief_description': 'play lucky unicorn game',
                'description': ''
            },
            'profile':{
                'brief_description': 'open my profile website',
                'description': ''
            },
            'quit':{
                'brief_description': 'quit the entire program',
                'description': ''
            },
            'rps':{
                'brief_description': 'play rock paper scissors game',
                'description': ''
            },
            'restart':{
                'brief_description': 'restart the application',
                'description': ''
            },
            'settings':{
                'brief_description': 'print settings in JSON format',
                'description': ''
            },
            'settings -reset':{
                'brief_description': 'reset back to factory settings',
                'description': ''
            },
            'spaz':{
                'brief_description': 'SPAZ YOUR SCREEN for 7 seconds (caution)',
                'description': ''
            },
            'stats':{
                'brief_description': 'view your stats',
                'description': ''
            },
            'system':{
                'brief_description': 'get your system information',
                'description': ''
            }
        }
        print()
        for key, value in master_command_list.items():
            num = 30-len(key)
            tabs = ' '*num
            print(command_color+'   '+key+tabs+des_color+value['brief_description'])
    # sub commands for command
    elif expected_dash == '-':
        # identify sub command
        sub_command = user_input[len(command_string)+2:len(user_input)]
        if sub_command == 'des':
            print('sub command was correctly des')
        else:
            print(Fore.RED+'The "-{}" sub command is invalid'.format(sub_command))
    # otherwise inform user that the command was identified, but had had a type
    else:
        invalid_command_ext(command_string, user_input)

# highler lower game command function
def base_command_hl(user_input, command_string):
    # calculate where the dash should be (if there is)
    expected_dash = user_input[len(command_string)+1:len(command_string)+2]
    # base command
    if user_input == command_string:
        print('coming soon .... \ngoing back to main menu...')
    # sub commands for command
    elif expected_dash == '-':
        # identify sub command
        sub_command = user_input[len(command_string)+2:len(user_input)]
        if sub_command == 'help':
            print('coming soon .... \ngoing back to main menu...')
        else:
            print(Fore.RED+'The "-{}" sub command is invalid'.format(sub_command))
    # otherwise inform user that the command was identified, but had had a type
    else:
        invalid_command_ext(command_string, user_input)

# log command function
def base_command_log(user_input, command_string):
    # calculate where the dash should be (if there is)
    expected_dash = user_input[len(command_string)+1:len(command_string)+2]
    # base command
    if user_input == command_string:
        print(Fore.BLUE+'Printing data.log ...')
        f = open('main/data.log', 'r')
        file_contents = f.read()
        print (file_contents)
        f.close()
    # sub commands for command
    elif expected_dash == '-':
        # identify sub command
        sub_command = user_input[len(command_string)+2:len(user_input)]
        if sub_command == 'clean':
            print('cleaning log...')
            myText = open(r'main/data.log','w')
            myText.write('<<< start of log >>>')
            myText.close()
            print('log cleaned!')
        elif sub_command == 'disable':
            mod_config('mod','logOption','disabled')
        elif sub_command == 'enable':
            mod_config('mod','logOption','enabled')
        elif sub_command == 'help':
            print('log definition')
        else:
            print(Fore.RED+'The "-{}" sub command is invalid'.format(sub_command))
    # otherwise inform user that the command was identified, but had had a type
    else:
        invalid_command_ext(command_string, user_input)

def stats():
    return ''


# <<<<<<<<<<<<<<<<<<<< <<<<<<<<<< SCRIPT >>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>
#check_internet_on_start()
screen_clear()
mouse.position = (0, 0)

print(Fore.GREEN+
    '''

██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗░░░░░░░██████╗░░█████╗░███╗░░░███╗███████╗░██████╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║░░░░░░██╔════╝░██╔══██╗████╗░████║██╔════╝██╔════╝
██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║█████╗██║░░██╗░███████║██╔████╔██║█████╗░░╚█████╗░
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║╚════╝██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░░╚═══██╗
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║░░░░░░╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██████╔╝
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝░░░░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░
    ''')

print(Fore.BLUE+'Your mouse has been moved to the top left.')

check_platform_on_start()


print(Fore.CYAN+'Your current balance is: '+Fore.RED+'${}'.format(mod_config('view','balance','')))
if first_time == True:
    print(Fore.WHITE+'''
Welcome to python-games!
As this may be your first time using this application, this is just a reminder to make sure that you have 
read the documentation so you know how to use this app properly. Otherwise, you may run into some 
unexpected problems :D

''')
    from keyboard import press
    keyboard.write('help')


print(Fore.GREEN+'Welcome to the main menu. Use a command or type "help" if you don\'t know any commands')





def activate_admin():
    print('admin activated')

keyboard.add_hotkey("shift+alt+p", lambda: activate_admin)


# Function that contains all code for commands, some link to other functions
def command_line():
    user_input = ''
    while user_input != 'quit':
        with open('main/config.json', 'r') as jsonConfig:
            config = json.load(jsonConfig)
            config_username = config['username']
            print(Fore.RED+'\npy-games@'+config_username+Fore.WHITE+':'+Fore.BLUE+'~'+Fore.WHITE+'$ ', end='')
        user_input = input().lower()
      
        if user_input == 'advanced':
            print()
            print_color = Fore.CYAN
            print(print_color+'   admin (command)      '+Fore.BLUE+'perform commands as admin, use before any command')
            print(print_color+'   clear                '+Fore.BLUE+'clear the terminal')

        elif user_input == 'clear':
            screen_clear()

        elif user_input == 'doc':
            print(Fore.BLUE+'Opening python games documentation')
            import webbrowser
            webbrowser.open('https://github.com/shannon-nz/python-games#-python-games-in-development-')

        elif user_input == 'download':
            download('https://github.com/shannon-nz/python-games/blob/main/main/games/luckyunicorn/Python%20Program%20Documentation.pptx?raw=true', 'luckyunicorn_documentation.pptx')

        # check if this is the valid command
        elif user_input[0:len('help')] == 'help':
            base_command_help(user_input, 'help')

        # check if this is the valid command
        elif user_input[0:len('hl')] == 'hl':
            base_command_hl(user_input, 'hl')

        # check if this is the valid command
        elif user_input[0:len('log')] == 'log':
            base_command_log(user_input, 'log')

        elif user_input == 'ls':
            os.system('dir')

        elif user_input == 'lu':
            print(Fore.BLUE+'Opening Lucky Unicorn Game...')
            sleep(1)
            os.system('python main/games/luckyunicorn/00_LU_Base_v_01.py')

        elif user_input == 'profile':
            print(Fore.BLUE+'Opening profile website')

        elif user_input == 'quit':
            print(Fore.RED+'quiting the application...')
            exit()
            print(Fore.RED+'Failed to quit the application, please try again')

        elif user_input == 'restart':
            add_log('restarting application...')
            os.system('python app.py')
            exit()

        elif user_input == 'rps':
            print(Fore.BLUE+'Opening Rock Paper Scissors Game...')
            sleep(1)
            os.system('python main/games/rock-paper-scissors/app.py')

        elif user_input == 'settings':
            with open('main/config.json', 'r') as jsonConfig:
                config = json.dumps(json.load(jsonConfig), sort_keys=True, indent=4, separators=(',', ': '))
            print(Fore.YELLOW+config)

        elif user_input == 'settings -reset':
            print('This will reset the entire application and it\'s configurations\nAre you sure you want to reset? (y/n)', end='')
            verification_prompt = input('')
            with open('main/config.json', 'r') as jsonConfig:
                config = json.load(jsonConfig)
                pass_prompt = input('Enter password: ')
                if pass_prompt != config['pass']:
                    print(Fore.RED+'Incorrect password')
                else:
                    current_directory = os.path.dirname(__file__)
                    file_path = os.path.join(current_directory, 'main\\info', 'default_config.json')
                    with open(file_path, 'r') as jsonConfig:
                        default_config = json.load(jsonConfig)
                    with open('main/config.json', 'r') as jsonConfig:
                        config = json.load(jsonConfig)
                    with open('main/config.json', 'w') as f:
                        json.dumps(json.dump(default_config, f), indent=4)
                    add_log('settings have been reset')
                    add_log('restarting the application...')
                    screen_clear()
                    os.system('python app.py')
                    exit()

        elif user_input == 'spaz':
            spaz_screen()

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
            os.system('python main/info/system.py')
            import webbrowser
            webbrowser.open('https://github.com/shannon-nz')

        # This option is hidden because it deletes all modules, which would require the user to install them again
        elif user_input == 'remove -modules':
            import pip
            pip.main(['uninstall', 'colorama'])
            pip.main(['uninstall', 'pynput'])
            pip.main(['uninstall', 'tabulate'])
            pip.main(['uninstall', 'keyboard'])
            pip.main(['uninstall', 'requests'])

        elif user_input == 'hello':
            print('Oh, hello! What would you like me to do for you today?')

        elif user_input == 'admin':
            print('Admin mode now enabled')

        elif user_input == 'custom_command':
            with open('main/config.json', 'r') as jsonConfig:
                config = json.load(jsonConfig)
                config_username = config['username']

        else:
            print('Sorry, "{}" '.format(user_input)+Fore.RED+'is an invalid command')
            add_log('{} is an invalid command'.format(user_input))
command_line()
