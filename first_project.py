#!/usr/bin

# get user name
name = input('Hello, can i know your name?')#

# Get the level of the user
print('What level are you?')

level = input()
print('Year')
year = input()
grad = input('Will you graduate this year?  Enter Y for yes and N for no\n')
while True:
    if grad == 'y' or grad == 'Y':
        graduate = True
        print(f'Congratulations {name}.')
        break
    elif grad == 'n' or grad == 'N':
        graduate = False
        print(f'Work harder so you can graduate next year.')
        break
    else:
        grad = input('Will you graduate this year? Enter Y for yes and N for no')
        continue
print(f'Thank you for your time {name}.')
