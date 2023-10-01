# Ask the user for a word
word = input("Enter a word: ")

# Convert the word to lowercase
word = word.lower()

# Initialize an empty list to store the code for each letter
code_list = []

# Use a for loop to traverse the string and generate the code for each letter
for char in word:
    # if char.isalpha():  # Check if the character is a letter
    code = ord(char) - ord('a')  # Calculate the code for the letter
    code_list.append(str(code))  # Convert code to string and add to the list

# Join the code list into a space-separated string12
code_str = ' '.join(code_list)

# Display the encoded code for the word
print(f"The code for \"{word}\" is: {code_str}")
