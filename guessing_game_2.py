'''
Author: Kevin Ligan

Purpose: Team Activity - Guess My Number Game (Stretch challenge)
'''

import random

while True:
    # get the random number between 1 to 100
    magic_number = random.randint(1, 100)
    
    # initialize the guess counter
    guess_count = 0
    
    while True:
        # ask the user for the guess
        guess = int(input("What is your guess? "))
        
        # increment the guess counter
        guess_count += 1
        
        # check if the guess is correct
        if guess == magic_number:
            print("You guessed it in", guess_count, "guesses!")
            break
        elif guess < magic_number:
            print("Higher")
        else:
            print("Lower")
    
    # ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no) ")
    
    # exit the loop if the user does not want to play again
    if play_again.lower() != "yes":
        break

    # inform the user how many guesses they made in the previous game
    print("You made", guess_count, "guesses in the previous game.\n")