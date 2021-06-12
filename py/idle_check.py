def run():
    import sys
    from time import sleep
    idle_check = "idlelib" in sys.modules
    if(idle_check == True):
        print("Your are not using the terminal, this program will work better in the terminal.")
        print('Please double click on the app.py file to run it in the terminal or access it manually from the manual if you know how.')
        print('Exiting the program in 10s...')
        sleep(10)
        exit()