def invalid_command_ext(command_string, user_input):
    invalid_text = user_input[len(command_string):len(user_input)]
    print('The "{}" command was identified, but contained invalid text "{}"'.format(command_string, invalid_text))

def base_command_help(user_input):
    # calculate where the dash should be (if there is)
    expected_dash = user_input[len(command_string)+1:len(command_string)+2]
    # base command
    if user_input == command_string:
        print('true')
    # sub commands for command
    elif expected_dash == '-':
        # identify sub command
        sub_command = user_input[len(command_string)+2:len(user_input)]
        if sub_command == 'des':
            print('sub command was correctly des')
        else:
            print('The "-{}" sub command is invalid'.format(sub_command))
    # otherwise inform user that the help command was identified, but had had a type
    else:
        invalid_command_ext(command_string, user_input)
        


user_input = 'help -des'
command_string = 'help'
# check if this is the valid command
if user_input[0:len(command_string)] == command_string:
    base_command_help(user_input)
    

input('x')