
# An example of how to append items to a list
fruit_list = []

for item in range (0, 4):
    fruit = input('Fruit: ')
    fruit_list.append(fruit)


print()
print('**** The Fruit List ****')

# This prints the texts as ['', '', ''], which is not appealing to read off
# print(fruit_list)

# This will print each fruit individually
for item in fruit_list:
    print(item)