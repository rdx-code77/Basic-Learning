'''
Author: Saikumar Srinivas
Filename: knockJoke_sai_05.py
Purpose: Knock-Knock Jokes
Revisions:
    00: Announce the start of the game and prompt user for input
    01: Ensure the game's joke database is shuffled
    02: Allow the user to specify the number of jokes they want to hear
    03: Prompt user for the "Knock-knock" response
    04: Ask the user for the punchline response
    05: Display the punchline
'''
### STEP 1: Announce the start of the game and prompt user for input
print("Ready to tell a knock-knock joke!\n")

### STEP 2: Importing necessary libraries
import random

### STEP 3: Define a function to prompt user responses & clean it
def prompt_response(prompt, responses, suggest):
    print(prompt)
    response = input().replace("'", "").strip(".!?").lower()
    if response in responses:
        return True
    else:
        print(f'The correct response is "{suggest}"')
        print("Try again.\n")
        return False

### STEP 4: Define the database of jokes
jokes = [
    ("Dwayne.", "dwayne who", "Dwayne who?", "Dwayne the tub before I dwown"),
    ("Cash.", "cash who", "Cash who?", "No thanks, I prefer peanuts."),
    ("Lettuce.", "lettuce who", "Lettuce who?", "Lettuce in, it's cold out here!"),
    ("Boo.", "boo who", "Boo who?", "Don't cry, it's just a joke!"),
    ("Atch.", "atch who", "Atch who?", "Bless you!"),
    ("Hawaii.", "hawaii who", "Hawaii who?", "I'm good. Hawaii you?"),
    ("Tank.", "tank who", "Tank who?", "You're welcome.")
]

### STEP 5: Shuffle the order of jokes
random.shuffle(jokes)   # Using the shuffle function from the random module
num_jokes = len(jokes)

### STEP 6: Announce the available number of jokes
print(f"There are {num_jokes} available.")

### STEP 7: Prompt the user for the number of jokes they want to hear
while True:
    # Receive and validate the response; handled exceptions
    try:
        num_jokes_requested = int(input("How many jokes would you like me to tell? "))

        if num_jokes_requested <= 0:
            print("Please enter a positive number of jokes.\n")
        elif num_jokes_requested > num_jokes:
            print(f"Sorry, there are only {num_jokes} jokes available.\n")
        else:
            num_jokes = num_jokes_requested
            break
    except ValueError:
        print("Please enter a valid numerical value.\n")

print(f"\nReady to tell {num_jokes} jokes!\n")

### STEP 8: Loop through the selected number of jokes
for i in range(num_jokes):
    who_varient = ["whos there", "who there", "who is there", "who is it", "whose there"]
    while not prompt_response('Knock-knock!', who_varient, "Who's there?"):
        continue
    joke = jokes[i]
    while not prompt_response(joke[0], [joke[1]], joke[2]):
        continue
    print(f"{joke[3]}\n")

### STEP 9: Thank the user for playing
print("\nThanks for Playing")
