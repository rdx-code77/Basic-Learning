"""
Author: Saikumar Srinivas
Filename: finalProject_sai_09.py
Purpose: Final Project
Revisions:
    00: Announce the project description
    01: Created initial script structure, reading CSV data, and converting data types.
    02: Added user input functionality for selecting products, dates, and cities.
    03: Implemented data filtering based on user input criteria.
    04: Generated bar graphs using Plotly for selected data.
    05: Enhanced data validation for user inputs to prevent unexpected errors.
    06: Optimized data processing loops for better performance.
    07: Improved visualization aesthetics and layout in the generated graphs.
    08: Added more detailed error messages for user input handling.
    09: Implemented additional checks to handle edge cases and prevent crashes.
"""
import csv  # Module for reading and writing CSV files
from datetime import datetime  # Module to handle date and time information
import plotly.offline as py  # importing plotly to draw graphs
import plotly.graph_objs as go

print("==============================")
print("Analysis of Commodity Data")
print("==============================\n")

# STEP1: Reading the data from the CSV file
with open('produce_csv.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]

# STEP2: Converting the data to appropriate data types
modData = []
# iterating through the list
for row in data:
    newRow = list()
    for item in row:
        # Checking for currency values (prices)
        if "$" in item:
            # replacing the $ sign with null value
            newRow.append(float(item.replace("$", "")))
        # Checking for date values
        elif "/" in item:
            # changing the sting format of date into requited date format
            newRow.append(datetime.strptime(item, '%m/%d/%Y'))
        else:
            # Keeping non-price and non-date values as they are
            newRow.append(item)
    # Appending the modified row to modData
    modData.append(newRow)

# STEP3: Extracting locations and forming individual records
locations = modData.pop(0)[2:]  # Removing header and extracting locations
records = list()  # creating an empty list to store new data
for row in modData:
    newRow = row[:2]  # Extracting commodity and date
    # Creating records for each location and its respective price
    for loc, price in zip(locations, row[2:]):
        # new data is added to record
        records.append(newRow + [loc, price])

# STEP4: catching the index exception when user enter out of bound index
try:
    city = sorted(locations)  # sorting the city in file
    commodity = sorted(set([i[0] for i in modData]))  # retrieving and sorting the product
    dates = sorted(set([i[1] for i in modData]))  # retrieving and sorting the dates

    # Displaying and accepting user input for Product
    [print(f"<{i}> {j}") for i, j in enumerate(commodity)]
    b = input("Enter product numbers separated by spaces:  ").split()
    commodity_name = [commodity[int(i)] for i in b]
    # Formatting selected product names as a string
    selected_products = ', '.join(commodity_name)  # Joining the selected product names with ', '
    # Printing the selected products
    print(f"Selected products: {selected_products}\n")

    # Displaying and accepting user input for Dates
    [print(f"<{i}> {str(j).split()[0]}") for i, j in enumerate(dates)]
    print(f"Earliest available date is: {min(dates)}")
    print(f"Latest available date is: {max(dates)}\n")
    c = input("Enter start/end date numbers separated by a space:  ").split()
    dates_value = [dates[int(i)] for i in c]
    # Formatting selected dates as a string
    selected_start_date = str(dates_value[0]).split()[0] if dates_value else ""
    selected_end_date = str(dates_value[1]).split()[0] if len(dates_value) > 1 else ""
    # Printing the selected dates
    print(f"Selected date range: {selected_start_date} to {selected_end_date}\n")

    # Displaying and accepting user input for city
    [print(f"<{i}> {j}") for i, j in enumerate(city)]
    a = input("Enter location numbers separated by spaces:  ").split()
    city_value = [city[int(i)] for i in a]
    city_value_print = city_value
    # Formatting selected city names as a string
    selected_cities = ', '.join(city_value)  # Joining the selected city names with ', '
    # Printing the selected cities
    print(f"Selected cities: {selected_cities}\n")

    # Creating the final list based for user selected condition
    final_list_graph = [i for i in records if (
            (i[0] in commodity_name) and (min(dates_value) <= i[1] <= max(dates_value)) and (
            i[2] in city_value_print))]
    # Creating dictionary where location is the key as it is the filtering condition of graph
    final_list_graph_dict = {i: [] for i in city_value}

    # Iterating through each city in the dictionary of city values
    for city_value in final_list_graph_dict:
        # Iterating through each product in the list of commodity names
        for product_name in commodity_name:
            # Filtering prices for a specific product and city combination
            prices = [k[3] for k in final_list_graph if k[0] == product_name and k[2] == city_value]

            # Calculating the average price for the filtered prices
            # If prices exist, calculate the average; otherwise, set it to 0
            average_price = sum(prices) / len(prices) if prices else 0

            # Appending the calculated average price to the respective city's list in final_list_graph_dict
            final_list_graph_dict[city_value].append(average_price)

    value = []
    for city_value, average in final_list_graph_dict.items():
        value.append(go.Bar(x=commodity_name, y=average, name=city_value))

    print(f'{len(final_list_graph)} records have been selected.\n')
    print("RECORDS SELECTED  ...\n")
    [print(f"<{i}> {j}") for i, j in enumerate(final_list_graph)]

    my_dict = {}  # creating an empty dictionary
    for loc in final_list_graph:
        if loc[0] + "-" + loc[2] in my_dict:  # creating product and place as one unit and storing as key
            my_dict[loc[0] + "-" + loc[2]] = my_dict[loc[0] + "-" + loc[2]] + 1  # incrementing the count if it's there
        elif loc[0] + "-" + loc[2] not in my_dict:
            my_dict[loc[0] + "-" + loc[2]] = 1  # assigning the value as one if it's not there and encountered as 1

    for loc in my_dict:
        print(f"{str(my_dict[loc])} prices for {loc.split('-')[0]} in {loc.split('-')[1]}")  # printing the result

    header = 'Produce Prices from ' + datetime.strftime(min(dates_value), "%Y-%m-%d") + ' through ' + datetime.strftime(
        max(dates_value), "%Y-%m-%d")

    layout = go.Layout(title=dict(text=header, x=0.50, xanchor="center"),
                       xaxis=dict(title='Product'),  # formatting x-axis
                       yaxis=dict(title='Average Price', tickprefix="$", tickformat=".2f"),  # formatting y-axis
                       font=dict(size=20)  # formatting font
                       )

    # Plot the graph and saving it in a html format
    fig = go.Figure(data=value, layout=layout)
    py.plot(fig, filename='sai_final_project.html')

# catching the Index exception
except IndexError:
    print("Entered index value is not in list. Please Try again !")
