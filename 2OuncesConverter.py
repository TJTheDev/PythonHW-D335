#Python WGU Tarrylon Toney Ounces converter
"""
Create a solution that accepts an integer input representing any number of ounces. Output the converted total number of tons, pounds, and remaining ounces based on the input ounces value. There are 16 ounces in a pound and 2,000 pounds in a ton.

The solution output should be in the format

Tons: value_1
Pounds: value_2
Ounces: value_3
"""

#there are 16 ounces in a pound and 2000 pounds in a ton
poundsCal = 16
totalPounds = 0
tonsCal = 2000 * 16
totalTons = 0

#solution accepts an integer value representing any number of ounces
totalOunces = int(input())

#loop to check Tons
while totalOunces >= tonsCal:
    totalOunces = totalOunces - tonsCal
    totalTons = totalTons + 1

#loop to fix Pounds
while totalOunces >= poundsCal:
    totalOunces = totalOunces - poundsCal
    totalPounds = totalPounds + 1


#Outputs the converted tons, pounds, and ounces represented by the input value of ounces
print("Tons:", totalTons)
print("Pounds:", totalPounds)
print("Ounces:", totalOunces)
