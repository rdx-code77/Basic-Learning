print("Guess the Secret Number\n")

import random
import math

nMax = int(input("Enter the maximum number in the range: "))
print(f"\nTry to guess the secret number from 1 to {nMax} (inclusive).\n")

nGuesses = math.ceil(math.log2(nMax))
secret_number = random.randrange(1, nMax + 1)

for guess_number in range(1, nGuesses + 1):
    # Display the number of available guesses to the user
    if nGuesses == 1:
        print("You have 1 guess available.")
    else:
        print(f"You have {nGuesses} guesses available.")

    guess = int(input(f"Enter your guess: "))

    if guess == secret_number:
        print("Correct. Well done!")
        break
    elif guess < secret_number:
        print(f"The secret number is greater than {guess}.")
    else:
        print(f"The secret number is less than {guess}.")

    # Decrement the number of available guesses
    nGuesses -= 1

else:
    print(f"Sorry, No more guesses are allowed.\nThe secret number was {secret_number}.")
