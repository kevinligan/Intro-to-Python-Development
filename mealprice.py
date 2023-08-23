'''
Author: Kevin Ligan
Purpose: Project 02: Meal Price Calculator
'''

print()
'''Additional creativity'''
# Display a welcome message to the user
print('\nWelcome! :) ')

print()
# This program calculates the total cost of a meal including sales tax and displays it to the user.

# Prompt user for the price of a child's and adult's meal and store the value as a float
child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))

# Prompt user for the number of children and adults and store the value as an integer
num_children = int(input('How many children are there? '))
num_adults = int(input('How many adults are there? '))

# Prompt user for the sales tax rate and store the value as a float
tax_rate = float(input('What is the sales tax rate? '))

# Calculate the subtotal by multiplying the price of child's meal by the number of children
# and the price of adult's meal by the number of adults, and then adding them together
subtotal = child_price * num_children + adult_price * num_adults

# Calculate the sales tax by multiplying the subtotal by the tax rate (as a decimal)
sales_tax = subtotal * (tax_rate / 100)

# Calculate the total by adding the subtotal and the sales tax
total = subtotal + sales_tax

# Display the subtotal, sales tax, and total in dollars with 2 decimal places
print(f'\nSubtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Total: ${total:.2f}')

# Prompt user for the payment amount and store it as a float
payment_amount = float(input('\nWhat is the payment amount? '))

# Compute the change by subtracting the payment amount from the total
change = payment_amount - total

# Display the change in dollars and cents
print(f'Your change is: ${change:.2f}')

'''Additional creativity'''
# Display a thank you and come again message to the user
print('\nThank you for dining with us!')
print('\nCome Again!!! :) ')

print()