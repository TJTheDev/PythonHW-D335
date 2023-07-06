"""
Given four values representing counts of quarters, dimes, nickels and pennies, output the total amount as dollars and cents.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'Amount: ${dollars:.2f}')

Ex: If the input is:
4 
3
2
1

where 4 is the number of quarters, 3 is the number of dimes, 2 is the number of nickels, and 1 is the number of pennies, the output is:
Amount: $1.41
"""

quarterTotal = int(input()) * 0.25  # Prompt the user to input the number of quarters and multiply it by 0.25 to calculate the total value of quarters

dimesTotal = int(input()) * 0.10  # Prompt the user to input the number of dimes and multiply it by 0.10 to calculate the total value of dimes

nickelsTotal = int(input()) * 0.05  # Prompt the user to input the number of nickels and multiply it by 0.05 to calculate the total value of nickels

penniesTotal = int(input()) * 0.01  # Prompt the user to input the number of pennies and multiply it by 0.01 to calculate the total value of pennies

totalCount = quarterTotal + dimesTotal + nickelsTotal + penniesTotal  # Calculate the total value of all the coins by adding the values of quarters, dimes, nickels, and pennies

print(f"Amount: ${totalCount:.2f}")  # Output the total amount in dollars with two decimal places
