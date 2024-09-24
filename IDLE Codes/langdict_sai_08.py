'''
Author: Saikumar Srinivas
Filename: langdict_sai_08.py
Purpose: Language translation using dictionary 
Revisions:
    00: Announce the start of the program.
    01: Initialized the translations dictionary with initial colors and their translations.
    02: Introduced user interface for color translations.
    03: Provided functionality to prompt the user for an English color word and language selection.
    04: Implemented the check for word presence in the translations dictionary.
    05: Displayed available languages to translate into.
    06: Checked for availability of the selected language for the entered color word.
    07: Enabled addition of new words and translations to the dictionary.
    08: Handled invalid choices when adding new words.
'''
### STEP 1: Announce the start of the program
print("Language Translator")

### STEP 2: Creating a dictionary for translations
translations = {
    'blue': {'french': 'bleu', 'spanish': 'azul', 'german': 'blau'},
    'green': {'french': 'vert', 'spanish': 'verde', 'german': 'grün'},
    'yellow': {'french': 'jaune', 'spanish': 'amarillo', 'german': 'gelb'},
    'red': {'french': 'rouge', 'spanish': 'rojo', 'german': 'rot'}
    }

### STEP 3: User interface for translation  
available_colors = list(translations.keys())
print("\nAvailable English words are:", '; '.join(available_colors))

### STEP 4: Prompt the user to enter a word in English (or <Enter> to exit)    
while True:
    word_input = input("\nPlease enter a color in English: ").lower()
    if not word_input:
        print("Exiting ...")
        break
    
### STEP 5: Check if the word is in the translations dictionary    
    if word_input in translations:
        available_languages = list(translations[word_input].keys())
        print("\nAvailable language translations are:", '; '.join(available_languages))
        language_input = input("\nPlease enter a language from the list: ").lower()

### STEP 6: Check if the language is available for the entered word        
        if language_input in translations[word_input]:
            translation = translations[word_input][language_input]
            print(f'\nThe word "{word_input}" in {language_input} is "{translation}".')
        else:
            print("\nTranslation not available for this language.")
            
### STEP 7: Add new words and translations            
    else:
        add_word_choice = input(f'\nWord not found. Would you like to add "{word_input}" to the lists? <Y>es or <N>o: ').lower()  
        if add_word_choice == "y":
            translations[word_input] = {}
            for language in ['french', 'spanish', 'german']:
                translation = input(f"What is the translation of '{word_input}' in {language.capitalize()}? ").lower()
                translations[word_input][language] = translation
                
### STEP 8: Handle invalid choices
        elif add_word_choice != "n":
            print("Invalid choice. Please enter Y for 'yes' and N for 'no', Try again!")

