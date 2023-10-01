'''
Author: Saikumar Srinivas
Filename: coin-sai-05.py
Purpose: Coin Counter
Revisions:
    00:Announce, promt
    01:Taking input from the user & defining the values of the coins
    02:Iterating over the user input & incrementing the number & value of coins & storing the total value
    03:Formatting the coin report
    04:Assigning coin values to formatted dictionary
    05:Calculating the sum & printing the value in formatted form
'''
### STEP 1: Announce, promt
# announce
print("Program to count coins and calculate values\n")

### STEP 2: Get the input string from the user
input_string = input("Enter the coin string: ")

### STEP 3: Initialize dictionaries to store coin counts and values
coin_counts = {'p': 0, 'n': 0, 'd': 0, 'q': 0, 'h': 0}
coin_values = {'p': 0.01, 'n': 0.05, 'd': 0.10, 'q': 0.25, 'h': 0.50}

### STEP 4: Process the input string
total_value = 0.0
for coin in input_string:
    if coin in coin_counts:
        coin_counts[coin] += 1
        total_value += coin_values[coin]

### STEP 5: Display the results in a neat report format
# Coin Counter Report
print("=" * 40)
print("Coin Counter Report".center(40))
print("=" * 40)

### STEP 6: Print column headers
print("{:<12} {:<8} {:<10} {:<10}".format("Coin", "Value", "Number", "Amount"))
print("{:<12} {:<8} {:<10} {:<10}".format("====", "=====", "======", "======"))

for coin_type, count in coin_counts.items():
    coin_name = {
        'p': 'Pennies',
        'n': 'Nickels',
        'd': 'Dimes',
        'q': 'Quarters',
        'h': 'Half-dollars'}[coin_type]
    coin_value = coin_values[coin_type]
    total_coin_value = coin_value * count

### STEP 7: Format the output to align columns
    print("{:<12} {:<8} {:<10} ${:<.2f}".format(coin_name, f"${coin_value:.2f}:", count, total_coin_value))

print("=" * 40)

### STEP 8: Calculate and print the total value
total_value = sum(coin_values[coin_type] * count for coin_type, count in coin_counts.items())
print("{:<32} ${:<.2f}".format("Total amount:", total_value))

