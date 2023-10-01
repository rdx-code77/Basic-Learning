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
print("Program to compute the average of the numbers provided.")

### STEP 2: Ask the user how many numbers to average
number_count = int(input("How many numbers would you like to average? "))

### STEP 3: Initialize variables for sum 
total = 0

### STEP 4: Use a loop to get numbers and accumulate the total(sum)
for i in range(1, number_count + 1):
    num = float(input(f"Enter number {i}: "))
    total += num

### STEP 5: Calculate the average
average = total / number_count

### STEP 6: Display the average
print(f"The average is {average}.")
