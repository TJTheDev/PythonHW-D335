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
Given input characters for an arrowhead and arrow body, print a right-facing arrow.

Ex: If the input is:

*
#
Then the output is:

      #
******##
******###
******##
      #
"""

base_char = input()
head_char = input()

row1 = '      ' + head_char
row2 = (base_char * 6) + (head_char * 2)
row3 = (base_char * 6) + (head_char * 3)

print(row1)
print(row2)
print(row3)
print(row2)
print(row1)

"""
Given an integer representing a 10-digit phone number, output the area code, prefix, and line number using the format (800) 555-1212.

Ex: If the input is:

8005551212
the output is:

(800) 555-1212
"""

phone_number = int(input())

numberStr = str(phone_number)

print (f"({numberStr[0:3]}) {numberStr[3:6]}-{numberStr[6:]}")

"""
Write a program whose inputs are three integers, and whose output is the smallest of the three values.

Ex: If the input is:

7
15
3
the output is:

3
"""
num1 = int(input())
num2 = int(input())
num3 = int(input())
smallest = num1

if num2 < smallest:
    smallest = num2
    
if num3 < smallest:
    smallest = num3

print (smallest)

"""
Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

Ex: If the input is:

0 
(or less than 0), the output is:

No change 
Ex: If the input is:

45
the output is:

1 Quarter
2 Dimes 
"""

dollarCount = 0
quarterCount = 0
dimeCount = 0
nickelCount = 0
pennyCount = 0

numIn = int(input())
noChangeCheck = numIn

while numIn >= 100:
    numIn = numIn - 100
    dollarCount += 1

while numIn >= 25:
    numIn = numIn - 25
    quarterCount += 1
    
while numIn >= 10:
    numIn = numIn - 10
    dimeCount += 1
    
while numIn >= 5:
    numIn = numIn - 5
    nickelCount += 1

pennyCount = numIn

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

if noChangeCheck == 0:
    print("No change")

"""
Write a program whose input is two integers. Output the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer. End with a newline.

Ex: If the input is:

-15
10
the output is:

-15 -10 -5 0 5 10 
Ex: If the second integer is less than the first as in:

20
5
the output is:

Second integer can't be less than the first.
For coding simplicity, output a space after every integer, including the last.
"""
numIn1 = int(input())
numIn2 = int(input())
numTrue = False

if numIn1 > numIn2:
  print ("Second integer can't be less than the first.")

while numIn1 <= numIn2:
    print(numIn1, end=" ")
    numIn1 = numIn1 + 5
    numTrue = True

if numTrue == True:
    print ()

"""
Write a program that takes in a line of text as input, and outputs that line of text in reverse. The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

Ex: If the input is:

Hello there
Hey
done
then the output is:

ereht olleH
yeH
"""

userInput = ""
revString = True

while revString == True:
    userInput = str(input())
    if userInput == "done" or userInput == "Done" or userInput == "d" or userInput:
        revString = False
    else:
        reverse = userInput [::-1]
        print (reverse)
