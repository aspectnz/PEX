import random
import os
from time import sleep

def options():
	print('   ● lu')
	print('   ● rps')
	print('   ● hl')
	print('   ● restart')
	print('   ● quit')
	print('   ○ help')

print('Welcome to the main menu, listing commands...')

user_input = ''
while user_input != 'quit':
	options()
	user_input = input('\nEnter command: ')

	if user_input == 'lu':
		print('Opening Lucky Lucky Unicorn Game...')
		sleep(1)
		print('\n********** LUCKY UNICORN **********')
		os.system('python luckyunicorn/00_LU_Base_v_01.py')
	elif user_input == 'help':
		print('   lu = lucky unicorn (game)')
		print('   rps = rock paper scissors (game)')
		print('   hl = higher/lower (game)')
		print('   restart = restart the application (action)')
		print('   quit = quit the entire program (action)')
		print('   help = display command details (help)')
	elif user_input == 'restart':
		os.system('python app.py')
	elif user_input == 'quit':
		print('quiting the application...')
		sleep(1)
		quit()
	else:
		print('▼ INVALID COMMAND, PLEASE ENTER A VALID COMMAND ▼')
