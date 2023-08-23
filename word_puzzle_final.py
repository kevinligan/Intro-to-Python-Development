'''
Author: Kevin Ligan
Purpose: Final Project - Word Puzzle
'''
 
import random
#Added Creativity: If the user exceeds the time limit for each guess, a time's up message is displayed, informing the user about the time constraint.
import time

# List of possible secret words
word_list = ['mosiah', 'apple', 'banana', 'orange', 'grape', 'watermelon', 'strawberry', 'blueberry', 'kiwi', 'mango']

# Select a random secret word from the list
secret_word = random.choice(word_list)

# Initialize the guess count
guess_count = 0

# Set the time limit for each guess (in seconds)
time_limit = 2

# Start the timer
start_time = time.time()

# Welcome message
print('Welcome to the word guessing game!\n')

# Loop until the user guesses the secret word or runs out of time
while True:
    # Prompt the user for a guess
    guess = input('What is your guess? ')

    # Increase the guess count
    guess_count += 1

    # Check if the length of the guess is the same as the length of the secret word
    if len(guess) != len(secret_word):
        print('Your guess should be the same length as the secret word.\n')
        continue
    #Using a loop, the hint is displayed for each guess and it follows the correct rules for underscores, lowercase, and uppercase letters.
    # Create the initial hint
    hint = ""
    for secret_char, guess_char in zip(secret_word, guess):
        if secret_char == guess_char:
            hint += secret_char.upper()
        elif secret_char in guess:
            hint += guess_char.lower()
        else:
            hint += "_"

    # Display the hint
    print(f'Hint: {hint}\n')

    # Check if the guess is correct
    if guess == secret_word:
        # Display the success message and guess count
        print(f"Congratulations! You guessed the secret word '{secret_word}' in {guess_count} guesses.")
        # Break out of the loop
        break
    else:
        # Display the failure message
        print('Your guess was not correct.\n')
    # Check the elapsed time
    elapsed_time = time.time() - start_time
    if elapsed_time >= time_limit:
        # Time limit exceeded

    # Check if the time limit has been exceeded
        print(f"Time's up! You have exceeded the time limit of {time_limit} seconds.")
        break