'''
Author: Kevin Ligan

Purpose: Shopping Cart - Final
'''

# Additional creativity: Added a welcome message and quantities
# Welcome message
print('\nWelcome to the Shopping Cart Program!\n')

# Initialize empty lists for names, prices, and quantities
names = []
prices = []
quantities = []

# Function to add an item to the shopping cart
def add_item():
    item_name = input('What item would you like to add? ')
    item_price = float(input("What is the price of '{}'? ".format(item_name)))
    item_quantity = int(input("How many '{}' would you like to add? ".format(item_name)))
    names.append(item_name)
    prices.append(item_price)
    quantities.append(item_quantity)
    print("'{}' (Quantity: {}) has been added to the cart.\n".format(item_name, item_quantity))

# Function to display the contents of the shopping cart
def view_cart():
    # Additional creativity: Formatting the numbers, items, quantities and prices with aligned columns
     print('\nShopping Cart Summary:')
     print('{:<5} {:<15} {:<10} {:<10}'.format('No.', 'Item', 'Quantity', 'Price'))
     for i in range(len(names)):
         print('{:<5} {:<15} {:<10} ${:.2f}'.format(i+1, names[i], quantities[i], prices[i]))

# Function to remove an item from the shopping cart
def remove_item():
    item_number = int(input('Which item would you like to remove? '))
    if item_number >= 1 and item_number <= len(names):
        item_index = item_number - 1
        item_name = names.pop(item_index)
        item_price = prices.pop(item_index)
        item_quantity = quantities.pop(item_index)
        print("'{}' (Quantity: {}) has been removed from the cart.\n".format(item_name, item_price, item_quantity))
    else:
        print('Invalid item number. Please try again.\n')

# Function to compute the total price of the items in the shopping cart
def compute_total():
    total = sum(prices[i] * quantities[i] for i in range(len(prices)))
    print('The total price of the items in the shopping cart is ${:.2f}\n'.format(total))

# Main program loop
while True:
    print('Please select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    action = int(input('Please enter an action: '))

    if action == 1:
        add_item()
    elif action == 2:
        view_cart()
    elif action == 3:
        remove_item()
    elif action == 4:
        compute_total()
    elif action == 5:
        print('Thank you. Goodbye.')
        break
    else:
        print('Invalid action. Please try again.\n')

