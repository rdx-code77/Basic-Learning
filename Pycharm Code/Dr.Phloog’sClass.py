def findGrade(grades):
    # Sort the grades in ascending order
    grades.sort()

    # Determine how many grades to exclude
    num_to_exclude = len(grades) // 3

    # Exclude the lowest grades
    excluded_grades = grades[num_to_exclude:]

    # Compute the average of the remaining grades
    average = sum(excluded_grades) / len(excluded_grades)

    # Determine the letter grade
    if average < 80:
        letter = 'X'
    elif average > 90:
        letter = 'Z'
    else:
        letter = 'Y'

    return (average, letter)


print('Program to calculate grades for Dr. Phloog\n')
# CODE TO TEST THE FUNCTION
grades = []
grades.append([50, 100, 60])  # [80.00,'Y']
grades.append([50, 100, 50, 50, 100, 50, 50, 100, 50])  # [75.00,'X']
grades.append([65, 100, 22, 89, 0, 100, 92, 78, 87, 97])  # [91.86,'Z']
grades.append([90, 70, 60, 100, 65, 95, 27, 55, 79, 60])  # [79.86,'X']
grades.append([65, 100, 22, 89, 45, 92, 78, 87])  # [85.17,'Y']
for item in grades:
    grade = findGrade(item)
    print(f"{grade[0]:6.2f} --> {grade[1]} ")
