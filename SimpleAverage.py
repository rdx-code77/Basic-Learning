print("Program to compute the average of the numbers provided.")
# Ask the user how many numbers to average
num_count = int(input("How many numbers would you like to average? "))

# Initialize variables for sum and count
total = 0

# Use a loop to get numbers and accumulate the sum
for i in range(1, num_count + 1):
    num = float(input(f"Enter number {i}: "))
    total += num

# Calculate the average
average = total / num_count

# Display the average3
print(f"The average is {average}.")
