'''
Author: Saikumar Srinivas
Filename: pred-sai-02.py
Purpose: Linear Prediction Problem
Revisions:
    00:Announce & get values from the user
    01:Caclculating the difference from the second number
    02:Printing the predicted final value
'''
### STEP 1: Announce, promt,& take response
# announce
print("Prediction of Linear value\n")
# prompt user to enter the sequence
# accepting float values 
first_number = float(input("Enter the first integer: "))
second_number = float(input("Enter the second integer: "))
### STEP 2: Compute the difference
difference = second_number - first_number
next_number = second_number + difference
### STEP 3: Print the result i.e Next number
print(f"The next number in the sequence is: {next_number}")
