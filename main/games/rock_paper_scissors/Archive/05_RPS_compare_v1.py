# THE FOLLOWING CODE IS FROM AN IMAGE WHICH HAS BEEN CONDENSED - THIS TAKES MORE LINES THAT SHOWN (SEE LINE NUMBERS ON THE SIDE )
# RPS Components 3 - Compare user choice and computer choice

rps_list = ['rock', 'paper', 'scissors']
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # Compare options...

        print(f'You chose {user_choice}, the computer chose {comp_choice}/ \nResult: {result}')

    comp_index += 1
    print()






