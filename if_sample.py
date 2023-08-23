'''
Author: Kevin Ligan

Purpose: Practicing if statements
'''

# Ask user for first number and convert it to an integer
first_number = int(input('What is the first number? '))

# Ask user for second number and convert it to an integer
second_number = int(input('What is the second number? '))

# Compare the two numbers and print the appropriate message
if first_number > second_number:
    print('The first number is greater')
elif first_number == second_number:
    print('The numbers are equal')
else:
    print('The second number is greater')

# Ask user for their favorite animal and print a message
favorite_animal = input('What is your favorite animal? ')
if favorite_animal.lower() == 'giraffe':
    print("That's my favorite too!")
else:
    print('That one is not my favorite.')