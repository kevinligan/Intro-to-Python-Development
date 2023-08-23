'''
Author: Brother Ligan
Purpose: Demonstrate the basics of reading from a text file in Python.
'''

# Open the file
with open('books.txt', 'r') as file:
    # Read the file line by line
    for line in file:
        # Strip leading and trailing whitespace
        book = line.strip()
        # Display each book
        print(book)