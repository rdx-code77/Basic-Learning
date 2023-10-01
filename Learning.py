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

def normalize(data, norm2Peak=True):
    # Function to normalize data
    # Args:
    #   data: List of numbers representing character counts
    #   norm2Peak: Boolean, True for normalizing to peak, False for normalizing to area (default is True)
    # Returns:
    #   List of floats representing normalized counts

    if norm2Peak:
        # Normalize to peak
        max_count = max(data)
        return [count / max_count for count in data]
    else:
        # Normalize to area
        total_count = sum(data)
        return [count / total_count for count in data]


def plotBars(counts, alphabet, barLength=20):
    # Function to plot histogram bars
    # Args:
    #   counts: List of numbers representing character counts
    #   alphabet: String representing the alphabet
    #   barLength: Optional integer specifying the maximum length of a bar (default is 20)

    # Find the character(s) with the maximum frequency
    max_count = max(counts)
    max_chars = [char for char, count in zip(alphabet, counts) if count == max_count]

    # Print the histogram
    print("Character Histogram:")
    for char, count in zip(alphabet, counts):
        normalized_count = int(count * barLength)
        histogram_bar = '=' * normalized_count
        print(f"{char}: {histogram_bar}")

    # Print the character(s) with the highest frequency
    print("\nCharacter(s) with the highest frequency:")
    for char in max_chars:
        percent = counts[alphabet.index(char)] / sum(counts) * 100
        print(f"{char}: {percent:.2f}%")


def main():
    # Input text
    input_text = input("Enter text to analyze: ")

    # Convert input text to uppercase
    input_text = input_text.upper()

    # Define the alphabet
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Initialize a list to store character counts
    char_counts = []

    # Count the characters in the input text
    for char in alphabet:
        count = input_text.count(char)
        char_counts.append(count)

    # Normalize the data to peak
    pkNormData = normalize(char_counts, norm2Peak=True)

    # Normalize the data to area
    aNormData = normalize(char_counts, norm2Peak=False)

    # Print the histogram
    plotBars(pkNormData, alphabet, barLength=20)


if __name__ == "__main__":
    main()
