"""
Write a program to read dates from input, one date per line. Each date's format must be as follows: March 1, 1990. Any date not following that format is incorrect and should be ignored. The input ends with -1 on a line alone. Output each correct date as: 3/1/1990.

Hint: Use string[start:end] to get a substring when parsing the string and extracting the date. Use the split() method to break the input into tokens.

Ex: If the input is:
March 1, 1990
April 2 1995
7/15/20
December 13, 2003
-1

then the output is:
3/1/1990
12/13/2003

"""

def get_month_as_int(monthString): # Convert the month string to the corresponding integer value
    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0   # Return 0 if the month string is not recognized
    return month_int


loop = True
listSave = []

while loop is True:
    dateCheck = str(input()).strip().capitalize()   # Read input from the user

    if dateCheck == str(-1):   # Check if the input is -1, indicating the end of input
        loop = False

    if "," in dateCheck and dateCheck[0:3].isalpha() and int(dateCheck[-1].isdigit()):    # Check if the input matches the required date format
        dateSplitOG = dateCheck.split(", ")     # Split the input into parts using the comma and space as delimiters
        dateSplit2nd = dateSplitOG[0].split(" ")
        print(f"{get_month_as_int(dateSplit2nd[0])}/{dateSplit2nd[1]}/{dateSplitOG[1]}")    # Output the date in the required format using string formatting
