'''
Author: Saikumar Srinivas
Filename: revisedavg-sai-03.py
Purpose: Revised Average
Revisions:
    00:Announce, promt
    01:Taking input from user & prompting to press <enter>
    02:Using the walrus operator & accepting user inputs till the condition turns false
    03:Calculating the average & then displaying it on condition basis
'''
### STEP 1: Announce, promt
# announce
print("Program to compute the average of the numbers provided.\n")

### STEP 2: Initialize an empty list to store the numbers
numbers = []  

print("Enter each number followed by <enter>.\nWhen you are done, just hit <enter> in response to the prompt.\n")

### STEP 3:
# Prompt the user to enter a number and simultaneously read their input.
# The walrus operator (:=) allows us to assign the input to the variable user_input.
while user_input := input("Enter a number: "):
    # This loop will continue as long as the user enters a non-empty input (i.e., not just pressing Enter).
    # When the user enters an empty input (e.g., presses Enter without typing a number),
    # the loop will exit because the input will be evaluated as a false value.

### STEP 4: Convert and append the input to the list & print the result
    numbers.append(float(user_input))  
print(f"\nYou entered {len(numbers)} numbers.\nThe average is {sum(numbers) / len(numbers):.1f}." if numbers else "No numbers entered.")

