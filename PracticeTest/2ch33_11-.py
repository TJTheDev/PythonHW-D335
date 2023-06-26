"""
The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which has an index n as parameter and returns the nth value in the sequence. Any negative index values should return -1.

Ex: If the input is:

7
the output is:

fibonacci(7) is 13
Note: Use a for loop and DO NOT use recursion.
"""

def fibonacci(n):
    # Check if the input number is negative
    if n < 0:
        return -1  # Fibonacci series is not defined for negative numbers
    
    # Initialize variables for the first two numbers in the Fibonacci sequence
    x = 0
    y = 1
    
    # Iterate 'n' times to generate the nth Fibonacci number
    for _ in range(n):
        # Assign the value of 'y' to 'x' and the sum of 'x' and 'y' to 'y'
        temp = x + y
        x = y
        y = temp
    
    # Return the nth Fibonacci number
    return x


if __name__ == '__main__':
    # Prompt the user to enter a starting number for the Fibonacci sequence
    start_num = int(input())
    
    # Call the fibonacci() function with the start number and print the result
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')

"""
Complete the calc_average() function that has an integer list parameter and returns the average value of the elements in the list as a float.

Ex: If the input list is:

1 2 3 4 5
then the returned average will be:

3.0
"""

def calc_average(nums):
    mathUp = 0  # Variable to store the sum of numbers
    divide = 0  # Variable to store the count of numbers
    
    # Iterate over the numbers in the list
    for _ in nums:
        mathUp = _ + mathUp  # Add the current number to the running sum
        divide = divide + 1  # Increment the count of numbers
        
    # Calculate the average by dividing the sum by the count
    mathUp = float(mathUp) / float(divide)
    
    return mathUp

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]  # List of numbers to calculate the average
    print(calc_average(nums))  # Call calc_average() with nums and print the result
    # The expected output is 3.0, since the average of [1, 2, 3, 4, 5] is 3.0

"""
(1) Prompt the user to enter a string of their choosing. Output the string. (1 pt)

Ex:

Enter a sentence or phrase:
The only thing we have to fear is fear itself.

You entered: The only thing we have to fear is fear itself.
(2) Complete the get_num_of_characters() function, which returns the number of characters in the user's string. We encourage you to use a for loop in this function. (2 pts)

(3) Extend the program by calling the get_num_of_characters() function and then output the returned result. (1 pt)

(4) Extend the program further by implementing the output_without_whitespace() function. output_without_whitespace() outputs the string's characters except for whitespace (spaces, tabs). Note: A tab is '\t'. Call the output_without_whitespace() function in main(). (2 pts)

Ex:

Enter a sentence or phrase: 
The only thing we have to fear is fear itself.

You entered: The only thing we have to fear is fear itself.

Number of characters: 46
String with no whitespace: Theonlythingwehavetofearisfearitself.
"""

def get_num_of_characters(input_str):
    # Initialize a counter for the number of characters
    num_count = 0
    
    # Iterate over each character in the input string
    for _ in input_str:
        # Increment the counter by 1 for each character
        num_count = num_count + 1
    
    # Return the total count of characters
    return num_count


def output_without_whitespace(input_str):
    # Initialize an empty string to store the output
    output = ""
    
    # Iterate over each character in the input string
    for _ in input_str:
        # Check if the character is not a whitespace (space or tab)
        if _ != " " and _ != "\t":
            # Concatenate the character to the output string
            output = output + _
    
    # Return the resulting string with no whitespace
    return output


if __name__ == '__main__':
    # Prompt the user to enter a sentence or phrase
    strIn = str(input("Enter a sentence or phrase:\n\n"))
    
    # Print the entered string
    print(f"You entered:", strIn + "\n")

    # Call the get_num_of_characters() function and print the number of characters in the input string
    print(f"Number of characters:", get_num_of_characters(strIn))
    
    # Call the output_without_whitespace() function and print the string without whitespace
    print(f"String with no whitespace:", output_without_whitespace(strIn))

"""
A palindrome is a word or a phrase that is the same when read both forward and backward. Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

Ex: If the input is:

bob
the output is:

bob is a palindrome
Ex: If the input is:

bobby
the output is:

bobby is not a palindrome
Hint: Start by removing spaces. Then check if a string is equivalent to it's reverse.
"""

# Prompt the user to enter a string and remove leading/trailing whitespace
strIn = str(input()).strip()

# Reverse the input string using slicing
strRev = strIn[::-1]

# Check if the original string is equal to its reverse
if strIn == strRev:
    # Print the result if it is a palindrome
    print(f"{strIn} is a palindrome")
else:
    # Print the result if it is not a palindrome
    print(f"{strIn} is not a palindrome")

"""
Write a program to read dates from input, one date per line. Each date's format must be as follows: March 1, 1990. Any date not following that format is incorrect and should be ignored. The input ends with -1 on a line alone. Output each correct date as: 3/1/1990.

Hint: Use string[start:end] to get a substring when parsing the string and extracting the date. Use the split() method to break the input into tokens.

Ex: If the input is:

March 1, 1990
April 2 1995
7/15/20
December 13, 2003
-1
then the output is:

3/1/1990
12/13/2003
"""

def get_month_as_int(monthString):

    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0

    return month_int


user_string = input()

# TODO: Read dates from input, parse the dates to find the one
#       in the correct format, and output in m/d/yyyy format
