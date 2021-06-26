# Function that contains all code for commands, some link to other functions
def command_line():
    idle_check()
    user_input = ''
    while user_input != 'quit':
        print(Back.BLUE+Style.DIM+'\nAs this application is still in development, not everything will work as expected.\nThis message will be removed from the program when production ready. So make sure to keep up to date on GitHub:')
        print(Fore.BLUE+'https://github.com/shannon-nz/PEX/')

        with open('main/config.json', 'r') as jsonConfig:
            config = json.load(jsonConfig)
            config_username = config['user']['username']
            print(Fore.RED+'\npex@'+config_username+Fore.WHITE+':'+Fore.BLUE+'~'+Fore.WHITE+'$ ', end='')
        
        
        '''
        with Listener(
            on_release=on_release) as listener:
                listener.join()
        '''

        user_input = input().lower()
      
        # check if this is the valid command
        if user_input[0:len('admin')] == 'admin':
            base_command_admin(user_input, 'admin')

        elif user_input == 'cls':
            screen_clear()

        elif user_input == 'doc':
            print(Fore.BLUE+'Opening PEX documentation')
            import webbrowser
            webbrowser.open('https://github.com/shannon-nz/PEX#-python-games-in-development-')

        # check if this is the valid command
        elif user_input[0:len('download')] == 'download':
            base_command_download(user_input, 'download')

        elif user_input == 'move-it':
            default.add_log('Playing "I like to move it')
            playsound('main/music/iliketomoveit.mp3')

        # check if this is the valid command
        elif user_input[0:len('help')] == 'help':
            sys.path.insert(0, './main/command')
            import c_help as c_help
            c_help.base_command_help(user_input, 'help')

        # check if this is the valid command
        elif user_input[0:len('hl')] == 'hl':
            base_command_hl(user_input, 'hl')

        # check if this is the valid command
        elif user_input[0:len('log')] == 'log':
            base_command_log(user_input, 'log')

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
            default.add_log('restarting application...')
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

        elif user_input == 'update':
            default.add_log('Updating PEX ')
            try:
                os.system('git pull')
            except:
                print('You must have git installed on your computer first.')

        elif user_input == 'update -reset':
            default.add_log('removing PEX folder if possible')
            os.system('rmdir /s downloads/PEX')
            default.add_log('Updating PEX')
            try:
                from git import Repo
            except:
                pip.main(['install','gitpython'])
                from git import Repo

            Repo.clone_from('https://github.com/shannon-nz/pex','downloads/PEX')

            default.add_log('Update complete')
            print('You can find the latest version in the downloads folder named PEX')

        elif user_input == 'update -clean':
            default.add_log('removing reset update')
            os.system('rmdir /s downloads\\PEX')

        elif user_input == 'custom_command':
            with open('main/config.json', 'r') as jsonConfig:
                config = json.load(jsonConfig)
                config_username = config['username']
        elif user_input[len(user_input)-2:len(user_input)] == '()':
            user_input = user_input[0:len(user_input)-2]
            print(Fore.RED+'The '+Fore.WHITE+user_input+Fore.RED+' function cannot be run via the command line at the moment')
        #elif user_input.find('a') != -1:
            #print('I found a')
        else:
            print(Fore.RED+'Sorry, "'+user_input+Fore.RED+'" is an invalid command')
            default.add_log(Fore.WHITE+'"'+user_input+'"'+Fore.RED+' is an invalid command')