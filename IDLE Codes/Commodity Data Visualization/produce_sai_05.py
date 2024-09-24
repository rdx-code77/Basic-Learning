"""
Author: Saikumar Srinivas
Filename: produce_sai_05.py
Purpose: Commodity data, filtering and visualization
Revisions:
    00: Created initial script structure, reading CSV data, and converting data types.
    01: Implemented data filtering to extract specific information for Oranges in Chicago.
    02: Prepared data for visualization by organizing dates and prices for Oranges in Chicago.
    03: Developed plot using Matplotlib to showcase the price trend of Oranges in Chicago over time.
    04: Enhanced plot readability by adding axis labels and formatting y-axis ticks as currency.
    05: Improved visualization aesthetics by including a title and legend for clear representation.
"""
import csv  # Module for reading and writing CSV files
from datetime import datetime  # Module to handle date and time information
import matplotlib.pyplot as plt  # Module to create visualizations (plots)
import matplotlib.ticker as mtick  # Module to format plot ticks

# Reading the data from the CSV file
with open('produce_csv.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]

# Converting the data to appropriate data types
modData = []
for row in data:
    newRow = list()
    for item in row:
        # Checking for currency values (prices)
        if "$" in item:
            # Converting currency values to floats
            newRow.append(float(item.replace("$", "")))
        # Checking for date values
        elif "/" in item:
            # Converting date strings to datetime objects
            newRow.append(datetime.strptime(item, '%m/%d/%Y'))
        else:
            # Keeping non-price and non-date values as they are
            newRow.append(item)
    # Appending the modified row to modData
    modData.append(newRow)

# Extracting locations and forming individual records
locations = modData.pop(0)[2:]  # Removing header and extracting locations
records = list()
for row in modData:
    newRow = row[:2]  # Extracting commodity and date
    # Creating records for each location and its respective price
    for loc, price in zip(locations, row[2:]):
        records.append(newRow + [loc, price])

# Filtering data for Oranges in Chicago
select = list(filter(lambda x: x[0] == "Oranges" and x[2] == "Chicago", records))

# Extracting dates and prices for Oranges in Chicago
dates = [x[1] for x in select]   # Dates for Oranges in Chicago
prices = [x[3] for x in select]  # Prices for Oranges in Chicago

# Creating and customizing the plot
fig = plt.figure()
ax = fig.add_subplot(111)

# Plotting dates against prices for Oranges in Chicago
ax.plot(dates, prices, label='Oranges in Chicago')

# Setting x-axis and y-axis labels
ax.set_xlabel('Date')
ax.set_ylabel('Price in dollars')

# Formatting y-axis ticks to display as currency
fmt = '${x:,.2f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

# Setting title
plt.title('Prices of Oranges in Chicago over Dates')

# Displaying legend
plt.legend()

# Displaying the plot
plt.show()

