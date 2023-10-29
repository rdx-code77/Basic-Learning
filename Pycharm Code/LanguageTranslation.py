print("Program to translate words from English to French and vice-versa")
# Define English and French word lists
english = ['chicken', 'salt', 'apple', 'earth', 'bean', 'water', 'milk']
french = ['poulet', 'sel', 'pomme', 'terre', 'haricot', 'eau', 'lait']

# Initialize an empty dictionary to store user-added translations
user_translations = {}

while True:
    word = input("\nEnter an English or French word to translate: ").lower()

    if not word:
        print("Exiting ...")
        break  # Exit the program if the user presses Enter

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
        add_word = input(f"Would you like to add {word} to the lists? <y>es or <n>o ").lower()

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

