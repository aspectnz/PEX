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
        if config['options']['log'] == 'enabled':
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            with open('main/data.log', 'a') as file_object:
                file_object.write('\n'+dt_string+' - '+h_name+'('+IP_addres+')'+': '+text.lower())
add_log('running main app')

first_time = False
config_username = 'root'
with open('main/config.json', 'r') as jsonConfig:
    config = json.load(jsonConfig)
    if config['user']['username'] == 'root':
        first_time = True
        print('Welcome, first make a username. Something short and easy to remember! ')
        while config['user']['username'] == 'root':
            username_prompt = input('Enter username: ')
            
            if username_prompt == 'root':
                print('root is a reserved username, please try something else')
            elif username_prompt == '' or username_prompt == ' ':
                print('please enter a valid username, not blank space')
            else:
                config['user']['username'] = username_prompt
                with open('main/config.json', 'w') as f:
                    json.dump(config, f, indent=4, sort_keys=True)

# <<<<<<<<<<<<<<<<<<<< <<<<<<<<<< IMPORTS >>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>
add_log('importing default modules')
import sys
try:
    add_log('successfully imported modules')
    import random
    import os
    from time import sleep
    import subprocess
    from subprocess import *
    import ctypes
except:
    add_log('error importing default modules')

def idle_check():
    sys.path.insert(0, './main/custom_modules')
    import idle_check as idle_check
    idle_check.run()
idle_check()

import pip




import ctypes
import enum
import sys

# Import numpy module
# If the module is not installed, then automatically install it. Otherwise, continue the program
try:
    import numpy
    add_log('successfully imported colorama')
except:
    add_log('error importing numpy')
    print('You do not have the "numpy" module, we are installing it for you now...')
    pip.main(['install', 'numpy'])
    import numpy
    add_log('installed and imported colorama successfully')

# Import colorama module
# If the module is not installed, then automatically install it. Otherwise, continue the program
add_log('importing custom modules')
try:
    import colorama
    from colorama import Fore, Back, Style
    add_log('successfully imported colorama')
    colorama.init()
    colorama.init(convert=True)
    colorama.init(autoreset=True)
except:
    add_log('error importing colorama')
    print('You do not have the "colorama" module, we are installing it for you now...')
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
    print(Fore.RED+'You do not have the "pynput" module, we are installing it for you now...')
    pip.main(['install', 'tabulate'])
    pip.main(['install', 'pandas'])
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
    pip.main(['install', 'pynput'])
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
    with open('main/config.json', 'r') as jsonConfig:
        config = json.load(jsonConfig)
    internet_config = config['requirements']['internetRequired']

    if internet_config == True:
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
            json.dump(config, f, indent = 4, sort_keys=True)

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
    for item in range(1, 51):
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
        sleep(0.05)
    print('\n\nAnd that is why you should be careful what you click on!')

def download(url, filename):
    print(Fore.BLUE+'[*] Downloading '+filename+' from '+url)
    try:
        import requests
    except:
        pip.main(['install', 'requests'])
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

def sub_command_help(command):
    with open('main/master_command_list.json', 'r') as command_list:
        data = json.load(command_list)
    if 'sub_commands' in data[command]:
        print(Fore.GREEN+'The "{}" command has the following sub-commands\n'.format(Fore.WHITE+command+Fore.GREEN))
        for (subcmd, subcmd_des) in data[command]['sub_commands'].items():
            subcmd_tab = 30-len(subcmd)
            print(' '*3+Fore.BLUE+subcmd+' '*subcmd_tab+Fore.CYAN+subcmd_des)
    else:
        print(Fore.RED+'The "{}" command has no sub commands\n'.format(Fore.WHITE+command+Fore.RED))




# highler lower game command function
def base_command_admin(user_input, command_string):
    # calculate where the dash should be (if there is)
    expected_dash = user_input[len(command_string)+1:len(command_string)+2]
    # base command
    if user_input == command_string:
        print('admin command requires a sub command')
    # sub commands for command
    elif expected_dash == '-':
        # identify sub command
        sub_command = user_input[len(command_string)+2:len(user_input)]
        if sub_command == 'help':
            sub_command_help(command_string)
        elif sub_command == 'delmods':
            pip.main(['uninstall', 'colorama'])
            pip.main(['uninstall', 'pynput'])
            pip.main(['uninstall', 'tabulate'])
            pip.main(['uninstall', 'pandas'])
            pip.main(['uninstall', 'keyboard'])
            pip.main(['uninstall', 'requests'])
        else:
            print(Fore.RED+'The "-{}" sub command is invalid'.format(sub_command))
    # otherwise inform user that the command was identified, but had had a type
    else:
        invalid_command_ext(command_string, user_input)


# highler lower game command function
def base_command_download(user_input, command_string):
    # calculate where the dash should be (if there is)
    expected_dash = user_input[len(command_string)+1:len(command_string)+2]
    # base command
    if user_input == command_string:
        print('download command requires a sub command')
    # sub commands for command
    elif expected_dash == '-':
        # identify sub command
        sub_command = user_input[len(command_string)+2:len(user_input)]
        if sub_command == 'help':
            sub_command_help(command_string)
        elif sub_command == 'lu':
            download('https://github.com/shannon-nz/python-games/blob/main/main/games/luckyunicorn/Python%20Program%20Documentation.pptx?raw=true', 'luckyunicorn_documentation.pptx')
        else:
            print(Fore.RED+'The "-{}" sub command is invalid'.format(sub_command))
    # otherwise inform user that the command was identified, but had had a type
    else:
        invalid_command_ext(command_string, user_input)


# Help command function
def base_command_help(user_input, command_string):
    with open('main/master_command_list.json', 'r') as command_list:
        data = json.load(command_list)

    # calculate where the dash should be (if there is)
    expected_dash = user_input[len(command_string)+1:len(command_string)+2]
    # base command
    if user_input == command_string:
        print(Fore.GREEN+'Use the "'+Fore.WHITE+'-help'+Fore.GREEN+'" sub-command for any command to show more options')
        command_color = Fore.WHITE
        des_color = Fore.WHITE
        print()
        for (command, command_detail) in data.items():
            num = 30-len(command)
            tabs = ' '*num
            print(command_color+'   '+command+tabs+des_color+command_detail['brief_description'])
            #sub_commands = command_detail['sub_commands']
            if 'sub_commands' in data[command]:
                for (subcmd, subcmd_des) in command_detail['sub_commands'].items():
                    subcmd_tab = 30-len(subcmd)
                    print(' '*3+Fore.BLUE+subcmd+' '*subcmd_tab+Fore.CYAN+subcmd_des)
    # sub commands for command
    elif expected_dash == '-':
        # identify sub command
        sub_command = user_input[len(command_string)+2:len(user_input)]
        if sub_command == 'help':
            sub_command_help(command_string)
        elif sub_command == 'des':
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
            sub_command_help(command_string)
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
        if sub_command == 'help':
            sub_command_help(command_string)
        elif sub_command == 'clean':
            print('cleaning log...')
            myText = open(r'main/data.log','w')
            myText.write('<<< start of log >>>')
            myText.close()
            print('log cleaned!')
        elif sub_command == 'disable':
            with open('main/config.json', 'r') as jsonConfig:
                config = json.load(jsonConfig)
            config['user']['log'] = 'disabled'
            with open('main/config.json', 'w') as f:
                json.dump(config, f, indent = 4, sort_keys=True)
        elif sub_command == 'enable':
            with open('main/config.json', 'r') as jsonConfig:
                config = json.load(jsonConfig)
            config['user']['log'] = 'enabled'
            with open('main/config.json', 'w') as f:
                json.dump(config, f, indent = 4, sort_keys=True)
        elif sub_command == 'help':
            print('log definition')
        else:
            print(Fore.RED+'The "-{}" sub command is invalid'.format(sub_command))
    # otherwise inform user that the command was identified, but had had a type
    else:
        invalid_command_ext(command_string, user_input)

# highler lower game command function
def base_command_settings(user_input, command_string):
    # calculate where the dash should be (if there is)
    expected_dash = user_input[len(command_string)+1:len(command_string)+2]
    # base command
    if user_input == command_string:
        with open('main/config.json', 'r') as jsonConfig:
            config = json.dumps(json.load(jsonConfig), indent=4, sort_keys=True)
        print(Fore.YELLOW+config)
    # sub commands for command
    elif expected_dash == '-':
        # identify sub command
        sub_command = user_input[len(command_string)+2:len(user_input)]
        if sub_command == 'help':
            sub_command_help(command_string)
        elif sub_command == 'reset':
            print('This will reset the entire application and it\'s configurations\nAre you sure you want to reset? (y/n)', end='')
            verification_prompt = input('')
            if verification_prompt == 'yes' or verification_prompt == 'y':
                with open('main/config.json', 'r') as jsonConfig:
                    config = json.load(jsonConfig)
                    pass_prompt = input('Enter password: ')
                    if pass_prompt != config['user']['pass']:
                        print(Fore.RED+'Incorrect password')
                    else:
                        current_directory = os.path.dirname(__file__)
                        file_path = os.path.join(current_directory, 'main\\info', 'default_config.json')
                        with open(file_path, 'r') as jsonConfig:
                            default_config = json.load(jsonConfig)
                        with open('main/config.json', 'r') as jsonConfig:
                            config = json.load(jsonConfig)
                        with open('main/config.json', 'w') as f:
                            json.dump(default_config, f, indent=4, sort_keys=True)
                        add_log('settings have been reset')
                        add_log('restarting the application...')
                        screen_clear()
                        os.system('python app.py')
                        exit()
            else:
                print(Fore.RED+'You did not enter yes, exiting reset')

        else:
            print(Fore.RED+'The "-{}" sub command is invalid'.format(sub_command))
    # otherwise inform user that the command was identified, but had had a type
    else:
        invalid_command_ext(command_string, user_input)

# highler lower game command function
def base_command_shortcuts(user_input, command_string):
    # calculate where the dash should be (if there is)
    expected_dash = user_input[len(command_string)+1:len(command_string)+2]
    # base command
    if user_input == command_string:
        print()
        with open('main/master_shortcut_list.json', 'r') as shortcut_list:
            data = json.load(shortcut_list)
        # base command
        for shortcut, replaced in data.items():
            tabn = 30-len(shortcut)
            print(' '*3+Fore.BLUE+shortcut+' '*tabn+Fore.CYAN+replaced)
    # sub commands for command
    elif expected_dash == '-':
        # identify sub command
        sub_command = user_input[len(command_string)+2:len(user_input)]
        if sub_command == 'help':
            sub_command_help(command_string)
        else:
            print(Fore.RED+'The "-{}" sub command is invalid'.format(sub_command))
    # otherwise inform user that the command was identified, but had had a type
    else:
        invalid_command_ext(command_string, user_input)

def stats():
    return ''


# <<<<<<<<<<<<<<<<<<<< <<<<<<<<<< SCRIPT >>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>
check_internet_on_start()
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

with open('main/config.json', 'r') as command_list:
    data = json.load(command_list)
in_balance = data['user']['balance']
print(Fore.CYAN+'Your current balance is: '+Fore.RED+'${}'.format(in_balance))
if first_time == True:
    print(Fore.WHITE+'''
Welcome to python-games!
As this may be your first time using this application, this is just a reminder to make sure that you have 
read the documentation so you know how to use this app properly. Otherwise, you may run into some 
unexpected problems. Enjoy!                                                                            :D

''')
    from keyboard import press
    keyboard.write('doc')


print(Fore.GREEN+'Welcome to the main menu. Use a command or type "help" if you don\'t know any commands')





def activate_admin():
    print('admin activated')

keyboard.add_hotkey("alt+p", lambda: activate_admin)


# Function that contains all code for commands, some link to other functions
def command_line():
    idle_check()
    user_input = ''
    while user_input != 'quit':
        print(Back.BLUE+Style.DIM+'\nAs this application is still in development, not everything will work as expected.\nThis message will be removed from the program when production ready. So make sure to keep up here:')
        print(Back.BLUE+Style.DIM+'https://github.com/shannon-nz/python-games/')

        with open('main/config.json', 'r') as jsonConfig:
            config = json.load(jsonConfig)
            config_username = config['user']['username']
            print(Fore.RED+'\npy-games@'+config_username+Fore.WHITE+':'+Fore.BLUE+'~'+Fore.WHITE+'$ ', end='')
        
        user_input = input().lower()
      
        # check if this is the valid command
        if user_input[0:len('admin')] == 'admin':
            base_command_admin(user_input, 'admin')

        elif user_input == 'cls':
            screen_clear()

        elif user_input == 'doc':
            print(Fore.BLUE+'Opening python games documentation')
            import webbrowser
            webbrowser.open('https://github.com/shannon-nz/python-games#-python-games-in-development-')

        # check if this is the valid command
        elif user_input[0:len('download')] == 'download':
            base_command_download(user_input, 'download')

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
            print(Fore.BLUE+'Opening shannon.rf.gd in default browser')
            import webbrowser
            webbrowser.open('https://www.shannon.rf.gd/')

        elif user_input == 'quit':
            print(Fore.RED+'quiting application...')
            exit()

        elif user_input == 'restart' or user_input == '/r':
            add_log('restarting application...')
            os.system('python app.py')
            exit()

        elif user_input == 'rps':
            print(Fore.BLUE+'Opening Rock Paper Scissors Game...')
            sleep(1)
            os.system('python main/games/rock-paper-scissors/app.py')

        # check if this is the valid command
        elif user_input[0:len('settings')] == 'settings':
            base_command_settings(user_input, 'settings')
        # shortcut
        elif user_input[0:len('/s')] == '/s':
            base_command_settings(user_input, '/s')

        # check if this is the valid command
        elif user_input[0:len('shortcuts')] == 'shortcuts':
            base_command_shortcuts(user_input, 'shortcuts')

        elif user_input == 'spaz':
            spaz_screen()

        elif user_input == 'stats':
            # creating a DataFrame
            with open('main/config.json', 'r') as command_list:
                data = json.load(command_list)
            balance = data['user']['balance']
            dict = {'Stats':['Connected to Internet', 'Balance'],
                    'Result':[
                        check_internet_connection(),
                        '${}'.format(balance)
                    ]}
            df = pd.DataFrame(dict)
            # displaying the DataFrame
            print(tabulate(df, headers = 'keys', tablefmt = 'psql'))

        # Display all system information
        elif user_input == 'system':
            print(Fore.BLUE+'Opening python file for "system information"...')
            os.system('python main/info/system.py')

        elif user_input == 'hello':
            print('Oh, hello! What would you like me to do for you today?')

        elif user_input == 'custom_command':
            with open('main/config.json', 'r') as jsonConfig:
                config = json.load(jsonConfig)
                config_username = config['username']
        else:
            print('Sorry, "{}" '.format(user_input)+Fore.RED+'is an invalid command')
            add_log('{} is an invalid command'.format(user_input))
command_line()
