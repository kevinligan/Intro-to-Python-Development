'''
Author: Kevin Ligan

Purpose: Determine and display letter grades.
'''

print()
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

# Check if the user passed the class or not and print a congratulatory or encouraging message with creativity
if grade_percentage >= 70:
    print('\nCongratulations! You passed the class with flying colors and got a grade of', letter)
else:
    print("\nDon't be discouraged, keep working hard for next time!")

# Print the letter grade
print('\nYour final grade for this class is:', letter)
print()