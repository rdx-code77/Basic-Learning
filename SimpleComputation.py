def calculate_rectangle_area(height, width):
    return height * width


try:
    height = float(input("Enter the height of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area = calculate_rectangle_area(height, width)
    print(f"The area of a {height} by {width} rectangle is {area}.")

except ValueError:
    print("Please enter valid numeric values for height and width.")
