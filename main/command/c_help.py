import sys
def add_log(text):
    print(text)
    sys.path.insert(0, './main/custom_modules')
    import add_log as add_log
    add_log.run(text)

import json
# Import colorama module
# If the module is not installed, then automatically install it. Otherwise, continue the program
try:
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()
    colorama.init(convert=True)
    colorama.init(autoreset=True)
except:
    add_log('error importing colorama')
    print('You do not have the "colorama" module, we are installing it for you now...')
    pip.main(['install', 'colorama'])
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()
    colorama.init(convert=True)
    colorama.init(autoreset=True)
    add_log('installed and imported colorama successfully')

def invalid_command_ext(command_string, user_input):
    invalid_text = user_input[len(command_string):len(user_input)]
    print(Fore.RED+'The "{}" command was identified, but contained invalid text "{}"'.format(command_string, invalid_text))



# Help command function
def base_command_help(user_input, command_string):
    with open('main/master_command_list.json', 'r') as command_list:
        data = json.load(command_list)

    # calculate where the dash should be (if there is)
    expected_dash = user_input[len(command_string)+1:len(command_string)+2]
    # Default colors for etxt sets
    command_color = Fore.WHITE
    des_color = Fore.WHITE
    # base command
    if user_input == command_string:
        print(Fore.GREEN+'Use the "'+Fore.WHITE+'-help'+Fore.GREEN+'" sub-command for any command to show more options')
        print(Fore.GREEN+'Or use "'+Fore.WHITE+'help -all'+Fore.GREEN+'" to show the full list of commands and sub-commands')
        print()
        for (command, command_detail) in data.items():
            num = 30-len(command)
            tabs = ' '*num
            print(command_color+'   '+command+tabs+des_color+command_detail['brief_description'])
    # sub commands for command
    elif expected_dash == '-':
        # identify sub command
        sub_command = user_input[len(command_string)+2:len(user_input)]
        if sub_command == 'help':
            sub_command_help(command_string)
        elif sub_command == 'all':
            for (command, command_detail) in data.items():
                num = 30-len(command)
                tabs = ' '*num
                print(command_color+'   '+command+tabs+des_color+command_detail['brief_description'])
                # Retrieve and print sub-commands
                if 'sub_commands' in data[command]:
                    for (subcmd, subcmd_des) in command_detail['sub_commands'].items():
                        subcmd_tab = 30-len(subcmd)
                        print(' '*3+Fore.BLUE+subcmd+' '*subcmd_tab+Fore.CYAN+subcmd_des)
        elif sub_command == 'sub':
            for (command, command_detail) in data.items():
                # Retrieve and print sub-commands
                if 'sub_commands' in data[command]:
                    for (subcmd, subcmd_des) in command_detail['sub_commands'].items():
                        subcmd_tab = 30-len(subcmd)
                        print(' '*3+Fore.BLUE+subcmd+' '*subcmd_tab+Fore.CYAN+subcmd_des)
        elif sub_command == 'des':
            print('sub command was correctly des')
        else:
            print(Fore.RED+'The "-{}" sub command is invalid'.format(sub_command))
    # otherwise inform user that the command was identified, but had had a type
    else:
        invalid_command_ext(command_string, user_input)