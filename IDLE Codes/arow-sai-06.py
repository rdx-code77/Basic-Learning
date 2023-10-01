'''
Author: Saikumar Srinivas
Filename: arow-sai-06.py
Purpose: Double Arrow Pattern
Revisions:
    00:Announce, promt
    01:Checking if drawing canvas opens
    02:Setting up a turtle named tom
    03:Penup to navigate to center of screen
    04:Pendown to start the pattern
    05:Finally Penup to navigate turtle to center of screen
    06:Fixed autclose of canvas window
'''
### STEP 1: Announce, promt
# announce
print("Drawing Double Arrow\n")

### STEP 2: Import the turtle module for drawing
import turtle

### STEP 3: Create a canvas for drawing
canvas = turtle.Screen()

### STEP 4: Create a turtle named 'tom'
tom = turtle.Turtle()

### STEP 5: Set the drawing speed of 'tom'
tom.speed(1)

### STEP 6: Lift the pen up to move to a starting position
tom.penup()
tom.goto(-50, -50)

### STEP 7: Put the pen down to start drawing
tom.pendown()

### STEP 8: Draw the pattern
tom.forward(200)
tom.right(90)
tom.forward(50)
tom.left(135)
tom.forward(200)
tom.left(90)
tom.forward(200)
tom.left(135)
tom.forward(50)
tom.right(90)
tom.forward(200)
tom.right(90)
tom.forward(50)
tom.left(135)
tom.forward(200)
tom.left(90)
tom.forward(200)
tom.left(135)
tom.forward(50)
tom.right(90)

### STEP 9: Lift the pen up to move to a new position
tom.penup()
tom.forward(100)
tom.left(90)
tom.forward(100)
tom.right(90)

### STEP 10: Close the Turtle graphics window when clicked
canvas.exitonclick()
