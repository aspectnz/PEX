PYTHONDONTWRITEBYTECODE=1

print(
'''

█░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀ ░ ░ ░
█▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█ ▄ ▄ ▄

PLEASE WAIT A SECOND
''')

imported_modules = False

import sys
sys.path.insert(0, './main/custom_modules')
import default as default


try:
    import json
    default.add_log('successfully imported json')
except:
    default.add_log('failed to import json')

try:
    import socket
    default.add_log('successfully imported socket')
except:
    default.add_log('failed to import socket')

h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)

try:
    from datetime import datetime
    default.add_log('successfully imported datetime')
except:
    default.add_log('failed to import datetime')

first_time = False
config_username = 'root'
with open('main/config.json', 'r') as jsonConfig:
    config = json.load(jsonConfig)
    if config['user']['username'] == 'root':
        first_time = True
        default.add_log('user has not established login details')
        print('Welcome, first make a username. Something short and easy to remember! ')
        while config['user']['username'] == 'root':
            username_prompt = input('Enter username: ')
            
            if username_prompt == 'root':
                print('root is a reserved username, please try something else')
            elif username_prompt == '' or username_prompt == ' ':
                print('please enter a valid username, not blank space')
            else:
                default.add_log('user set new username to '+username_prompt)
                config['user']['username'] = username_prompt
                with open('main/config.json', 'w') as f:
                    json.dump(config, f, indent=4, sort_keys=True)

def add_dislog(text):
    with open('main/config.json', 'r') as jsonConfig:
        config = json.load(jsonConfig)
        if config['options']['log'] == 'enabled':
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            with open('main/data.log', 'a') as file_object:
                file_object.write('\n'+dt_string+' - '+h_name+'('+IP_addres+')'+': '+text.lower())

def clean_cache():
    os.system('python -Bc "import pathlib; [p.unlink() for p in pathlib.Path(\'.\').rglob(\'*.py[co]\')]"')
    os.system('python -Bc "import pathlib; [p.rmdir() for p in pathlib.Path(\'.\').rglob(\'__pycache__\')]"')

# <<<<<<<<<<<<<<<<<<<< <<<<<<<<<< IMPORTS >>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>
default.add_log('importing default modules')

try:
    import random
    default.add_log('successfully imported random')
except:
    default.add_log('failed to import random')

try:
    import os
    default.add_log('successfully imported os')
except:
    default.add_log('failed to import os')

try:
    import subprocess
    from subprocess import *
    default.add_log('successfully imported subprocess')
except:
    default.add_log('failed to import subprocess')

try:
    import ctypes
    default.add_log('successfully imported ctypes')
except:
    default.add_log('failed to import ctypes')

try:
    import pip
    default.add_log('successfully imported pip')
except:
    default.add_log('failed to import pip')

try:
    import enum
    default.add_log('successfully imported enum')
except:
    default.add_log('failed to import enum')

try:
    import winsound
    default.add_log('successfully imported winsound')
except:
    default.add_log('failed to import winsound')

try:
    from time import sleep
    default.add_log('successfully imported sleep')
except:
    default.add_log('failed to import sleep')

try:
    from threading import Thread
    default.add_log('successfully imported thread')
except:
    default.add_log('failed to import thread')

default.add_log('Importing custom modules')
# Import numpy module
# If the module is not installed, then automatically install it. Otherwise, continue the program
try:
    default.add_log('importing numpy')
    import numpy
    default.add_log('successfully imported numpy')
except:
    default.add_log('error importing numpy')
    print('You do not have the "numpy" module, we are installing it for you now...')
    pip.main(['install', 'numpy'])
    import numpy
    default.add_log('installed and imported numpy successfully')

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

# Import pandas and tabulate module
# If the module is not installed, then automatically install it. Otherwise, continue the program
try:
    default.add_log('importing tabulate')
    from tabulate import tabulate
    default.add_log('successfully imported tabulate')
    default.add_log('importing pandas')
    import pandas as pd
    default.add_log('successfully imported pandas')
except:
    default.add_log('error importing pandas or tabulate')
    print(Fore.RED+'You do not have the "tabulate" module, we are installing it for you now...')
    pip.main(['install', 'tabulate'])
    pip.main(['install', 'pandas'])
    # importing the modules
    default.add_log('importing tabulate')
    from tabulate import tabulate
    default.add_log('importing pandas')
    import pandas as pd
    default.add_log('installed and imported pandas and tabulate successfully')


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


# import the playsound module
try:
    default.add_log('importing playsound')
    from playsound import playsound
    default.add_log('successfully imported playsound')
except:
    default.add_log('failed to import playsound')
    print(Fore.RED+'we are installing it for you now')
    pip.main(['install','playsound'])
    default.add_log('successfully imported playsound')

# <<<<<<<<<<<<<<<<<<<< <<<<<<<<<< FUNCTIONS >>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>
default.add_log('declaring functions')

default.add_log('greeting function')
def greeting():
    print(Fore.GREEN+
        '''
    ██████╗░███████╗██╗░░██╗
    ██╔══██╗██╔════╝╚██╗██╔╝
    ██████╔╝█████╗░░░╚███╔╝░
    ██╔═══╝░██╔══╝░░░██╔██╗░
    ██║░░░░░███████╗██╔╝╚██╗
    ╚═╝░░░░░╚══════╝╚═╝░░╚═╝
        ''')
    # move users mouse to top right
    mouse.position = (1000*10, 50)
    print(Fore.BLUE+'Your mouse has been moved to the top right.')
    with open('main/config.json', 'r') as command_list:
        data = json.load(command_list)
    in_balance = data['user']['balance']
    print(Fore.CYAN+'Your current balance is: '+Fore.RED+'${}'.format(in_balance))
    if first_time == True:
        print(Fore.WHITE+'''
    Welcome to PEX!
    As this may be your first time using this application, this is just a reminder to make sure that you have 
    read the documentation so you know how to use this app properly. Otherwise, you may run into some 
    unexpected problems. Enjoy!

    ''')
        from keyboard import press
        keyboard.write('doc')
    print(Fore.GREEN+'Welcome to the main menu. Use a command or type "help" if you don\'t know any commands')
    print(Back.BLUE+Style.DIM+'\nAs this application is still in development, not everything will work as expected.\nThis message will be removed from the program when production ready. So make sure to keep up to date on GitHub:')
    print(Fore.BLUE+'https://github.com/shannon-nz/PEX/')

default.add_log('check python version function')
def check_py_version():
    default.add_log('Validating python version')
    if sys.version_info[0] < 3:
        default.add_logdis('python version is less than 3')
        print('Your python version is not up to date, please make sure that you are running python3 or later.')
        default.add_log('Exiting program in 10s...')
        sleep(10)
        exit()

default.add_log('idle check function')
def idle_check():
    add_dislog('Validating enviroment')
    with open('main/config.json', 'r') as jsonConfig:
        config = json.load(jsonConfig)
    terminal_required = config['requirements']['terminal']

    if terminal_required == True:
        add_dislog('The current enviroment is Terminal')
        sys.path.insert(0, './main/custom_modules')
        import idle_check as idle_check
        idle_check.run()
    else:
        add_dislog('Terminal requirement is disabled')

default.add_log('check internet connection function')
def check_internet_connection():
    try:
        # connect to the host -- tells us if the host is actually reachable
        socket.create_connection(("1.1.1.1", 443))
        return True
    except OSError:
        return False

default.add_log('check internet connection on start function')
def check_internet_on_start():
    with open('main/config.json', 'r') as jsonConfig:
        config = json.load(jsonConfig)
    internet_config = config['requirements']['internet']

    if internet_config == True:
        if(check_internet_connection() == True):
            default.add_log('connected to the internet')
        else:
            default.add_log('not connected to the internet')
            print('''
    Not connected to the internet
    Please make sure that you are connected to the internet or that ports 53 and 443 are enabled
    Exiting program in 10 seconds ...
                ''')
            sleep(10)
            exit()

default.add_log('get users platform function')
def get_platform():
    # making a dictionary for the list of OSs
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]

default.add_log('check the users platform on start function')
def check_platform_on_start():
    if get_platform() != 'Windows':
        add_dislog('Windows is not the default OS, exiting program(10s)...')
        print('''
You are not using windows
Please make sure that you are using windows 10
Exiting program in 10 seconds...
            ''')
        sleep(10)
        exit()
    else:
        add_dislog('Windows is the default OS')

default.add_log('startup sound function')
def startup_sound():
    print(Fore.BLUE+'WELCOME TO PEX')
    print(Fore.BLUE+'Making sure that everything is ready...')
    playsound('main/music/startup.mp3')


# function to clear the screen with cmd command
default.add_log('clear screen function')
def screen_clear():
    default.add_log('clearing screen...')
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')

default.add_log('change terminal background function')
def change_terminal_background(value):
    # change the default background and fore color for the terminal
    os.system('color '+value)
    default.add_log('changed theme to "{}"'.format(value))

default.add_log('modify config.json values function')
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


    

default.add_log('download function')
def download(url, filename):
    # os.path.exists("/home/el/myfile.txt"
    # if the downloads folder does not exist, create one
    if os.path.isdir('downloads') == False:
        default.add_log('downloads folder is missing')
        os.system('mkdir downloads')
        default.add_log('created downloads folder')
    print(Fore.BLUE+'[*] Downloading '+filename+' from '+url)
    default.add_log('importing requests')
    try:
        import requests
        default.add_log('successfully imported requests')
    except:
        default.add_log('error importing requests')
        print(Fore.RED+'You do not have the "requests" module, we are installing it for you now...')
        pip.main(['install', 'requests'])
        import requests
        default.add_log('successfully installed requests')
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
# when the command is valid but contains additional invalid text
default.add_log('invalud command function')

default.add_log('sub-command help function')
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

default.add_log('sub-command error function')
def sub_command_error(sub_command):
    print(Fore.RED+'The "{}" sub command is invalid'.format(Fore.WHITE+'-'+sub_command+Fore.RED))

# admin command function
default.add_log('admin command function')
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
            sub_command_error(sub_command)
    # otherwise inform user that the command was identified, but had had a type
    else:
        invalid_command_ext(command_string, user_input)


# download command function
default.add_log('download command function')
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
            download('https://github.com/shannon-nz/pex/blob/main/main/games/luckyunicorn/Python%20Program%20Documentation.pptx?raw=true', 'luckyunicorn_documentation.pptx')
        else:
            sub_command_error(sub_command)
    # otherwise inform user that the command was identified, but had had a type
    else:
        invalid_command_ext(command_string, user_input)


# music command function
default.add_log('music command function')
def base_command_music(user_input, command_string):
    # calculate where the dash should be (if there is)
    expected_dash = user_input[len(command_string)+1:len(command_string)+2]
    # base command
    if user_input == command_string:
        print('This command requires a sub-command (i.e, "music -moveit")')
    # sub commands for command
    elif expected_dash == '-':
        # identify sub command
        sub_command = user_input[len(command_string)+2:len(user_input)]
        if sub_command == 'help':
            sub_command_help(command_string)
        elif sub_command == 'moveit':
            default.add_log('Playing "I like to move it')
            playsound('main/music/iliketomoveit.mp3')
        else:
            sub_command_error(sub_command)
    # otherwise inform user that the command was identified, but had had a type
    else:
        invalid_command_ext(command_string, user_input)

# highler lower game command function
default.add_log('higher/lower game function')
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
            sub_command_error(sub_command)
    # otherwise inform user that the command was identified, but had had a type
    else:
        invalid_command_ext(command_string, user_input)

# log command function
default.add_log('log command function')
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
            config['options']['log'] = 'disabled'
            with open('main/config.json', 'w') as f:
                json.dump(config, f, indent = 4, sort_keys=True)
        elif sub_command == 'enable':
            with open('main/config.json', 'r') as jsonConfig:
                config = json.load(jsonConfig)
            config['options']['log'] = 'enabled'
            with open('main/config.json', 'w') as f:
                json.dump(config, f, indent = 4, sort_keys=True)
        elif sub_command == 'help':
            print('log definition')
        else:
            sub_command_error(sub_command)
    # otherwise inform user that the command was identified, but had had a type
    else:
        invalid_command_ext(command_string, user_input)

# settings command function
default.add_log('settings command function')
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
        if sub_command == 'disreq -internet':
            with open('main/config.json', 'r') as jsonConfig:
                config = json.load(jsonConfig)
            config['requirements']['internet'] = False
            with open('main/config.json', 'w') as f:
                        json.dump(default_config, f, indent=4, sort_keys=True)

        elif sub_command == 'help':
            sub_command_help(command_string)

        elif sub_command == 'pass':
            with open('main/config.json', 'r') as jsonConfig:
                config = json.load(jsonConfig)
                pass_prompt = input('Enter password: ')
                if pass_prompt != config['user']['pass']:
                    print(Fore.RED+'Incorrect password')
                else:
                    # function to change the password here >>>>>>>>>>>>>>>>>>>>>>>>>>>
                    current_directory = os.path.dirname(__file__)
                    file_path = os.path.join(current_directory, 'main\\info', 'default_config.json')
                    with open(file_path, 'r') as jsonConfig:
                        default_config = json.load(jsonConfig)
                    with open('main/config.json', 'r') as jsonConfig:
                        config = json.load(jsonConfig)
                    with open('main/config.json', 'w') as f:
                        json.dump(default_config, f, indent=4, sort_keys=True)
                    default.add_log('settings have been reset')
                    default.add_log('restarting the application...')
                    screen_clear()
                    os.system('python app.py')
                    exit()
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
                        default.add_log('settings have been reset')
                        default.add_log('restarting the application...')
                        screen_clear()
                        os.system('python app.py')
                        exit()
            else:
                print(Fore.RED+'You did not enter yes, exiting reset')

        else:
            sub_command_error(sub_command)
    # otherwise inform user that the command was identified, but had had a type
    else:
        invalid_command_ext(command_string, user_input)

# shortcuts command function
default.add_log('shortcuts command function')
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
            sub_command_error(sub_command)
    # otherwise inform user that the command was identified, but had had a type
    else:
        invalid_command_ext(command_string, user_input)

default.add_log('stats command function')
def stats():
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

default.add_log('activate command function')
def activate_admin():
    print('admin activated')

# function that contains all code for commands, some link to other functions - this must always be the last command
default.add_log('command line function')

# change the recursive limit
sys.setrecursionlimit(501)
print('the recursive limit is {}'.format(501))

command_line_count = 0

def command_line():
    global command_line_count
    command_line_count += 1
    if command_line_count > 500:
        print(Fore.RED+'command line has been run over 500 times, re-running')
        command_line_count = 0
        command_line()
    # check the user is using terminal
    idle_check()
    # default values before prompt
    user_input = ''
    last_error = False
    first_prompt = True
    while user_input != 'quit':
        # open the config.json file and print the username before the input like pex@username:~$
        with open('main/config.json', 'r') as jsonConfig:
            config = json.load(jsonConfig)
            config_username = config['user']['username']
            # print before input
            print(Fore.RED+'\npex@'+config_username+Fore.WHITE+':'+Fore.BLUE+'~'+Fore.WHITE+'$ ', end='')

        # check if this is the first prompt
        # if so, then don't play the sound, otherwise play the enter sound or error sound, dependant on the last input
        if first_prompt != True:
            if last_error == True:
                playsound('main/music/error.wav')
                last_error = False
            else:
                playsound('main/music/enter.wav')
        first_prompt = False

        # get the users input
        user_input = input().lower()

        if user_input == '' or user_input == ' ':
            print(Fore.BLUE+'nothing does nothing :)')
            command_line()
      
        # admin command - gives the user admin access
        elif user_input[0:len('admin')] == 'admin':
            base_command_admin(user_input, 'admin')

        # clear screen command - clears the terminal
        elif user_input == 'cls':
            screen_clear()
        elif user_input == 'cls -help':
            print('The cls command will clear the terminal')

        # cmd command - run any cmd command that follows after "cmd "
        elif user_input == 'cmd -help':
            print('The cmd command will allow you to run normal cmd commands within PEX (i.e, "cmd dir")')
        elif user_input[0:4] == 'cmd ':
            user_input = user_input[4:len(user_input)]
            default.add_log('running {} command in cmd'.format(user_input))
            os.system(user_input)

        # documentation command - opens the PEX documentation in the default web browser
        elif user_input == 'doc':
            print(Fore.BLUE+'Opening PEX documentation')
            import webbrowser
            webbrowser.open('https://github.com/shannon-nz/PEX#-python-games-in-development-')
        elif user_input == 'doc -help':
            print('The doc command will open the documentation in your default browser')

        # downloads anything from the internet that is specified in the program
        elif user_input[0:len('download')] == 'download':
            base_command_download(user_input, 'download')

        # echo command - prints the text that follows after "echo " onto the screen
        elif user_input == 'echo -help':
            print('The echo command will print out any text that follows after "echo "')
        elif user_input[0:5] == 'echo ':
            if user_input.find('*') != -1:
                restriction_num = 6
                num = int(user_input[user_input.find('*')+1:len(user_input)])
                if len(user_input[user_input.find('*')+1:len(user_input)]) < restriction_num:
                    print(user_input*num)
                else:
                    print('number must be below 100,000')
            else:
                user_input = user_input[5:len(user_input)]
                print(user_input)

        # music command - plays music defined in the sub-command
        elif user_input[0:len('music')] == 'music':
            base_command_music(user_input, 'music')

        # help command - displays different sets of commands dependant on the sub-command (if any)
        elif user_input[0:len('help')] == 'help':
            sys.path.insert(0, './main/command')
            import c_help as c_help
            c_help.base_command_help(user_input, 'help')

        # hl command - plays the higher/lower game
        elif user_input[0:len('hl')] == 'hl':
            base_command_hl(user_input, 'hl')

        # log command - displays all the logs or configures it with sub-commands
        elif user_input[0:len('log')] == 'log':
            base_command_log(user_input, 'log')

        elif user_input == 'lu':
            print(Fore.BLUE+'Opening Lucky Unicorn Game...')
            sleep(1)
            os.system('python main/games/luckyunicorn/00_LU_Base_v_01.py')

        # profile command - opens profile website in default browser
        elif user_input == 'profile':
            print(Fore.BLUE+'Opening shannon.rf.gd in default browser')
            import webbrowser
            webbrowser.open('https://www.shannon.rf.gd/')

        # quit command - quits the application
        elif user_input == 'quit':
            print(Fore.RED+'quiting application...')
            exit()

        # restart command - restarts the application
        elif user_input == 'restart' or user_input == '/r':
            default.add_log('restarting application...')
            os.system('python app.py')
            exit()

        # rps command - plays the rock paper scissors game
        elif user_input == 'rps':
            print(Fore.BLUE+'Opening Rock Paper Scissors Game...')
            sleep(1)
            os.system('python main/games/rock-paper-scissors/app.py')

        # settings command - displays settings plus other features with sub-commands
        elif user_input[0:len('settings')] == 'settings':
            base_command_settings(user_input, 'settings')
        # shortcut for settings command
        elif user_input[0:len('/s')] == '/s':
            base_command_settings(user_input, '/s')

        # shortcuts command - displays the available shortcuts
        elif user_input[0:len('shortcuts')] == 'shortcuts':
            base_command_shortcuts(user_input, 'shortcuts')

        # spaz command - spazes the users screen
        elif user_input == 'spaz':
            sys.path.insert(0, './main/command')
            import c_spaz as c_spaz
            c_spaz.base_command_spaz()

        # stats command - displays current statistics
        elif user_input == 'stats':
            stats()

        # system command - displays system information
        elif user_input == 'system':
            print(Fore.BLUE+'Opening python file for "system information"...')
            os.system('python main/info/system.py')

        # update pex with the 'git pull' command - only works if git is installed
        elif user_input == 'update':
            default.add_log('Updating PEX ')
            try:
                # use the git pull command
                os.system('git pull')
            except:
                # inform user if git is not installed
                print('You must have git installed on your computer first.')

        # instead of using the git application, install in the downloads folder using the gitpython module
        elif user_input == 'update -reset':
            default.add_log('removing PEX folder if possible')
            os.system('rmdir /s downloads/PEX')
            default.add_log('Updating PEX')
            try:
                # import git python
                from git import Repo
            except:
                # install and import gitpython
                pip.main(['install','gitpython'])
                from git import Repo
            # clone pex
            Repo.clone_from('https://github.com/shannon-nz/pex','downloads/PEX')
            # output when cloning is complete
            default.add_log('Update complete')
            print('You can find the latest version in the downloads folder named PEX')

        elif user_input == 'update -clean':
            default.add_log('removing reset update')
            os.system('rmdir /s downloads\\PEX')

        # run a custom command
        elif user_input == 'custom_command':
            # open the config.json file
            with open('main/config.json', 'r') as jsonConfig:
                config = json.load(jsonConfig)
                # get the username
                config_username = config['username']

        # if the last 2 characters of the command are ():
        elif user_input[len(user_input)-2:len(user_input)] == '()':
            # remove () from the end of the command
            user_input = user_input[0:len(user_input)-2]
            # command is not yet available
            print(Fore.RED+'The '+Fore.WHITE+user_input+Fore.RED+' function cannot be run via the command line at the moment')

        #elif user_input.find('a') != -1:
            #print('I found a')

        # if the user entered an invalid command, inform them and play the error sound
        else:
            default.add_log(Fore.WHITE+'"'+user_input+'"'+Fore.RED+' is an invalid command'+Fore.WHITE)
            last_error = True


# <<<<<<<<<<<<<<<<<<<< <<<<<<<<<< SCRIPT >>>>>>>>>> >>>>>>>>>>>>>>>>>>>>>
# this section contains the ordered set of functions being called
default.add_log('running script...')
# clean the cache - delete __pycache__ if it is there
clean_cache()
# check if the python version is valid for this program
check_py_version()
# check if the user is using idle or terminal
idle_check()
# check if the user is connected to the internet. If the config file reads required, then exit the program.
check_internet_on_start()
# check if the user is using Windows or not, exit the program if not
check_platform_on_start()
# simultaneously run the clear screen function and play the start up sound
if __name__ == '__main__':
    Thread(target = screen_clear).start()
    Thread(target = startup_sound).start()
# clear the screen again
screen_clear()
# greet the user with printed text - extra text if it is their first time
greeting()

# << shortcuts >>
# admin shortcut
keyboard.add_hotkey("shift+alt+p", lambda: activate_admin())

# run the command line function - contains the main set of code which links to other functions
command_line()
# once the program has finished, then clear the cache - won't work if the quit command or something that uses the quit command is used
clean_cache()