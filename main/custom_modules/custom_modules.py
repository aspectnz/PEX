def imports():
    # Import colorama module
    # If the module is not installed, then automatically install it. Otherwise, continue the program
    return 'importing custom modules'
    try:
        import colorama
        from colorama import Fore, Back, Style
        colorama.init()
        colorama.init(convert=True)
        colorama.init(autoreset=True)
        return 'successfully imported colorama'
    except:
        return 'error importing colorama'
        print('You do not have the "colorama" module, we are installing it for you now...')
        import pip
        pip.main(['install', 'colorama'])
        import colorama
        from colorama import Fore, Back, Style
        colorama.init()
        colorama.init(convert=True)
        colorama.init(autoreset=True)
        return 'installed and imported colorama successfully'
    

    # Import pandas and tabulate module
    # If the module is not installed, then automatically install it. Otherwise, continue the program
    try:
        # importing the modules
        from tabulate import tabulate
        import pandas as pd
        return 'successfully imported pandas and tabulate'
    except:
        return 'error importing pandas or tabulate'
        import pip
        print(Fore.RED+'You do not have the "tabulate" module, we are installing it for you now...')
        pip.main(['install', 'tabulate'])
        # importing the modules
        from tabulate import tabulate
        import pandas as pd
        return 'installed and imported pandas and tabulate successfully'



    # Import pynput module
    # If the module is not installed, then automatically install it. Otherwise, continue the program
    try:
        from pynput.mouse import Button, Controller
        mouse = Controller()
        mouse.position = (0, 0)
        print(Fore.BLUE+'Your mouse has been moved to the top left.')
        return 'successfully imported pynput'
    except:
        return 'error importing pynput'
        import pip
        print(Fore.RED+'You do not have the "pynput" module, we are installing it for you now...')
        pip.main(['install', 'pynput'])
        #from pynput.keyboard import Key, Controller
        from pynput.mouse import Button, Controller
        from pynput import mouse
        return 'installed and imported pynput successfully'

    # Import keyboard module
    # If the module is not installed, then automatically install it. Otherwise, continue the program
    try:
        import keyboard
        keyboard.press('win+up')
        keyboard.release('win+up')
        return 'successfully imported keyboard'

    except:
        return 'error importing keyboard'
        import pip
        print(Fore.RED+'You do not have the "keyboard" module, we are installing it for you now...')
        pip.main(['install', 'keyboard'])
        import keyboard
        keyboard.press('win+up')
        keyboard.release('win+up')
        return 'installed and imported keyboard successfully'
    cus_imported_bool = True