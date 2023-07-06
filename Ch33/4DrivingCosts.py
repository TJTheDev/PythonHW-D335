"""
Driving is expensive. Write a program with a car's gas mileage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')

Ex: If the input is:
20.0
3.1599

where the gas mileage is 20.0 miles/gallon and the cost of gas is $3.1599/gallon, the output is:
3.16 11.85 79.00
"""

milesPerGallon = float(input())  # Prompt the user to input the miles per gallon and convert it to a float

costPerGallon = float(input())  # Prompt the user to input the cost per gallon and convert it to a float

per20Miles = (costPerGallon / milesPerGallon) * 20  # Calculate the cost for driving 20 miles

per75Miles = (costPerGallon / milesPerGallon) * 75  # Calculate the cost for driving 75 miles

per500Miles = (costPerGallon / milesPerGallon) * 500  # Calculate the cost for driving 500 miles

print(f'{per20Miles:.2f} {per75Miles:.2f} {per500Miles:.2f}')  # Output the costs for driving 20 miles, 75 miles, and 500 miles


