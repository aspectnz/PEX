# from video - I am not thinking about anything at the time of copying this, so feel free to delete it later on Shannon


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


