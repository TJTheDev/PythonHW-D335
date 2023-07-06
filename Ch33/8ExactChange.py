"""
Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

Ex: If the input is:
0 (or less than 0), the output is:
No change 

Ex: If the input is:
45

the output is:
1 Quarter
2 Dimes 

"""

dollarCount = 0  # Counter for dollars
quarterCount = 0  # Counter for quarters
dimeCount = 0  # Counter for dimes
nickelCount = 0  # Counter for nickels
pennyCount = 0  # Counter for pennies

numIn = int(input())  # Prompt the user to input a number and convert it to an integer
noChangeCheck = numIn  # Store the input value for later comparison

# Determine the number of dollars
while numIn >= 100:
    numIn = numIn - 100
    dollarCount += 1

# Determine the number of quarters
while numIn >= 25:
    numIn = numIn - 25
    quarterCount += 1
    
# Determine the number of dimes
while numIn >= 10:
    numIn = numIn - 10
    dimeCount += 1
    
# Determine the number of nickels
while numIn >= 5:
    numIn = numIn - 5
    nickelCount += 1

# The remaining value is the number of pennies
pennyCount = numIn

# Output the number of each type of coin, if there are any
if dollarCount > 0:
    print(dollarCount, "Dollars" if dollarCount > 1 else "Dollar")
    
if quarterCount > 0:
    print(quarterCount, "Quarters" if quarterCount > 1 else "Quarter")
    
if dimeCount > 0:
    print(dimeCount, "Dimes" if dimeCount > 1 else "Dime")
    
if nickelCount > 0:
    print(nickelCount, "Nickels" if nickelCount > 1 else "Nickel")
    
if pennyCount > 0:
    print(pennyCount, "Pennies" if pennyCount > 1 else "Penny")

# Output "No change" if the input value was zero
if noChangeCheck == 0:
    print("No change")