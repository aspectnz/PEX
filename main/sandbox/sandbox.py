def import_colorama(): 
    # Import colorama module
    # If the module is not installed, then automatically install it. Otherwise, continue the program
    try:
        import colorama
        colorama.init()
        colorama.init(convert=True)
        colorama.init(autoreset=True)
        from colorama import Fore, Back, Style
    except:
        print('You do not have the "colorama" module, we are installing it for you now...')
        import pip
        pip.main(['install', 'colorama'])
        import colorama
        colorama.init()
        colorama.init(convert=True)
        colorama.init(autoreset=True)
        from colorama import Fore, Back, Style
import_colorama()

print(Fore.RED+'ayayayayayayayaya')
input('hello')