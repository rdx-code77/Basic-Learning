import csv
'''
    Author: Saikumar Srinivas
    Filename: produce-exercise-template_sai.py
    Purpose: DATA HANDLING EXERCISE
    THE GOAL is to feel comfortable working with data records using
        LIST COMPREHENSIONS 
    YOU MAY consult any *non-human* reference material you like.
        DO NOT ask others on the internet to solve the problems for you.
    YOU MUST use the suggested method or a method demonstrated in class
        YOU MUST put your code in the space provided
        YOU MUST use the specified variable names
    OUTPUT containing CORRECT values is provided at the end of this file.
        YOUR CODE **must** replicate the output provided.
        To earn points, your results MUST correspond to those given.
        HARD-CODED solutions will receive a grade of 0
    16 out of the 17 challenges can be done using ONE LINE OF CODE
    Partial solutions will be accepted to earn points if they are CORRECT.
    DO NOT hard-code the answers.
    HARD-CODED print statements without calculation will have points DEDUCTED.
        Results must be computed.
        Formatted output will yield the most points.
    TO EARN THE MOST POINTS perform each operation using ONE source code line.
        Each result must be implemented in LESS THAN four source code lines.
    YOU MUST use this file and the data file provided
        DO NOT ALTER any of the comments
        DO NOT MODIFY the data file or the code that reads the data file.
    The file you submit MUST run WITHOUT ERROR MESSAGES.
'''
data = []
csvfile = open('produce_extra.csv','r')
reader = csv.reader(csvfile)
for row in reader:  ###! main loop reads one row at a time
    if reader.line_num == 1: ###! get the location names from row 1
        locations = row[2:]  ###! slice to remove commodity and date
    else:
        for location,value in zip(locations,row[2:]):  ###! iterate through locations and values
            row_num = len(data)     ###! index for the data row 
            data.append(row[:2])    ###! new data row: commodity and date
            data[row_num].append(location)  ###! append location
            data[row_num].append(float(value.replace('$','')))     ###! append value
csvfile.close()
'''
    Each comment below asks you to write one or two lines of code.
    Your solutions will reveal some aspect of our commodity data set.
    Data records are stored in a list called data.
    Each data record is organized like this:
        [commodity (string), date (string), location (string), price (float)]
    You can observe the format by running the program and then 
        typing "data" in the console window.
'''
# (1) make a list named comList of all commodities using list comprehension
comList = list(record[0] for record in data)
####
# (2) make another list named uComList with the duplicates removed 
# (one source code statement) hint: use the set() and list() functions
uComList = list(set(comList))
sComList = [ sName for sName in uComList if sName.lower().startswith("s")]
####
# (3) Print the number of unique commodities that are present in the data
# (one source code statement) hint: use the len() function
print(f"There are {len(uComList)} unique commodities.")
####
# (4) Use list comprehension compute a list named comNums where each item is a list 
# of this format: [commodity_name, number of records of that commodity]
# (one source code statement) hint: use the count() method
comNums = [[commodity, comList.count(commodity)] for commodity in uComList]
####
# (5) for each item in comNums, print the number of records
# (two source code lines)
for item in comNums:
    print(f"Found {item[1]} records for {item[0]}.")
####
####
# (6) Sort comNums according to number of records in ascending order 
# (one source code statement) hint: use the sort() method with a lambda
comNums.sort(key=lambda x: x[1])
####
# (7) print the commodity with the fewest number of records
# (one source code statement)
print(f"Least available commodity = {comNums[0][0]}.")
####
# (8) print the number of weeks the least available commodity was available for
# (one source code statement) hint: each commodity has 5 records for each week
print(f"{comNums[0][0]} were available for {comNums[0][1] // 5} weeks.")
####
# (9) use a list comprehension to find the lowest price for nectarines in Chicago
# assign it to a variable called min1 hint: use the min() function
# (one source code statement)
min1 = min([record[3] for record in data if record[0] == 'Nectarines' and 'Chicago' in record[2]])
####
# (10) use a list comprehension to find the date of the lowest price for nectarines
# in Chicago and assign it to a variable named mind1
# (one source code statement) hint: one value at index=0
mind1 = [record[1] for record in data if record[0] == 'Nectarines' and 'Chicago' in record[2] and record[3] == min1][0]
####
# (11) print the lowest price for nectarines in Chicago and the date
# (one source code statement)
print(f"The lowest price for Nectarines in Chicago was ${min1:.2f} on {mind1}.")
####
# (12) use a list comprehension to find the farm price for nectarines on the same 
# date and assign it to a variable named fp1
# (one source code statement)
fp1 = next((record[3] for record in data if record[1] == mind1 and record[0] == 'Nectarines' and 'Farm' in record[2]))
####
# (13) print the farm price for nectarines on the date 
# of lowest price in Chicago and print the computed price difference
# (one source code statement)
print(f"Nectarine farm price on {mind1} was ${fp1:.2f}; ${min1 - fp1:.2f} less than in Chicago.")
####
# (14) Create a dictionary called comNumsDict where the keys are the commodities 
# and the values are the number of weeks each commodity was available for
# (one source code statement) hint: use a list comprehension and the dict() function
comNumsDict = {commodity: sum(record[1] // 5 for record in comNums if record[0] == commodity) for commodity in uComList}
####
# (15) Use comNumDict to print the number of weeks peaches were available for
# (one source code statement)
print(f"Peaches were available for {comNumsDict['Peaches']} weeks.")
####
# (16) Use a list comprehension to calculate the average price of Peaches
# in Atlanta and assign it to a variable pAvg
# (one source code statement) hint use the sum() function and the dictionary
pAvg = sum([record[3] for record in data if record[0] == 'Peaches' and record[2] == 'Atlanta']) / comNumsDict['Peaches']
####
# (17) Print the average price of Peaches in Atlanta
print(f"The average price of peaches in Atlanta was ${pAvg:.2f}.")
####
'''
This is what your RESULTS should look like ...
    There are 22 unique commodities.
    Found 255 records for Celery.
    Found 80 records for Nectarines.
    Found 265 records for Romaine Lettuce.
    Found 130 records for Honeydews.
    Found 80 records for Plums.
    Found 160 records for Avocados.
    Found 80 records for Tomatoes.
    Found 125 records for Cantaloupe.
    Found 155 records for Flame Grapes.
    Found 265 records for Cauliflower.
    Found 265 records for Oranges.
    Found 25 records for Thompson Grapes.
    Found 260 records for Strawberries.
    Found 260 records for Broccoli Crowns.
    Found 35 records for Asparagus.
    Found 190 records for Potatoes.
    Found 235 records for Broccoli Bunches.
    Found 265 records for Green Leaf Lettuce.
    Found 265 records for Iceberg Lettuce.
    Found 260 records for Carrots.
    Found 265 records for Red Leaf Lettuce.
    Found 85 records for Peaches.
    Least available commodity = Thompson Grapes.
    Thompson Grapes were available for 5 weeks.
    The lowest price for Nectarines in Chicago was $1.68 on 6/18/2017.
    Nectarine farm price on 6/18/2017 was $0.88; $0.80 less than in Chicago.
    Peaches were available for 17 weeks.
    The average price of peaches in Atlanta was $1.73.
'''
