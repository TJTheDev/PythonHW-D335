"""
Write a program whose inputs are three integers, and whose output is the smallest of the three values.

Ex: If the input is:
7
15
3

the output is:
3

"""

num1 = int(input())  # Prompt the user to input the first number and convert it to an integer

num2 = int(input())  # Prompt the user to input the second number and convert it to an integer

num3 = int(input())  # Prompt the user to input the third number and convert it to an integer

smallest = num1  # Assume the first number is the smallest initially

if num2 < smallest:  # Check if the second number is smaller than the current smallest
    smallest = num2  # If so, update the smallest to be the second number

if num3 < smallest:  # Check if the third number is smaller than the current smallest
    smallest = num3  # If so, update the smallest to be the third number

print(smallest)  # Print the smallest number