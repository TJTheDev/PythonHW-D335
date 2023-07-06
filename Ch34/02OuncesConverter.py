#Python WGU Tarrylon Toney Ounces converter
"""
Create a solution that accepts an integer input representing any number of ounces. Output the converted total number of tons, pounds, and remaining ounces based on the input ounces value. There are 16 ounces in a pound and 2,000 pounds in a ton.

The solution output should be in the format

Tons: value_1
Pounds: value_2
Ounces: value_3

"""

tonsOut = 0  # Variable to store the number of tons
poundsOut = 0  # Variable to store the number of pounds
ounces = int(input())  # Get input value in ounces

while ounces >= (2000 * 16):  # Check if the input value is greater than or equal to one ton (2000 pounds)
    tonsOut = tonsOut + 1  # Increment the tons count
    ounces = ounces - (2000 * 16)  # Subtract one ton (2000 pounds) from the input value

while ounces >= 16:  # Check if the remaining ounces are greater than or equal to one pound
    poundsOut = poundsOut + 1  # Increment the pounds count
    ounces = ounces - 16  # Subtract one pound from the remaining ounces

print(f"Tons: {tonsOut}")  # Print the number of tons
print(f"Pounds: {poundsOut}")  # Print the number of pounds
print(f"Ounces: {ounces}")  # Print the remaining ounces
