print("Program to count coins and calculate values")

# Initialize dictionaries to store coin counts and values
coin_counts = {'p': 0, 'n': 0, 'd': 0, 'q': 0, 'h': 0}
coin_values = {'p': 0.01, 'n': 0.05, 'd': 0.10, 'q': 0.25, 'h': 0.50}

# Get the input string from the user
input_string = input("Enter the coin string: ")

# Process the input string
total_value = 0.0
for coin in input_string:
    if coin in coin_counts:
        coin_counts[coin] += 1
        total_value += coin_values[coin]

# Display the results in a neat report format
print("Coin Counter Report")
print("===================")
for coin_type, count in coin_counts.items():
    coin_name = {
        'p': 'Penny',
        'n': 'Nickel',
        'd': 'Dime',
        'q': 'Quarter',
        'h': 'Half-Dollar'}[coin_type]
    coin_value = coin_values[coin_type]
    total_coin_value = coin_value * count
    print(f"{coin_name} Count: {count:2d}  Value: ${total_coin_value:.2f}")

print("===================")
print(f"Total Value: ${total_value:.2f}")
