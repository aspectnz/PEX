game_summary = []


rounds_lost = 0
rounds_drawn = 0
rounds_played = 5

for item in rnage(0, 5):
    result = input('Choose result: ')

    outcome = f'Round {item}: {result}'

    if result == 'lost':
        rounds_lost += 1
    elif result == 'tie':
        rounds_drawn += 1


    game_summary.append(outcome)

rounds_won = rounds_played - rounds_lost - rounds_drawn

# **** Calculate Game Stats ****
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100

print()

print('**** Game History ****')
for game in game_summary:
    print(game)

print()

# displays game stats with % values to the nearest whole number
print('**** Game Statistics ****')
print('Win: {}, {}, ({:.0f}%)\nLoss: {}, ({:.0f}%)\nTie: {}, ({:.0f}%)'.format(rounds_won, percent_win, rounds_lost, percent_lose, rounds_drawn, percent_tie))