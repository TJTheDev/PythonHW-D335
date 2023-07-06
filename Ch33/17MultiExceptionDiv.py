"""
Write a program that reads integers user_num and div_num as input, and output the quotient (user_num divided by div_num). Use a try block to perform all the statements. Use an except block to catch any ZeroDivisionError and output an exception message. Use another except block to catch any ValueError caused by invalid input and output an exception message.

Note: ZeroDivisionError is thrown when a division by zero happens. ValueError is thrown when a user enters a value of different data type than what is defined in the program. Do not include code to throw any exception in the program.

Ex: If the input of the program is:
15
3

the output of the program is:
5

Ex: If the input of the program is:
10
0

the output of the program is:
Zero Division Exception: integer division or modulo by zero

Ex: If the input of the program is:
15.5
5

the output of the program is:
Input Exception: invalid literal for int() with base 10: '15.5'

"""

num1 = input()    # Prompt the user to enter the first number
num2 = input()    # Prompt the user to enter the second number

try:
    # Try to perform the division and format the result with no decimal places
    result = int(num1) / int(num2)
    print("{:.0f}".format(result))    # Print the result with no decimal places

except ZeroDivisionError: # Handle the exception if num2 is 0, resulting in a zero division error
    print("Zero Division Exception: integer division or modulo by zero")

except ValueError: # Handle the exception if num1 or num2 are not valid integers
    if "." in num1 or not num1.isdigit():
        print(f"Input Exception: invalid literal for int() with base 10: '{num1}'")
        
    if "." in num2 or not num2.isdigit():
        print(f"Input Exception: invalid literal for int() with base 10: '{num2}'")
