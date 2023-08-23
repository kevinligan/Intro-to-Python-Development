'''
Author: Kevin Ligan

Purpose: Shopping Cart - Milestones
'''

# Initialize an empty list to store the items in the cart
cart = []

while True:
    # Display menu options to the user
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    # Prompt the user to enter an action
    action = int(input("Please enter an action: "))
    
    if action == 1:
        # Prompt the user to enter an item to add to the cart
        item = input("What item would you like to add? ")
        cart.append(item)
        print(f"'{item}' has been added to the cart.")
    elif action == 2:
        # Display the contents of the cart
        print("The contents of the shopping cart are:")
        for item in cart:
            print(item)
    elif action == 3:
        # Prompt the user to enter an item to remove from the cart
        item = input("What item would you like to remove? ")
        if item in cart:
            cart.remove(item)
            print(f"'{item}' has been removed from the cart.")
        else:
            print(f"'{item}' is not in the cart.")
    elif action == 4:
        # Compute the total number of items in the cart
        total = len(cart)
        print(f"The total number of items in the cart is: {total}")
    elif action == 5:
        # Quit the program
        print("Thank you. Goodbye.")
        break
    else:
        print("Invalid action. Please try again.")