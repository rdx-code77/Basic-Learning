'''
Author: Saikumar Srinivas
Filename: graph-sai-06.py
Purpose: TextGraph Program
Revisions:
    00:Announce, promt
    01:Taking the input from user
    02:Splitting the list to represent numbers
    03:Setting a fixed length of 50 characters
    04:Iterating over the numbers 
    05:Checking if the number is in the valid range
    06:Printing the characters
'''
### STEP 1: Announce, promt
# announce
print("Draw a bar graph using characters\n")

### STEP 2: Prompt the user to enter up to 10 positive whole numbers less than 50
response = input("Enter up to 10 positive whole numbers less than 50: ")

### STEP 3: Split the input into a list of individual strings representing numbers
numbers = response.split()

### STEP 4: Initialize a variable to keep track of the valid numbers entered
valid_num = 0

### STEP 5: Maximum number of characters for each bar
bar_length = 50

### STEP 6: Iterate through the list of numbers
for number in numbers:
    try:
        n = int(number)
        if 1 <= n <= bar_length:  # Check if the number is within the valid range
            valid_num += 1
            bar = n * "="  # Create the bar using '=' characters
            print(bar)
        else:
            print("?")  # Invalid number, print '?'
    except ValueError:
        print("?")  # Invalid input, print '?'

