import random
# set balance for testing purposes
balance = 5
rounds_played = 0

play_again = input('Press <Enter> to play...').lower()
while play_again == '':
    # increase # of rounds played
    rounds_played += 1

    # print round number
    print('*** Round #{} ***'.format(rounds_played))

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # If the random # is between 1 and 5, user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = 'unicorn'
        balance += 4
    # If the random # is between 6 and 36, user gets a donkey (subtract $1 from balance
    elif 6 <= chosen_num <= 36:
        chosen = 'donkey'
        balance -= 1
    # The token is either a horse or zebra...
    # In both cases, subtract $0.50 from the balance
    else:
        # If the number is even, set the chosen item to a horse
        if chosen_num % 2 == 0:
            chosen = 'horse'
        # Otherwise set it to a zebra
        else:
            chosen = 'zebra'
        balance -= 0.5

    if balance < 1:
        play_again = 'xxx'
        print('Sorry you have run out of money')
    else:
        play_again = input('Press Enter to play again or "xxx" to quit')


print()
print('Final balance', balance)