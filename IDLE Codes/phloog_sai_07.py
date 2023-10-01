'''
Author: Saikumar Srinivas
Filename: phloog_sai_07.py
Purpose: Calculate Grades
Revisions:
    00: Announce the start of the program
    01: Define a function findGrade() to calculate grades
    02: Sort the grades in ascending order
    03: Determine how many grades to exclude
    04: Exclude the lowest grades
    05: Compute the average of the remaining grades
    06: Determine the letter grade based on the average
    07: Return the average and letter grade as a tuple
'''

### STEP 1: Announce the start of the program
print('Program to calculate grades for Dr. Phloog\n')

### STEP 2: Define a function findGrade() to calculate grades
def findGrade(grades):
    # STEP 3: Sort the grades in ascending order
    grades.sort()

    # STEP 4: Determine how many grades to exclude
    low_excluded = len(grades) // 3

    # STEP 5: Exclude the lowest grades
    excluded_grades = grades[low_excluded:]

    # STEP 6: Compute the average of the remaining grades
    average = sum(excluded_grades) / len(excluded_grades)

    # STEP 7: Determine the letter grade based on the average
    if average < 80:
        letter = 'X'
    elif average > 90:
        letter = 'Z'
    else:
        letter = 'Y'

    # STEP 8: Return the average and letter grade as a tuple
    return (average, letter)

grades = []
grades.append([50,100,60]) # [80.00,'Y']
grades.append([50,100,50,50,100,50,50,100,50]) # [75.00,'X']
grades.append([65,100,22,89,0,100,92,78,87,97]) # [91.86,'Z']
grades.append([90,70,60,100,65,95,27,55,79,60]) # [79.86,'X']
grades.append([65,100,22,89,45,92,78,87]) # [85.17,'Y']
for item in grades:
    grade = findGrade(item)
    print(f"{grade[0]:6.2f} --> {grade[1]} ") 
