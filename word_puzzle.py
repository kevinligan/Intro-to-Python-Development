'''
Author: Kevin Ligan
Purpose: Project Milestone - Word Puzzle
'''

secret_word = "mosiah"

# initialize the guess count
guess_count = 0

# welcome message
print("Welcome to the word guessing game!\n")

# loop until the user guesses the secret word
while True:
    # prompt the user for a guess
    guess = input("What is your guess? ")
    # increase the guess count
    guess_count += 1
    # check if the guess is correct
    if guess == secret_word:
        # display the success message and guess count
        print(f"\nCongratulations! You guessed it!\n\nIt took you {guess_count} guesses.")
        # break out of the loop
        break
    else:
        # display the failure message
        print("Your guess was not correct.\n")