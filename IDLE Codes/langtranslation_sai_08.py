'''
Author: Saikumar Srinivas
Filename: langtranslation_sai_08.py
Purpose: Language translation
Revisions:
    00: Announce the start of the program and prompt the user for input.
    01: Added the English and French word lists.
    02: Initialized an empty dictionary to store user-added translations.
    03: Started a loop to continuously prompt the user for a word to translate.
    04: Exit the program if the user presses Enter.
    05: Perform translation and prompt to add the word if not found in lists.
    06: Handled the case if the word is present in the English or French lists.
    07: Added the functionality to add words to the lists based on user choice.
    08: Handled the scenario if the user enters an invalid choice for adding words.
'''
### STEP 1: Announce the start of the program
print("Program to translate words from English to French and vice-versa")

### STEP 2: Defined English and French word lists
english = ['chicken', 'salt', 'apple', 'earth', 'bean', 'water', 'milk']
french = ['poulet', 'sel', 'pomme', 'terre', 'haricot', 'eau', 'lait']

### STEP 3: Initialize an empty dictionary to store user-added translations
user_translations = {}

### STEP 4: Start a loop to continuously prompt the user for a word to translate
while True:
    word = input("\nEnter an English or French word to translate: ").lower()
    
### STEP 5: Exit the program if the user presses Enter
    if not word:
        print("Exiting ...")
        break

### STEP 6: Perform translation and prompt to add the word
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

### STEP 7: Add word to translation lists based on user choice
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
        elif add_word == "n":
            pass
        else:
            print("Please enter Y for 'yes' and N for 'no', Try again!")
            

