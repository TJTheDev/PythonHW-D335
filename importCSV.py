"""
Instructions:
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.
 
Task:
Create a solution that accepts an input identifying the name of a CSV file, for example, "input1.csv". Each file contains two rows of comma-separated values. Import the built-in module csv and use its open() function and reader() method to create a dictionary of key:value pairs for each row of comma-separated values in the specified file. Output the file contents as two dictionaries.
The solution output should be in the format
{key:value,key:value,key:value}
{key:value,key:value,key:value}
 
Sample Input/Output:
If the file content is
input1.csv
then the expected output is
{a:100,b:200,c:300}
{bananas:1.85,steak:19.99,cookies:4.52}
Alternatively, if the file content is
input2.csv
then the expected output is
{d:400,e:500,f:600}
{celery:2.81,milk:4.34,bread:5.63}
"""



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
