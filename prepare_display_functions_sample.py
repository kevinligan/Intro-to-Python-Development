"""
Author: Kevin Ligan

Purpose: Demonstrates a basic procedure in a function.
"""

# Define a function to display the message as is
def display_regular(message):
    print(message)

# Define a function to display the message in uppercase
def display_uppercase(message):
    # Convert the message to uppercase and assign it to the variable new_message
    new_message = message.upper()
    print(new_message)

# Define a function to display the message in lowercase
def display_lowercase(message):
    # Convert the message to lowercase and assign it to the variable new_message
    new_message = message.lower()
    print(new_message)

# The regular flow of the program starts here...

# Prompt the user to enter a message and store it in the variable user_message
user_message = input("What is your message? ")

# Call the display_regular function to display the message as is
display_regular(user_message)

# Call the display_uppercase function to display the message in uppercase
display_uppercase(user_message)

# Call the display_lowercase function to display the message in lowercase
display_lowercase(user_message)
