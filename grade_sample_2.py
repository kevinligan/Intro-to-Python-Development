'''
Author: Kevin Ligan

Purpose: Determine and display letter grades with +/- signs.

'''

# Ask the user to input their grade percentage and store it in a variable
grade_percentage = float(input('Please enter your grade percentage: "'))

# Check the grade percentage and assign the appropriate letter grade to the letter variable
if grade_percentage >= 90:
    letter = 'A'
elif grade_percentage >= 80:
    letter = 'B'
elif grade_percentage >= 70:
    letter = 'C'
elif grade_percentage >= 60:
    letter = 'D'
else:
    letter = 'F'

# Check the last digit of the percentage to determine the sign of the grade
last_digit = int(str(grade_percentage)[-1])
if letter == 'A' and grade_percentage != 100 and last_digit >= 7:
    sign = '+'
elif letter == 'F' or grade_percentage == 0:
    sign = ''
elif last_digit < 3:
    sign = '-'
else:
    sign = ''

# Print the grade with the appropriate sign if it exists
if letter == 'A' and grade_percentage != 100 and last_digit >= 7:
    print('\nCongratulations! You passed the class with an A-', sign)
else:
    print('\nCongratulations! You passed the class with a', letter, sign)

# Print the letter grade
print('\nYour final grade for this class is:', letter)
print()

'''
- Include a message if the user scored a 100%
- Encourage the user to work harder for a higher grade if they scored a C or lower
'''

# Check if the user scored a 100%
if grade_percentage == 100:
    print('Perfect score! Great job!')

# Encourage the user to work harder for a higher grade if they scored a C or lower
if letter == 'C' or letter == 'D' or letter == 'F':
    print("Don't be discouraged, keep working hard for next time!")