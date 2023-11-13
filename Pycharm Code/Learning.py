# from itertools import chain
#
# var = chain(range(1, 6), range(10, 21, 2))
# for i in var:
#     print(i, end=" ")
#

# veg = ["corn", "radish", "patuto", "rice", "rasam"]
# for i in range(len(veg)):
#     print(veg[i])

# import math

# x = int(input("enter a number"))
# z = math.sqrt(x)
# print(z)
#
# q = int(input("enter the number"))
# p = q ** 0.5
# print(p)

# a = int(input("Enter number of males: "))
# b = int(input("Enter number of females: "))
# Total = a + b
# Percent_males = (a / Total) * 100
# Percent_females = (b / Total) * 100
# print(f"Percent males: {round(Percent_males)}%")
# print(f"Percent females: {round(Percent_females)}%")

# Input: Customer type (premium or regular)
# isPremiumCustomer = input("Enter customer type (premium or regular): ").lower()
#
# # Input: Number of books purchased
# nbooksPurchased = int(input("Enter the number of books purchased: "))
#
# # Determine the number of free books based on customer type and purchase count
# if isPremiumCustomer == "premium":
#     if nbooksPurchased >= 8:
#         freeBooks = 2
#     elif nbooksPurchased >= 5:
#         freeBooks = 1
#     else:
#         freeBooks = 0
# elif isPremiumCustomer == "regular":
#     if nbooksPurchased >= 12:
#         freeBooks = 2
#     elif nbooksPurchased >= 7:
#         freeBooks = 1
#     else:
#         freeBooks = 0
#
# # Display the result
# print(f"You are eligible for {freeBooks} free book(s).")

# Input: Boolean for customer type (True for premium, False for regular)
# isPremiumCustomer = input("Are you a premium customer? (True or False): ").strip().lower() == "true"
#
# # Input: Number of books purchased
# nbooksPurchased = int(input("Enter the number of books purchased: "))
#
# # Determine the number of free books based on customer type and purchase count
# if isPremiumCustomer:
#     if nbooksPurchased >= 8:
#         freeBooks = 2
#     elif nbooksPurchased >= 5:
#         freeBooks = 1
#     else:
#         freeBooks = 0
# else:
#     if nbooksPurchased >= 12:
#         freeBooks = 2
#     elif nbooksPurchased >= 7:
#         freeBooks = 1
#     else:
#         freeBooks = 0
#
# # Display the result
# print(f"You are eligible for {freeBooks} free book(s).")

# Input: User's choice of menu item (S, T, or B)
# choice = input("Enter your choice (S, T, or B): ").upper()
#
# # Input: User's age
# age = int(input("Enter your age: "))
#
# # Initialize a variable for the recommended drink
# recommended_drink = ""
#
# # Check the user's choice and age to determine the recommended drink
# if choice == "S":
#     if age <= 21:
#         recommended_drink = "vegetable juice"
#     else:
#         recommended_drink = "cabernet"
# elif choice == "T":
#     if age <= 21:
#         recommended_drink = "cranberry juice"
#     else:
#         recommended_drink = "chardonnay"
# elif choice == "B":
#     if age <= 21:
#         recommended_drink = "soda"
#     else:
#         recommended_drink = "IPA"
# else:
#     recommended_drink = "invalid menu selection"
#
# # Display the recommended drink
# print(f"Recommended drink: {recommended_drink}")

'''
Author: Saikumar Srinivas
Filename: avrg-sai-03.py
Purpose: Simple Average
Revisions:
    00:Announce, promt
    01:Taking input from user & initializing total(sum) as 0
    02:Iterating the range function based on user input
    03:Calculating the average & then displaying it
'''

### STEP 1: Announce, promt
# announce
# print("Program to compute the average of the numbers provided.")
#
# # Initialize an empty list to store the numbers
# numbers = []
#
# print("Enter each number followed by <enter>.")
# print("When you are done, just hit <enter> in response to the prompt.")
# while user_input := input("Enter a number: ").strip():
#     try:
#         numbers.append(float(user_input))  # Convert and append the input to the list
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#
# if numbers:
#     average = sum(numbers) / len(numbers)
#     print(f"You entered {len(numbers)} numbers.\nThe average is {average:.1f}.")
# else:
#     print("No numbers were entered.")


# weights = (12, 19, 6, 14, 22, 7)
# desired_weight = 18
# actual_weight = set()
# for i in weights:
#     if i in desired_weight:
#         actual_weight.add(i)
#         actual_weight.discard(i)
#     print(actual_weight)


# def generate_histogram(text):
#     # Initialize a dictionary to store character frequencies
#     char_frequency = {}
#
#     # Convert the text to uppercase for case-insensitive analysis
#     text = text.upper()
#
#     # Calculate character frequencies
#     for char in text:
#         if char.isalpha():  # Ignore non-alphabetic characters
#             if char in char_frequency:
#                 char_frequency[char] += 1
#             else:
#                 char_frequency[char] = 1
#
#     # Find the maximum frequency
#     max_frequency = max(char_frequency.values())
#
#     # Print the histogram
#     for char, frequency in char_frequency.items():
#         histogram_bar = '=' * frequency
#         print(f"{char}: {histogram_bar}")
#
#     # Print the character with the maximum frequency
#     for char, frequency in char_frequency.items():
#         if frequency == max_frequency:
#             print(f"\n{char} was used most ({max_frequency} times)")
#
#
# # Input text
# input_text = input("Enter text to analyze ...\n")
# generate_histogram(input_text)

# print("Text Analysis Histogram\n")
#
#
# def generate_histogram(text):
#     # Initialize a dictionary to store character frequencies
#     char_frequency = {}
#
#     # Convert the text to uppercase for case-insensitive analysis
#     text = text.upper()
#
#     # Calculate character frequencies
#     for char in text:
#         if char.isalpha():  # Ignore non-alphabetic characters
#             if char in char_frequency:
#                 char_frequency[char] += 1
#             else:
#                 char_frequency[char] = 1
#
#     # Find the maximum frequency
#     max_frequency = max(char_frequency.values())
#
#     # Print the histogram
#     print("Character Histogram:")
#     for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#         frequency = char_frequency.get(char, 0)
#         histogram_bar = '=' * frequency
#         print(f"{char}: {histogram_bar}")
#
#     # Print the character(s) with the highest frequency
#     for char, frequency in char_frequency.items():
#         if frequency == max_frequency:
#             print(f"\n{char} was used most ({max_frequency} times)")
#
#
# # Input text
# input_text = input("Enter text to analyze ...\n")
# generate_histogram(input_text)

# print("Text Analysis Histogram\n")
#
#
# def generate_histogram(text):
#     # Initialize a list to store character frequencies (26 elements for A to Z)
#     char_frequency = [0] * 26
#
#     # Convert the text to uppercase for case-insensitive analysis
#     text = text.upper()
#
#     # Calculate character frequencies
#     for char in text:
#         if char.isalpha():  # Ignore non-alphabetic characters
#             char_index = ord(char) - ord('A')  # Calculate index for A to Z
#             char_frequency[char_index] += 1
#
#     # Find the maximum frequency
#     max_frequency = max(char_frequency)
#
#     # Print the histogram
#     print("Character Histogram:")
#     for char_index, frequency in enumerate(char_frequency):
#         char = chr(char_index + ord('A'))  # Convert index back to character
#         histogram_bar = '=' * frequency
#         print(f"{char}: {histogram_bar}")
#
#     # Print the character(s) with the highest frequency
#     for char_index, frequency in enumerate(char_frequency):
#         char = chr(char_index + ord('A'))  # Convert index back to character
#         if frequency == max_frequency:
#             print(f"\n{char} was used most ({max_frequency} times)")
#
#
# # Input text
# input_text = input("Enter text to analyze ...\n")
# generate_histogram(input_text)

# def normalize(data, norm2Peak=True):
#     # Function to normalize data
#     # Args:
#     #   data: List of numbers representing character counts
#     #   norm2Peak: Boolean, True for normalizing to peak, False for normalizing to area (default is True)
#     # Returns:
#     #   List of floats representing normalized counts
#
#     if norm2Peak:
#         # Normalize to peak
#         max_count = max(data)
#         return [count / max_count for count in data]
#     else:
#         # Normalize to area
#         total_count = sum(data)
#         return [count / total_count for count in data]
#
#
# def plotBars(counts, alphabet, barLength=20):
#     # Function to plot histogram bars
#     # Args:
#     #   counts: List of numbers representing character counts
#     #   alphabet: String representing the alphabet
#     #   barLength: Optional integer specifying the maximum length of a bar (default is 20)
#
#     # Find the character(s) with the maximum frequency
#     max_count = max(counts)
#     max_chars = [char for char, count in zip(alphabet, counts) if count == max_count]
#
#     # Print the histogram
#     print("Character Histogram:")
#     for char, count in zip(alphabet, counts):
#         normalized_count = int(count * barLength)
#         histogram_bar = '=' * normalized_count
#         print(f"{char}: {histogram_bar}")
#
#     # Print the character(s) with the highest frequency
#     print("\nCharacter(s) with the highest frequency:")
#     for char in max_chars:
#         percent = counts[alphabet.index(char)] / sum(counts) * 100
#         print(f"{char}: {percent:.2f}%")
#
#
# def main():
#     # Input text
#     input_text = input("Enter text to analyze: ")
#
#     # Convert input text to uppercase
#     input_text = input_text.upper()
#
#     # Define the alphabet
#     alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#     # Initialize a list to store character counts
#     char_counts = []
#
#     # Count the characters in the input text
#     for char in alphabet:
#         count = input_text.count(char)
#         char_counts.append(count)
#
#     # Normalize the data to peak
#     pkNormData = normalize(char_counts, norm2Peak=True)
#
#     # Normalize the data to area
#     aNormData = normalize(char_counts, norm2Peak=False)
#
#     # Print the histogram
#     plotBars(pkNormData, alphabet, barLength=20)
#
#
# if __name__ == "__main__":
#     main()
#
# '''
# Name: Histogram Analysis
# Author: Khatija Begum
# Description: Constructing a histogram for character frequencies in the text.
# '''
#
# '''  Program Begins Here  '''
#
# print(" Text Analysis Histogram\n")  # Printing the program name
#
# User_text = input("Enter text to analyze ...\n")  # Enter the Text for Analysis
#
# '''
#
# Defining a function to Construct Histogram for input text given by the User such that whenever this function is called a histogram is generated.
#
# bigChar = A String Initialised with zero, 26 times for elements A to Z
#
# User_text.upper()is used considering the desired output for this program, we are using upper() method to convert the text entered by user to Upper case.
#
# for loop used to iterate each character of the text
#
# Method isalpha() used here to ignore non-alphabetic text given by user as it's not required for our program to display non-alphabetic text.
#
# index is calculated to store the characters in our list bigChar which is initialized to 0, we take 'A' as starting point for index.
#
# Character frequencies is calculates by adding 1 to index of bigChar every time the loop iterates over the text.
#
# Highest frequencies are calculated using max() function and printed along with Characters at the end of histogram generation.
#
# '''
#
#
# def histogram(User_text):
#     bigChar = '0' * 26  # Initializing String with 0 to store characters A-Z
#
#     User_text = User_text.upper()  # Convert the text to uppercase
#
#     for c in User_text:  # Calculate character frequencies in text
#         if c.isalpha():  # Skip non-alphabetic characters
#             index = ord(c) - ord('A')  # Calculate the index for A-Z starting from A
#             bigChar = bigChar[:index] + str(int(bigChar[index]) + 1) + bigChar[
#                                                                        index + 1:]  # Calculating Character frequencies and storing in String bigChar
#
#     for index in range(26):  # Printing the histogram
#         char = chr(ord('A') + index)  # To print, get the characters A-Z
#         n = int(bigChar[index])
#         bar = '=' * n
#         print(f"{char}: {bar}")
#
#     # To Print the character(s) with the Maximum frequency
#
#     bigFreq = max(bigChar)  # Finding the maximum frequency of Characters in the Text
#
#     print()  # Simply printing to get space between histogram output and max frequency output to get the desired result.
#
#     for index in range(26):
#         char = chr(ord('A') + index)
#         n = int(bigChar[index])
#         if n == int(bigFreq):
#             print(f"{char} was used most ({bigFreq} times)")  # printing Character and Highest frequency using f-string
#
#
# # Function invocation
# histogram(User_text)

# Input text
# input_text = input("Enter text to analyze: ")
#
# # Convert input text to uppercase
# input_text = input_text.upper()
#
# # Define the alphabet
# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# # Initialize a list to store character counts
# char_counts = []
#
# # Count the characters in the input text
# for char in alphabet:
#     count = input_text.count(char)
#     char_counts.append(count)
#
# # Find the character(s) with the maximum frequency
# max_count = max(char_counts)
# max_chars = [char for char, count in zip(alphabet, char_counts) if count == max_count]
#
# # Print the histogram
# print("Character Histogram:")
# for char, count in zip(alphabet, char_counts):
#     normalized_count = int(count / max_count * 20)
#     histogram_bar = '=' * normalized_count
#     print(f"{char}: {histogram_bar}")
#
# # Print the character(s) with the highest frequency
# print("\nCharacter(s) with the highest frequency:")
# for char in max_chars:
#     percent = char_counts[alphabet.index(char)] / sum(char_counts) * 100
#     print(f"{char}: {percent:.2f}%")

# def normalize(data, norm2Peak=True):
#     """
#     Normalize data based on the specified option.
#
#     Args:
#         data: List of numbers representing character counts
#         norm2Peak: Boolean, True for normalizing to peak, False for normalizing to area (default is True)
#
#     Returns:
#         List of floats representing normalized counts
#     """
#     if not data:
#         return []
#
#     if norm2Peak:
#         max_count = max(data)
#         normalized_data = [count / max_count for count in data]
#     else:
#         total_count = sum(data)
#         normalized_data = [count / total_count for count in data]
#
#     return normalized_data
#
#
# def plotBars(counts, alphabet, barLength=20):
#     """
#     Plot histogram bars and report character(s) with the maximum frequency.
#
#     Args:
#         counts: List of numbers representing character counts
#         alphabet: String representing the alphabet
#         barLength: Optional integer specifying the maximum length of a bar (default is 20)
#     """
#     if not counts:
#         return
#
#     # Normalize counts to peak for histogram
#     peak_normalized_counts = normalize(counts, norm2Peak=True)
#
#     # Find the character(s) with the maximum frequency
#     max_count = max(counts)
#     max_chars = [char for char, count in zip(alphabet, counts) if count == max_count]
#
#     # Print the histogram
#     print("Character Histogram:")
#     for char, count in zip(alphabet, peak_normalized_counts):
#         normalized_count = int(count * barLength)
#         histogram_bar = '=' * normalized_count
#         print(f"{char}: {histogram_bar}")
#
#     # Print the character(s) with the highest frequency and their percent of the sample
#     print("\nCharacter(s) with the highest frequency:")
#     for char in max_chars:
#         percent = counts[alphabet.index(char)] / sum(counts) * 100
#         print(f"{char}: {percent:.2f}%")
#
#
# if __name__ == "__main__":
#     # Input text
#     input_text = input("Enter text to analyze: ")
#
#     # Convert input text to uppercase
#     input_text = input_text.upper()
#
#     # Define the alphabet
#     alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#     # Initialize a list to store character counts
#     char_counts = []
#
#     # Count the characters in the input text
#     for char in alphabet:
#         count = input_text.count(char)
#         char_counts.append(count)
#
#     # Call the plotBars function to visualize the character frequencies
#     plotBars(char_counts, alphabet, barLength=20)

# import random
#
#
# def prompt_response(prompt, responses, suggest):
#     print(prompt)
#     response = input().lower()  # Convert the user input to lowercase
#     cleaned_response = ''.join(char for char in response if char.isalnum() or char.isspace())
#     if cleaned_response in responses:
#         return True
#     else:
#         print(f'The correct response is "{suggest}"')
#         print('Try again\n')
#         return False
#
#
# # Define a list of knock-knock jokes
# jokes = [
#     {
#         'prompt1': "Knock-knock.",
#         'response1': "Who's there?",
#         'prompt2': "Lettuce.",
#         'response2': "Lettuce who?",
#         'punchline': "Lettuce in, it's cold out here!"
#     },
#     {
#         'prompt1': "Knock-knock.",
#         'response1': "Who's there?",
#         'prompt2': "Tank.",
#         'response2': "Tank who?",
#         'punchline': "You're welcome!"
#     },
#     # Add more jokes as needed
# ]
#
# # Shuffle the list of jokes randomly
# random.shuffle(jokes)
#
# # Ask the user how many jokes they want to listen to
# num_jokes = int(input("How many knock-knock jokes would you like to hear? "))
#
# for i in range(min(num_jokes, len(jokes))):
#     joke = jokes[i]
#     success1 = prompt_response(joke['prompt1'], ["who's there?"], joke['response1'])
#     success2 = prompt_response(joke['prompt2'], [joke['response1']], joke['response2'])
#     success3 = prompt_response(joke['punchline'], [joke['response2']], "You're welcome!")
#
#     if success1 and success2 and success3:
#         print("Congratulations! You got the joke!\n")
#     else:
#         print("Sorry, you missed the joke. Let's try the next one!\n")

# import random
#
#
# # Function to check if the response is correct
# def is_response_correct(response, correct_responses):
#     cleaned_response = clean(response.lower())
#     return cleaned_response in correct_responses
#
#
# # Function to remove punctuation from a string
# def clean(response):
#     punctuation = "',.!?;\""
#     return ''.join([c for c in response if c not in punctuation])
#
#
# # List of knock-knock jokes
# jokes = [
#     ('Tank', "You're welcome!"),
#     ('Lettuce', 'Lettuce in, it’s cold out here!'),
#     ('Boo', "Don't cry, it's just a joke!"),
#     # Add more jokes here
# ]
#
# # Shuffle the order of jokes
# random.shuffle(jokes)
#
# # Get the maximum number of jokes available
# max_jokes = len(jokes)
#
# while True:
#     try:
#         # Ask the user how many jokes they want to hear
#         n_jokes = int(input(f"How many jokes would you like me to tell (1-{max_jokes})? "))
#
#         if 1 <= n_jokes <= max_jokes:
#             break
#         else:
#             print(f"Please enter a number between 1 and {max_jokes}.")
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")
#
# # Take a slice of jokes based on the user's input
# selected_jokes = jokes[:n_jokes]
#
# # Tell the selected jokes
# for prompt, punchline in selected_jokes:
#     print("Knock-knock.")
#     input("Who's there? ")
#     print(prompt)
#     response = input(f"{prompt} who? ")
#
#     if is_response_correct(response, [punchline]):
#         print("You're welcome!\n")
#     else:
#         print(f"Actually, the correct response is: {punchline}\n")
#
# print("That's all the jokes for today! Have a great day!")
#
# import random
#
#
# def clean(response):
#     """Removes punctuation from a string.
#
#   Args:
#     response: A string.
#
#   Returns:
#     A string without punctuation.
#   """
#     punctuation = "',.!?;\""
#     response = response.strip()
#     return ''.join([c for c in response if c not in punctuation])
#
#
# def is_correct_response(response, responses):
#     """Returns True if the response is in the list of correct responses.
#
#   Args:
#     response: A string.
#     responses: A list of strings.
#
#   Returns:
#     True if the response is in the list of correct responses, False otherwise.
#   """
#     return response.lower() in [response.lower() for response in responses]
#
#
# def tell_joke(joke):
#     """Tells a joke.
#
#   Args:
#     joke: A tuple containing the joke prompt and punchline.
#   """
#     joke_prompt, joke_punchline = joke
#     print(joke_prompt)
#     response = input("Who's there? ")
#     while not is_correct_response(response, [joke_prompt.lower()]):
#         print("Try again.")
#         response = input("Who's there? ")
#     print(joke_punchline)
#
#
# def main():
#     """Tells a random joke."""
#     jokes = [
#         ("Tank", "You're welcome!"),
#         ("Boo", "Don't cry, it's just a joke"),
#         ("Cows go", "No, cows go moo"),
#         ("Alpaca", "Alpaca the suitcase, you load up the car"),
#         ("Avenue", "Avenue knocked on this door before"),
#         ("Dishes", "Dishes the police come out with their hands up"),
#         ("Lettuce", "Lettuce in, it's cold out here!"),
#     ]
#
#     # Shuffle the jokes
#     random.shuffle(jokes)
#
#     # Get the number of jokes to tell
#     print("There are {} available jokes.".format(len(jokes)))
#     num_jokes = int(input("How many jokes would you like me to tell? "))
#
#     # Tell the jokes
#     for i in range(num_jokes):
#         tell_joke(jokes[i])
#
#
# if __name__ == "__main__":
#     main()

# def create_resume(name, contact_info, summary, experience, education, skills):
#     resume = f"Name: {name}\n"
#     resume += f"Contact: {contact_info}\n\n"
#
#     resume += "Summary:\n"
#     resume += f"{summary}\n\n"
#
#     resume += "Experience:\n"
#     for i, exp in enumerate(experience, 1):
#         resume += f"{i}. {exp['position']} at {exp['company']} ({exp['start_date']} - {exp['end_date']}):\n"
#         resume += f"   - {exp['description']}\n"
#
#     resume += "\nEducation:\n"
#     for i, edu in enumerate(education, 1):
#         resume += f"{i}. {edu['degree']} in {edu['major']} at {edu['university']} ({edu['graduation_year']})\n"
#
#     resume += "\nSkills:\n"
#     resume += ', '.join(skills)
#
#     return resume
#
#
# # Example data
# name = "John Doe"
# contact_info = "123 Main St, City, State | john.doe@email.com | (123) 456-7890"
# summary = "Results-driven professional with 5 years of experience in software development."
# experience = [
#     {
#         "position": "Software Engineer",
#         "company": "ABC Inc.",
#         "start_date": "2018",
#         "end_date": "2021",
#         "description": "Developed web applications using Python and Django."
#     },
#     {
#         "position": "Frontend Developer",
#         "company": "XYZ Corp.",
#         "start_date": "2016",
#         "end_date": "2018",
#         "description": "Designed and implemented user interfaces using HTML, CSS, and JavaScript."
#     }
# ]
# education = [
#     {
#         "degree": "Bachelor of Science",
#         "major": "Computer Science",
#         "university": "University of XYZ",
#         "graduation_year": "2016"
#     }
# ]
# skills = ["Python", "Django", "HTML/CSS", "JavaScript"]
#
# # Generate the resume
# generated_resume = create_resume(name, contact_info, summary, experience, education, skills)
#
# # Print the generated resume
# print(generated_resume)

# import random
#
#
# def prompt_response(prompt, responses, suggest):
#     print(prompt)
#     response = input().replace("'", "").strip(".!?").lower()
#     if response in responses:
#         return True
#     else:
#         print(f'The correct response is "{suggest}"')
#         print("Try again\n")
#         return False
#
#
# num_jokes = int(input("How many jokes would you like me to tell? "))
# while not prompt_response('Knock-knock',
#                           ["Who's there?", "Whos there?", "Who is there", "whos there?", "whos there", "who?", "who",
#                            "Whose there?", "Who's There?", "who's there?"], "Who's there?"):
#     continue
#
# jokes = [
#     ("Dwayne", "dwayne who", "Dwayne who?", "Dwayne the tub before I dwown"),
#     ("Cash", "cash who", "Cash who?", "No thanks, I prefer peanuts."),
#     ("Lettuce", "lettuce who", "Lettuce who?", "Lettuce in, it's cold out here!"),
#     ("Boo", "boo who", "Boo who?", "Don't cry, it's just a joke!"),
#     ("Atch", "atch who", "Atch who?", "Bless you!"),
#     ("Hawaii", "hawaii who", "Hawaii who?", "I'm good. Hawaii you?")
# ]
# random.shuffle(jokes)
#
# for i in range(num_jokes):
#     joke = jokes[i]
#     while not prompt_response(joke[0], [joke[1]], joke[2]):
#         continue
#     print(joke[3])
#     print("\nThanks for Playing")

# Define English and French word lists
# english = ['chicken', 'salt', 'apple', 'earth', 'bean', 'water', 'milk']
# french = ['poulet', 'sel', 'pomme', 'terre', 'haricot', 'eau', 'lait']
#
# # Initialize an empty dictionary to store user-added translations
# user_translations = {}
#
# while True:
#     word = input("Enter a word (or press Enter to exit): ").lower()
#
#     if not word:
#         break  # Exit the program if the user presses Enter
#
#     if word in english:
#         english_index = english.index(word)
#         translation = french[english_index]
#         print(f"The translation in French is: {translation}")
#     elif word in french:
#         french_index = french.index(word)
#         translation = english[french_index]
#         print(f"The translation in English is: {translation}")
#     else:
#         print("Word not found in the dictionary.")
#         add_word = input("Would you like to add this word to the dictionary? (yes/no): ").lower()
#
#         if add_word == "yes":
#             lang = input("Is the word in English or French? ").lower()
#             if lang == "english":
#                 english.append(word)
#                 translation = input(f"Enter the translation of '{word}' in French: ").lower()
#                 french.append(translation)
#             elif lang == "french":
#                 french.append(word)
#                 translation = input(f"Enter the translation of '{word}' in English: ").lower()
#                 english.append(translation)
#             user_translations[word] = translation
#             print("Word and translation added to the dictionary.")
#         else:
#             print("Word not added to the dictionary.")
#
# # Print the user-added translations
# if user_translations:
#     print("\nUser-Added Translations:")
#     for word, translation in user_translations.items():
#         print(f"{word.capitalize()} in French is {translation.capitalize()}")

# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []
#
#
# print(twoSum([2, 7, 11, 15], 9))

# def isPalindrome(x):
#     """
#         :type x: int
#         :rtype: bool
#         """
#     if x < 0:
#         return False
#     inputNum = x
#     newNum = 0
#     while x > 0:
#         newNum = newNum * 10 + x % 10
#         x = x // 10
#     return newNum == inputNum
#
# print(isPalindrome(13331))

# def romanToInt(s):
#     roman = {
#         "I": 1,
#         "V": 5,
#         "X": 10,
#         "L": 50,
#         "C": 100,
#         "D": 500,
#         "M": 1000
#     }
#     total = 0
#     s = s.replace("IV", "IIII").replace("IX", "VIIII")
#     s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#     s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#     for symbol in s:
#         total += roman[symbol]
#     return total
#
#
# print(romanToInt("MCMXCIV"))

from random import shuffle


# def makeDeck():
#     colors = list('rgby')
#     numbers = list(range(1, 10))
#     deck = []
#     for color in colors:
#         for number in numbers:
#             deck.append(f'{number}{color}')
#     return deck
#
#
# def deal(deck, players=2, cards=7):
#     hands = [[] for _ in range(players)]
#     for _ in range(cards):
#         for hand in hands:
#             hand.append(deck.pop())
#     pile = [deck.pop()]
#     return hands, pile
#
#
# def draw(deck, playerHand):
#     card = deck.pop()
#     playerHand.append(card)
#     return card
#
#
# def discard(pile, playerHand, playerCard):
#     pile.append(playerCard)
#     playerHand.remove(playerCard)
#
#
# def match(pile, playerHand):
#     top_card = pile[-1]
#     for card in playerHand:
#         if card[0] == top_card[0] or card[1] == top_card[1]:
#             return card
#     return None
#
#
# def play(deck, pile, playerHand):
#     matching_card = match(pile, playerHand)
#     if matching_card:
#         discard(pile, playerHand, matching_card)
#     else:
#         draw_card = draw(deck, playerHand)
#         matching_card = match(pile, playerHand)
#         if matching_card:
#             discard(pile, playerHand, matching_card)
#     return len(playerHand) == 0
#
#
# def supervisor(deck, pile, hands, pause=True):
#     while True:
#         for i, hand in enumerate(hands):
#             if pause:
#                 input(' ...\n')
#             if play(deck, pile, hand):
#                 print(f"\nPlayer #{i} wins!")
#                 return i
#             print(f'PLAYER #{i}:\n\thand= {hand}')
#             print(f'\ttop of pile: {pile[-3:]}')
#             print(f'\tend of deck: {deck[-4:]}', end='')
#             print(f'\n#{i}: end of round hand= {hand}')
#             print(f'          top of pile= {pile[-1]}\n')
#
#
# def initialize(nPlayers, nCards):
#     deck = makeDeck()
#     shuffle(deck)
#     hands, pile = deal(deck, nPlayers, nCards)
#     return deck, pile, hands
#
#
# if __name__ == "__main__":  #
#     '''
#     UNCOMMENT THE LINES BELOW TO RUN A SMALL SIMULATION OF THE GAME
#     Larger simulations are possible by increasing the number of players
#     and/or the number of cards per hand.  The game is limited by the
#     number of cards in the deck.  The product of the number of players
#     and the number of cards per hand must be less than 34 to get a game started.
#     For example, dealing 8-card hands to 4 players would leave only 3 cards in
#     the deck to draw from and the deck may need to be replenished soon after
#     the game starts.  To handle larger games, you can modify play() can call
#     makeDeck() and shuffle() to get cards to add to the existing deck when its
#     length is 1.
#     '''
#
#     deck, pile, hands = initialize(2, 3)  # two players / 3 cards
#     print(f'{hands= }')
#     print(f'{pile= }\n')
#     winner = supervisor(deck, pile, hands, False)  # True to pause before each play
#     print(f'\nWinning hand is #{winner}!\n')
#     print('\n*** RESULTS ***\n')
#     for i, hand in enumerate(hands):
#         print(f'player #{i}: {hand= } {"WINNER!" if not hand else ""}')
#     input("The game is over.  Press Enter to continue with formal tests.")
#
#     '''
#     FORMAL FUNCTION TESTING
#     '''
#     ### MAKEDECK TESTS ###
#     deck = makeDeck()
#     s = "makeDeck() failed!"
#     # two different methods to separate numbers and colors for all cards
#     # map() or list comprehension ... which is best?
#     _c = [c for n, c in deck]  # list comprehension for colors
#     _c = list(map(lambda x: x[-1], deck))  # lambda returns the color of each card
#     _n = [n for n, c in deck]  # list comprehension for numbers
#     _n = list(map(lambda x: x[0], deck))  # lambda returns the number of each card
#
#     assert len(deck) == 36, f'{s} deck not 36 cards long.'  # check deck length
#     # check number of each color
#     assert _c.count('r') == _c.count('g') == _c.count('b') == _c.count('y') == 9, \
#         f"{s} bad color"
#     # check number of each digit
#     assert _n.count('1') == _n.count('2') == _n.count('3') == 4, f'{s} bad digit 1..3'
#     assert _n.count('4') == _n.count('5') == _n.count('6') == 4, f'{s} bad digit 4..6'
#     assert _n.count('7') == _n.count('8') == _n.count('9') == 4, f'{s} bad digit 7..9'
#     print("makedeck() tests passed!\n------------------------\n")
#
#     ### DEAL TESTS ###
#     s = "deal() failed!"
#     deck = ['xx', '4z', '4y', '4x', '3z', '3y', '3x', '2z', '2y', '2x', '1z', '1y', '1x']
#     [hx, hy, hz], pile = deal(deck, 3, 4)  # 3 players 4 cards each
#     assert deck == [], f"{s} bad deck\n\t{card=}\n\t{deck=}\n\t{hand=}"
#     assert set(hx) == {'1x', '2x', '3x', '4x'}, f"{s} bad hand #1\n\t{deck=}\n\t{hx=}"
#     assert set(hy) == {'1y', '2y', '3y', '4y'}, f"{s} bad hand #2\n\t{deck=}\n\t{hy=}"
#     assert set(hz) == {'1z', '2z', '3z', '4z'}, f"{s} bad hand #3\n\t{deck=}\n\t{hz=}"
#     assert pile == ['xx'], f"{s} bad pile #3\n\t{deck=}\n\t{pile=}"
#     print("deal() tests passed!\n--------------------\n")
#
#     #### MATCH TESTS ####
#     s = "match() failed!"
#     pile, hand = ['6g', '2r'], ['3b', '2y']  # number match
#     assert match(pile, hand) == '2y', f"Number {s}\n\t{pile=}\n\t{hand=}"
#     pile, hand = ['6g', '2r'], ['3r', '4y']  # color match
#     assert match(pile, hand) == '3r', f"Color {s}\n\t{pile=}\n\t{hand=}"
#     pile, hand = ['6g', '2r'], ['6g', '7y']  # no match
#     assert match(pile, hand) == None, f"{s}\n\t{pile=}\n\t{hand=}"
#     print(f"match() tests passed!\n---------------------\n")
#
#     #### DISCARD TESTS ####
#     s = "discard() failed!"
#     pile, hand, card = ['6g', '2r'], ['7r', '2y', '3b'], '2y'  # test data
#     result = discard(pile, hand, card)
#     _rpt = f"\n\t{card=}\n\t{pile=}\n\t{hand=}"
#     assert pile == ['6g', '2r', '2y'], f"{s} bad pile" + _rpt
#     assert set(hand) == {'7r', '3b'}, f"{s} bad hand" + _rpt
#     assert result == None, f"{s} bad return value" + _rpt
#     print("discard() tests passed!\n-----------------------\n")
#
#     #### DRAW TESTS ####
#     s = "draw() failed!"
#     deck, hand = ['6g', '2r', '1y'], ['7r', '3b']  # test data
#     result = draw(deck, hand)
#     _rpt = f"\n\t{deck=}\n\t{hand=}"
#     assert deck == ['6g', '2r'], f"{s} bad deck" + _rpt
#     assert set(hand) == {'7r', '3b', '1y'}, f"{s} bad hand" + _rpt
#     assert result == '1y', f"{s} bad return value\n\t{result=}" + _rpt
#     print("draw() tests passed!\n--------------------\n")
#
#     ### PLAY TESTS ###
#     s = "play() failed!"
#     # color match continue
#     deck, pile, hand = ['6g', '2r', '1y'], ['1r', '3b'], ['7r', '2b', '9y']
#     result = play(deck, pile, hand)
#     _rpt = f"\n\t{deck=}\n\t{pile=}\n\t{hand=}"
#     assert deck == ['6g', '2r', '1y'], f"{s} bad deck" + _rpt
#     assert pile == ['1r', '3b', '2b'], f"{s} bad pile" + _rpt
#     assert set(hand) == {'7r', '9y'}, f"{s} bad hand" + _rpt
#     assert result == False, f"{s} bad result" + _rpt
#     # number match continue
#     deck, pile, hand = ['6g', '2r', '1y'], ['1r', '3b'], ['9y', '3r', '6y']
#     result = play(deck, pile, hand)
#     _rpt = f"\n\t{deck=}\n\t{pile=}\n\t{hand=}"
#     assert deck == ['6g', '2r', '1y'], f"{s} bad deck" + _rpt
#     assert pile == ['1r', '3b', '3r'], f"{s} bad pile" + _rpt
#     assert set(hand) == {'6y', '9y'}, f"{s} bad hand" + _rpt
#     assert result == False, f"{s} bad result" + _rpt
#     # no match continue
#     deck, pile, hand = ['6g', '2r', '1y'], ['1r', '3b'], ['7r', '9y']
#     result = play(deck, pile, hand)
#     _rpt = f"\n\t{deck=}\n\t{pile=}\n\t{hand=}"
#     assert deck == ['6g', '2r'], f"{s} bad deck" + _rpt
#     assert pile == ['1r', '3b'], f"{s} bad pile" + _rpt
#     assert set(hand) == {'9y', '7r', '1y'}, f"{s} bad hand" + _rpt
#     assert result == False, f"{s} bad result" + _rpt
#     # color match done
#     deck, pile, hand = ['6g', '2r', '1y'], ['1r', '3b'], ['2b']
#     result = play(deck, pile, hand)
#     _rpt = f"\n\t{deck=}\n\t{pile=}\n\t{hand=}"
#     assert deck == ['6g', '2r', '1y'], f"{s} bad deck" + _rpt
#     assert pile == ['1r', '3b', '2b'], f"{s} bad pile" + _rpt
#     assert hand == [], f"{s} bad hand" + _rpt
#     assert result == True, f"{s} bad result" + _rpt
#     print("play() tests passed!\n--------------------\n")

# mess = [['o', 'c', 'h', 'c', 'a', 64, 'd'],
#         ['o', 'o', 91, 'y', 'y', 'e', 'i'],
#         ['u', 'r', 'o', 'u', 'y', 46, 'e'],
#         ['u', 'y', 'e', 'r', 19, 't', 't'],
#         ['a', 'h', 55, 's', 'n', 'i', 's'],
#         [27, 'u', 'r', 't', 'r', 'r', 'n'],
#         [72, 'a', 'c', 'p', 't', 'g', 'm']]
#
# # Rotation function
# def rotate(lst):
#     int_indices = [i for i, x in enumerate(lst) if isinstance(x, int)]
#     for idx in int_indices:
#         while lst[idx] != idx + 1:
#             popped = lst.pop(idx)
#             lst.insert(0, popped)
#
# # Step 1: Rotation for alignment
# for sublist in mess:
#     rotate(sublist)
#
# # Step 2: Sort and build words
# words = []
# for sublist in sorted(mess, key=lambda x: [i for i, c in enumerate(x) if isinstance(c, int)]):
#     word = ''.join(str(c) if isinstance(c, int) else c for c in sublist)
#     words.append(word)
#
# # Display the discovered words
# for word in words:
#     print(word)

import csv
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter

# Function to read data from CSV and convert values
def read_and_convert_data(filename):
    data = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header row

        for row in reader:
            commodity, date_str, farm, atlanta, chicago, nyc, la = row

            # Convert date to datetime object
            date = datetime.strptime(date_str, "%m/%d/%Y")

            # Remove dollar signs and spaces from prices
            prices = [float(price.replace('$', '').strip()) for price in [atlanta, chicago, nyc, la]]

            data.append([commodity, date, farm] + prices)

    return data


# Function to filter data for a specific commodity and location
def filter_data(data, commodity, location):
    filtered_data = [record for record in data if record[0] == commodity and record[2] == location]
    return filtered_data

# Function to plot a line graph
def plot_line_graph(dates, prices, commodity, location):
    fig, ax = plt.subplots()
    ax.plot(dates, prices, label=f'{commodity} Prices in {location}')

    # Format x-axis as dates
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    # Add labels and legend
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title(f'{commodity} Prices Over Time ({location})')
    ax.legend()

    # Show the plot
    plt.show()

# Example usage
filename = 'produce_csv.csv'
data = read_and_convert_data(filename)

# Choose a commodity and location for filtering
commodity_to_filter = 'Oranges'
location_to_filter = 'Chicago'

# Filter data
filtered_data = filter_data(data, commodity_to_filter, location_to_filter)

# Separate dates and prices for plotting
dates = [record[1] for record in filtered_data]
prices = [record[3] for record in filtered_data]

# Plot the line graph
plot_line_graph(dates, prices, commodity_to_filter, location_to_filter)
