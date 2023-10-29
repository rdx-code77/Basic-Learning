import random


def prompt_response(prompt, responses, suggest):
    print(prompt)
    response = input().replace("'", "").strip(".!?").lower()
    if response in responses:
        return True
    else:
        print(f'The correct response is "{suggest}"')
        print("Try again\n")
        return False


jokes = [
    ("Dwayne", "dwayne who", "Dwayne who?", "Dwayne the tub before I dwown"),
    ("Cash", "cash who", "Cash who?", "No thanks, I prefer peanuts."),
    ("Lettuce", "lettuce who", "Lettuce who?", "Lettuce in, it's cold out here!"),
    ("Boo", "boo who", "Boo who?", "Don't cry, it's just a joke!"),
    ("Atch", "atch who", "Atch who?", "Bless you!"),
    ("Hawaii", "hawaii who", "Hawaii who?", "I'm good. Hawaii you?")
]
random.shuffle(jokes)

num_jokes = len(jokes)

print(f"There are {num_jokes} available.")

while True:
    num_jokes_requested = int(input("How many jokes would you like me to tell? "))

    if num_jokes_requested <= 0:
        print("Please enter a positive number of jokes.")
    elif num_jokes_requested > num_jokes:
        print(f"Sorry, there are only {num_jokes} jokes available.")
    else:
        num_jokes = num_jokes_requested
        break

print(f"\nReady to tell {num_jokes} jokes!\n")

for i in range(num_jokes):
    while not prompt_response('Knock-knock',
                              ["Who's there?", "Whos there?", "Who is there", "whos there?", "whos there", "who?",
                               "who",
                               "Whose there?", "Who's There?", "who's there?"], "Who's there?"):
        continue

    joke = jokes[i]
    while not prompt_response(joke[0], [joke[1]], joke[2]):
        continue
    print(f"{joke[3]}\n")
print("Thanks for Playing")
