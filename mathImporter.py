"""
Instructions:
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.
 
Task:
Create a solution that accepts an integer input. Import the built-in module math and use its factorial() method to calculate the factorial of the integer input. Output the value of the factorial, as well as a Boolean value identifying whether the factorial output is greater than 100.
The solution output should be in the format
factorial_value
Boolean_value
 
Sample Input/Output:
If the input is
10
then the expected output is
3628800
True
Alternatively, if the input is
3
then the expected output is
6
False
"""

import math

numIn = int(input())
numInFuc = math.factorial(numIn)

print(numInFac)
print(numInFuc > 100)
