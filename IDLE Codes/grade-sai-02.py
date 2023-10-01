'''
Author: Saikumar Srinivas
Filename: grade-sai-02.py
Purpose: Letter Grade Project
Revisions:
    00:Announce & get values from the user
    01:Defining a function which return values based on user input 
    02:Printing the letter grade
'''
### STEP 1: Announce, promt
# announce
print("Lets convert your Numerical score to Letter Grade\n")
### STEP 2: Get a numerical score from the user
score = float(input("Enter the numerical score: "))
### STEP 3:Define a function to convert a numerical score to a letter grade
def letterGrade(score):
    # Check if the score is greater than or equal to 95
    if score >= 95:
        return 'A+'
    # Check if the score is between 90 and 94
    elif score >= 90:
        return 'A'
    # Check if the score is between 85 and 89
    elif score >= 85:
        return 'A-'
    # Check if the score is between 80 and 84
    elif score >= 80:
        return 'B+'
    # Check if the score is between 75 and 79
    elif score >= 75:
        return 'B'
    # Check if the score is between 70 and 74
    elif score >= 70:
        return 'B-'
    # Check if the score is between 65 and 69
    elif score >= 65:
        return 'C+'
    # Check if the score is between 60 and 64
    elif score >= 60:
        return 'C'
    # Check if the score is between 55 and 59
    elif score >= 55:
        return 'C-'
    # If none of the above conditions are met, return 'F'
    else:
        return 'F'

### STEP 4: Print the letter grade corresponding to the input score
print('The letter grade for', score, 'percent is', letterGrade(score) + '.')
