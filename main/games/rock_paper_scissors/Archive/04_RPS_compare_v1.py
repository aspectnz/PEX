# RPS Components 3 - Compare user choice and computer choice

rps_list = ['rock', 'paper', 'scissors']
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # Compare choices
        if comp_choice == user_choice:
            result = 'tie'
            rounds_drawn += 1
        elif user_choice == 'rock' and comp_choice == 'scissors':
            result = 'won'
        elif user_choice == 'paper' and comp_choice == 'rock':
            result = 'won'
        elif user_choice == 'scissors' and comp_choice == 'paper':
            result = 'won'
        else:
            result = 'lost'
            rounds_lost += 1

        if result == 'tie':
            feedback = 'It\'s a tie'
        else:
            feedback = f'{user_choice} vs {comp_choice} - you. {result}'

        print(f'You chose {user_choice}, the computer chose {comp_choice} \nResult: {result}')

    comp_index += 1
    print()






