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

# Find the smallest positive number in the list
positive_numbers = [num for num in numbers if num > 0]
smallest_positive = min(positive_numbers)

# Sort the list in ascending order
sorted_numbers = sorted(numbers)

# Print the results
print("The sum is:", total)
print("The average is:", average)
print("The largest number is:", maximum)
print("The smallest positive number is:", smallest_positive)
print("The sorted list is:")
for num in sorted_numbers:
    print(num)