# Formatted output: No parking sign
print("  NO PARKING")
print("2:00 - 6:00 a.m.")


# Input: Mad Lib
# Read a value from a user and store the value in first_name
first_name = str(input())
generic_location = str(input())
whole_number = int(input())
plural_noun = str(input())

# TODO: Type your code to read three more values here.

# Output a short story using the four input values. Do not modify the code below.
print(first_name, 'went to', generic_location, 'to buy', whole_number, 'different types of', plural_noun)

# Convert to dollars
''' Given four values representing counts of quarters, dimes, nickels and pennies, 
output the total amount as dollars and cents. 

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'Amount: ${dollars:.2f}')
'''

quarterTotal = int(input()) * (.25)
dimesTotal = int(input()) * (.10)
nickelsTotal = int(input()) * (.05)
penniesTotal = int(input()) * (.01)
totalCount = (quarterTotal + dimesTotal + nickelsTotal + penniesTotal)

print(f"Amount: ${totalCount:.2f}")

"""
Driving is expensive. Write a program with a car's gas mileage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')
"""

milesPerGallon = float(input())
costPerGallon = float(input())

per20Miles = (costPerGallon / milesPerGallon) * 20

per75Miles = (costPerGallon / milesPerGallon) * 75

per500Miles = (costPerGallon / milesPerGallon) * 500


print(f'{per20Miles:.2f} {per75Miles:.2f} {per500Miles:.2f}')

"""

"""
