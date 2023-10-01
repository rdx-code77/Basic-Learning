def predict_next_number(first, second):
    difference = second - first
    next_number = second + difference
    return next_number


try:
    first_number = int(input("Enter the first integer: "))
    second_number = int(input("Enter the second integer: "))

    next_number = predict_next_number(first_number, second_number)
    print(f"The next number in the sequence is: {next_number}")

except ValueError:
    print("Please enter valid integers.")
