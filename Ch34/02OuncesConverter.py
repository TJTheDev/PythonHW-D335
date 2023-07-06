#Python WGU Tarrylon Toney Ounces converter
"""
Create a solution that accepts an integer input representing any number of ounces. Output the converted total number of tons, pounds, and remaining ounces based on the input ounces value. There are 16 ounces in a pound and 2,000 pounds in a ton.

The solution output should be in the format

Tons: value_1
Pounds: value_2
Ounces: value_3

"""

tonsOut = 0
poundsOut = 0
ounces = int(input())

while ounces >= (2000 * 16):
    tonsOut = tonsOut + 1
    ounces = ounces - (2000 * 16)

while ounces >= 16:
    poundsOut = poundsOut + 1
    ounces = ounces - 16

print (f"Tons: {tonsOut}")
print (f"Pounds: {poundsOut}")
print (f"Ounces: {ounces}")
