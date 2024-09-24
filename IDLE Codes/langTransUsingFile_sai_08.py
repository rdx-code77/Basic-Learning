import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
file_path = 'produce_csv.csv'  # Replace 'your_file_path_here.csv' with your file path
data = pd.read_csv(file_path)

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')

# Filter data for Oranges in Chicago
filtered_data = data[(data['Commodity'] == 'Oranges') & (data['Farm'] == 'Chicago')]

# Plotting prices of Oranges in Chicago over time
plt.figure(figsize=(10, 6))
plt.plot(filtered_data['Date'], filtered_data['Chicago'].replace('[\$,]', '', regex=True).astype(float), marker='o', linestyle='-', color='blue')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Price of Oranges in Chicago Over Time')
plt.grid(True)
plt.tight_layout()
plt.show()
