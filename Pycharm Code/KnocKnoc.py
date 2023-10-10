import random


def tell_knock_knock_jokes():
    print("Ready to tell a knock-knock joke!\n")
    jokes = [
        ("Knock-knock", "Dwayne", "Dwayne the tub before I dwown"),
        ("Knock-knock", "Cash", "No thanks, I prefer peanuts."),
        ("Knock-knock", "Lettuce", "Lettuce in, it's cold out here!"),
        ("Knock-knock", "Boo", "Don't cry, it's just a joke!"),
        ("Knock-knock", "Atch", "Bless you!"),
        ("Knock-knock", "Hawaii", "I'm good. Hawaii you?"),
    ]

    print(f"There are {len(jokes)} available.")
    num_jokes = int(input("How many jokes would you like me to tell? "))
    if num_jokes > len(jokes):
        print(f"Sorry, there are only {len(jokes)} jokes available.")
        return

    print(f"\nReady to tell {num_jokes} jokes!\n")

    random.shuffle(jokes)
    responses = ["Who's there?", "Whos there?", "Who is there", "whos there?", "whos there", "who?", "who",
                 "Whose there?", "Who's There?", "who's there?"]

    for i in range(num_jokes):
        joke = jokes[i]
        for line in joke:
            print(line)
            while True:
                var = input()
                if any(response.lower() in var.lower() for response in responses):
                    break
                else:
                    print("Invalid. Please provide a valid response.")

    print("Thanks for playing!")


tell_knock_knock_jokes()
