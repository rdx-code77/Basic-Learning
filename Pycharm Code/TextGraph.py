print("Draw a bar graph using characters")
# Prompt the user to enter up to 10 positive whole numbers less than 50
user_input = input("Enter up to 10 positive whole numbers less than 50: ")

# Split the input into a list of individual strings representing numbers
numbers = user_input.split()

# Initialize a variable to keep track of the valid numbers entered
valid_count = 0

# Maximum number of characters for each bar
max_width = 50

# Iterate through the list of numbers
for number in numbers:
    try:
        n = int(number)
        if 1 <= n <= 50:  # Check if the number is within the valid range
            valid_count += 1
            bar = n * "="  # Create the bar using '=' characters
            print(bar)
        else:
            print("?")  # Invalid number, print '?'
    except ValueError:
        print("?")  # Invalid input, print '?'

# Check if no valid numbers were entered
if valid_count == 0:
    print("No valid numbers entered.")
