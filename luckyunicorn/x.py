import sys
import os
colorama_install = ''
# Import Colorama Module
# If colorama is not installed, then ask the user if they want to install it
while colorama_install.lower() != 'installed':
    try:
        import colorama
        colorama.init()
        colorama.init(convert=True)
        from colorama import Fore, Back, Style
        colorama_install = 'installed';
    except ImportError:
        print('Error, Module colorama is required')
        prompt_install_colorama = input('Would you like to install colorama? (y/n): ').lower();
        if prompt_install_colorama == 'yes' or prompt_install_colorama == 'y':
            import pip
            failed = pip.main(['install', 'colorama'])
        elif prompt_install_colorama == 'no' or prompt_install_colorama == 'n':
            print('The program is unable to run without colorama, exiting program')
            quit()
        else:
            print('Invalid Input, please answer yes/y or no/n')
            prompt_install_colorama = input('Would you like to install colorama? (y/n): ');



# Checking if the user is running the program in idle or in the terminal
# If running in idle, take the user through the process of how to run in the terminal or allow them to run it in idle.
idle_check = "idlelib" in sys.modules;
if idle_check == True:
    print('It appears that you are using Idle to run this program, although the program is optimised for running in the terminal.')
    run_in_idle = input('Do you want to force run the program in idle? (y/n/?): ')
    if run_in_idle == 'y':
        print('The script will continue')
    elif run_in_idle == 'n':
        print('Great Choice! You may close this window and run the script in your terminal.')
        print('If you need help with this')
        quit()
    elif run_in_idle == '?':
        try:
            print('Opening "https://howchoo.com/python/run-python-terminal"')
            import webbrowser
            webbrowser.open('https://howchoo.com/python/run-python-terminal')
            print('Exiting the program...')
            quit()
        except ImportError:
            print('There was an error opening the link');
            print('Paste this into your browser: https://howchoo.com/python/run-python-terminal')
    else:
      print('Please choose a valid option "yes", "no", or "?" to learn how')

else:
    print('Thanks for running the program in your Terminal')


text = "The quick brown fox jumps over the lazy dog"

show_instructions = ''
while show_instructions != 'xxx':

    # Ask the user if they have played before
    print(Fore.RED+Style.DIM+'Have you played this game before?')
    print(Fore.WHITE+'')
    show_instructions = input('(y/n): ').lower()

    # If they say yes, output 'program continues'
    # If they say no, output 'display instructions'
    # If the answer is invalid, print an error

    if show_instructions == 'yes' or show_instructions == 'y':
            print(Fore.BLUE+'You chose "Yes", continuing program.\n')

    elif show_instructions == 'no' or show_instructions == 'n':
            print(Fore.BLUE+'You chose "No", displaying instructions.\n')

    else:
            print(Fore.BLUE+'Please answer with yes/y or no/n.')