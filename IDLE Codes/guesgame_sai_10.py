'''
Author: Saikumar Srinivas
Filename: guesgame_sai_10.py
Purpose: Guessing Game
Revisions:
    00: Announce the start of the game and prompt user for input
    01: Take the range from the user and provide game instructions
    02: Calculate the maximum number of guesses based on the range
    03: Generate a random secret number within the specified range
    04: Implement the main game loop
    05: Get the user's guess
    06: Display the number of available guesses to the user
    07: Check if the guess matches the secret number
    08: Provide hints if the guess is too low or too high
    09: Decrement the number of available guesses
    10: Display the game outcome when the user runs out of guesses
'''
### STEP 1: Announce the start of the game and prompt user for input
print("Guess the Secret Number\n")

### STEP 2: Import necessary libraries
import random  # For generating random numbers
import math    # For mathematical operations

### STEP 3: Take the range from the user and provide game instructions
nMax = int(input("Enter the maximum number in the range: "))
print(f"\nTry to guess the secret number from 1 to {nMax} (inclusive).\n")

### STEP 4: Calculate the maximum number of guesses based on the range
nGuesses = math.ceil(math.log2(nMax))

### STEP 5: Generate a random secret number within the specified range
secret_number = random.randrange(1, nMax + 1)

### STEP 6: Implement the main game loop
for guess_number in range(1, nGuesses + 1):

    ### STEP 7: Display the number of available guesses to the user
    if nGuesses == 1:
        print("You have 1 guess available.")
    else:
        print(f"You have {nGuesses} guesses available.")

    ### STEP 8: Get the user's guess
    guess = int(input(f"Enter your guess: "))

    ### STEP 9: Check if the guess matches the secret number
    if guess == secret_number:
        print("Correct. Well done!")
        break

    ### STEP 10: Provide hints if the guess is too low or too high
    elif guess < secret_number:
        print(f"The secret number is greater than {guess}.")
    else:
        print(f"The secret number is less than {guess}.")

    ### STEP 11: Decrement the number of available guesses
    nGuesses -= 1

else:
    ### STEP 12: Display the game outcome when the user runs out of guesses
    print(f"\nSorry, no more guesses are allowed.\nThe secret number was {secret_number}.")
