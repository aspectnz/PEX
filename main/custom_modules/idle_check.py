

import subprocess
from subprocess import *
def run():
    import sys
    #from time import sleep
    idle_check = "idlelib" in sys.modules
    if(idle_check == True):
        print("Your are not using the terminal, this program will work better in the terminal.")
        print('Opening program in terminal in 0 seconds  ...')
        subprocess.call('python app.py', creationflags=subprocess.CREATE_NEW_CONSOLE)