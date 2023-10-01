'''
Author: Saikumar Srinivas
Filename: cyph-sai-06.py
Purpose: Cypher Program
Revisions:
    00:Announce, promt
    01:Taking input that needs to be cyphered
    02:Converting the word to lowercase(important step)
    03:Applying a loop to calculate the code for each letter entered
    04:Appending the code to the code_list
    05:Joining the code seperated by spaces
    06:Printing the code for the word 
'''
###  STEP 1: Announce, promt
# announce
print("Program to encode a word\n")

###  STEP 2: Ask the user for a word
word = input("Enter a word: ")

###  STEP 3: Convert the word to lowercase
word = word.lower()

###  STEP 4: Initialize an empty list to store the code for each letter
code_list = []

###  STEP 5: Use a for loop to generate the code for each letter
for char in word:
    code = ord(char) - ord('a')  # Calculate the code for the letter
    code_list.append(str(code))  # Convert code to string and add to the list

###  STEP 6: Join the code list into a space-separated string
code_str = ' '.join(code_list)

###  STEP 7: Display the encoded code for the word
print(f"The code for \"{word}\" is: {code_str}")
