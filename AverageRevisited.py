print("Program to compute the average of the numbers provided.")

numbers = []  # Initialize an empty list to store the numbers

# Use a while loop to continuously prompt for numbers
while True:
    user_input = input("Enter a number (or press Enter to calculate the average): ")

    # Check if the user pressed Enter without typing a number
    if not user_input:
        break  # Exit the loop if the user pressed Enter

    try:
        number = float(user_input)  # Convert the input to a float
        numbers.append(number)  # Add the number to the list
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Check if any numbers were entered
if numbers:
    average = sum(numbers) / len(numbers)  # Calculate the average
    print(f"You entered {len(numbers)} numbers.")
    print(f"The average is {average:.1f}.")
else:
    print("No numbers were entered.")


numbers = []  # Initialize an empty list to store the numbers

while user_input := input("Enter a number (or press Enter to calculate the average): ").strip():
    try:
        numbers.append(float(user_input))  # Convert and append the input to the list
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"You entered {len(numbers)} numbers.\nThe average is {average:.1f}.")
else:
    print("No numbers were entered.")
