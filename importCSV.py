import csv

# Accept a string input representing the CSV file name
csvName = str(input())

# Open the CSV file in read mode using a context manager
with open(csvName, 'r') as file:
    # Read all rows from the CSV file and store them in the 'data' list
    data = [row for row in csv.reader(file)]

# Iterate over each row in the 'data' list
for row in data:
    # Extract the even-indexed elements from the row and strip whitespace
    evens = [row[x].strip() for x in range(0, len(row), 2)]
    # Extract the odd-indexed elements from the row and strip whitespace
    odds = [row[x].strip() for x in range(1, len(row), 2)]
    # Combine the even and odd elements into a dictionary using zip()
    combined = dict(zip(evens, odds))
    # Print the combined dictionary for each row
    print(combined)
