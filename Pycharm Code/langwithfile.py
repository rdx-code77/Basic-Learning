# Function to read vocabulary from file
def read_vocabulary(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            # Convert lines to list of tuples using split()
            vocabulary = [tuple(line.strip().split()) for line in lines if line.strip()]
        # Convert tuples to lists
        english, french = map(list, zip(*vocabulary))
        return english, french
    except FileNotFoundError:
        # Return empty lists if the file is not found
        return [], []


# Function to write vocabulary to file
def write_vocabulary(filename, vocabulary):
    with open(filename, 'w') as file:
        for word, translation in vocabulary:
            file.write(f"{word} {translation}\n")


# Announce the start of the program
print("Program to translate words from English to French and vice-versa")

# Read initial vocabulary from file
vocabulary_file = "vocabulary.txt"
english, french = read_vocabulary(vocabulary_file)

# Start a loop to continuously prompt the user for a word to translate
while True:
    word = input("\nEnter an English or French word to translate: ").lower()

    # Exit the program if the user presses Enter
    if not word:
        print("Exiting ...")

        # Write the current vocabulary to the file before exiting
        write_vocabulary(vocabulary_file, list(zip(english, french)))
        break

    # Perform translation and prompt to add the word
    if word in english:
        english_index = english.index(word)
        translation = french[english_index]
        print(f"The English word '{word}' is '{translation}' in French")
    elif word in french:
        french_index = french.index(word)
        translation = english[french_index]
        print(f"The French word '{word}' is '{translation}' in English")
    else:
        print(f"The word {word} was not found in English or French word lists")
        add_word = input(f"Would you like to add {word} to the lists? <Y>es or <N>o ").lower()

        if add_word == "y":
            lang = input(f"What language is {word} in? <E>nglish or <F>rench ").lower()
            if lang == "e":
                english.append(word)
                translation = input(f"What is the French word for '{word}'? ").lower()
                french.append(translation)
            elif lang == "f":
                french.append(word)
                translation = input(f"What is the English word for '{word}'? ").lower()
                english.append(translation)
            else:
                print("Please enter E for 'English' or F for 'French', Try again!")
        elif add_word != "n":
            print("Please enter Y for 'yes' and N for 'no', Try again!")
