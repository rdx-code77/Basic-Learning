'''
Author: Saikumar Srinivas
Filename: rarea-sai-02.py
Purpose: Compute the Area of a Rectangle
Revisions:
    00:Announce & get values from the user
    01:Calculate the area 
    02:Printing the result
'''
### STEP 1: Announce, promt,& take response
# announce
print("Area of a Rectangle\n")
# prompt user to enter the dimensions of a rectangle
# accepting float values 
height = float(input("Enter the height of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
### STEP 2: Compute the area of a rectangle
area = height * width
### STEP 3: Print the result
print(f"The area of a {height} by {width} rectangle is {area}.")
'''
I have gone ahead & used multiple test cases to check its efficiency, You can try it too!!!
'''
