'''
Author: Kevin Ligan

Purpose: Practice using numbers in lists.
'''

# Initialize an empty list to store the numbers
numbers = []

# Prompt the user to enter numbers until they input 0
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    numbers.append(num)

# Compute the sum of the numbers
total = sum(numbers)

# Compute the average of the numbers
average = total / len(numbers)

# Find the maximum number in the list
maximum = max(numbers)

# Print the results
print("The sum is:", total)
print("The average is:", average)
print("The largest number is:", maximum)