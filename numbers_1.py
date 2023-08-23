'''
Author: Kevin Ligan
Purpose: Practice using mathematical expression
'''

print()

current_age = int(input('How old are you? '))
next_birthday_age = current_age + 1
print('On your next birthday, you will be', next_birthday_age)

print()

egg_cartons = int(input('How many egg cartons do you have?'))
eggs = egg_cartons * 12
print('You have', eggs, 'eggs')

print()

cookies  = int(input('How many cookies do you have? '))
people = int(input('How many people are there? '))
cookies_per_person = cookies / people
print('Each person may have', cookies_per_person, 'cookies')