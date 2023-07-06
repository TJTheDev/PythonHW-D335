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

"""

numIn1 = int(input())  # Prompt the user to input the first number and convert it to an integer
numIn2 = int(input())  # Prompt the user to input the second number and convert it to an integer
numTrue = False  # Variable to track if the loop was executed

if numIn1 > numIn2:
    print("Second integer can't be less than the first.")  # Output an error message if the second integer is less than the first

while numIn1 <= numIn2:
    print(numIn1, end=" ")  # Output the current value of numIn1 without a newline character
    numIn1 = numIn1 + 5  # Increment numIn1 by 5
    numTrue = True  # Set numTrue to True to indicate that the loop was executed

if numTrue == True:
    print()  # Output a newline character if the loop was executed
