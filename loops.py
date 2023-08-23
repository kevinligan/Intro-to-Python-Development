'''
Author: Kevin Ligan
Purpose: Practice while loops.
'''
#Prompt the user to enter positive number
number = int(input('\nPlease type a positive number: '))

#Check whether the entered number is negative.
while number < 0:
    print('\nSorry, that is a negative number. Please try again.')
    number = float(input('\nPlease type a positive number: '))
    #Jump back to line 8

#Display the entered positive number.
print(f'The number is: {number}')