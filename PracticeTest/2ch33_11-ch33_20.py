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
    # Convert the month string to the corresponding integer value
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
        # Return 0 if the month string is not recognized
        month_int = 0

    return month_int

loop = True
listSave = []

while loop is True:
    # Read input from the user
    dateCheck = str(input()).strip().capitalize()

    # Check if the input is -1, indicating the end of input
    if dateCheck == str(-1):
        loop = False

    # Check if the input matches the required date format
    if "," in dateCheck and dateCheck[0:3].isalpha() and int(dateCheck[-1].isdigit()):
        
        # Split the input into parts using the comma and space as delimiters
        dateSplitOG = dateCheck.split(", ")
        dateSplit2nd = dateSplitOG[0].split(" ")
        
        # Output the date in the required format using string formatting
        print(f"{get_month_as_int(dateSplit2nd[0])}/{dateSplit2nd[1]}/{dateSplitOG[1]}")
"""
Write a program to calculate the total price for car wash services. A base car wash is $10. A dictionary with each additional service and the corresponding cost has been provided. Two additional services can be selected. A '-' signifies an additional service was not selected. Output all selected services, according to the input order, along with the corresponding costs and then the total price for all car wash services.

Ex: If the input is:

Tire shine
Wax
the output is:

ZyCar Wash
Base car wash -- $10
Tire shine -- $2
Wax -- $3
----
Total price: $15
Ex: If the input is:

Rain repellent
-
the output is:

ZyCar Wash
Base car wash -- $10
Rain repellent -- $2
----
Total price: $12
"""

services = { 'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5 }
base_wash = 10
total = 0

# Get user input for service choices
service_choice1 = input()
service_choice2 = input()

# Print the car wash header
print("ZyCar Wash")
print("Base car wash -- $10")
total = base_wash

# Check if the first service choice is selected
if service_choice1 != "-":
    # Print the first service choice and its price
    print(f"{service_choice1} -- ${services[service_choice1]}")
    total = total + services[service_choice1]

# Check if the second service choice is selected
if service_choice2 != "-":
    # Print the second service choice and its price
    print(f"{service_choice2} -- ${services[service_choice2]}")
    total = total + services[service_choice2]

# Print a separator
print("----")

# Print the total price
print(f"Total price: $" + str(total))

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
num1 = input()
num2 = input()

try:
    # Try to perform the division and format the result with no decimal places
    result = int(num1) / int(num2)
    print("{:.0f}".format(result))

except ZeroDivisionError:
    # Handle the exception if num2 is 0, resulting in a zero division error
    print("Zero Division Exception: integer division or modulo by zero")

except ValueError:
    # Handle the exception if num1 or num2 are not valid integers
    if "." in num1 or not num1.isdigit():
        print(f"Input Exception: invalid literal for int() with base 10: '{num1}'")
    if "." in num2 or not num2.isdigit():
        print(f"Input Exception: invalid literal for int() with base 10: '{num2}'")

"""
A pedometer treats walking 2,000 steps as walking 1 mile. Write a steps_to_miles() function that takes the number of steps as a parameter and returns the miles walked. The steps_to_miles() function throws a ValueError object with the message "Exception: Negative step count entered." when the number of steps is negative. Complete the main() program that reads the number of steps from a user, calls the steps_to_miles() function, and outputs the returned value from the steps_to_miles() function. Use a try-except block to catch any ValueError object thrown by the steps_to_miles() function and output the exception message.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

Ex: If the input of the program is:

5345
the output of the program is:

2.67
Ex: If the input of the program is:

-3850
the output of the program is:

Exception: Negative step count entered.

def steps_to_miles(x):
    if x < 0:
        raise ValueError("Exception: Negative step count entered.")
    else:
        return(x / 2000)
    

if __name__ == '__main__':
    stepCount = int(input())
    if steps_to_miles(stepCount) > 0:
        print(f"{steps_to_miles(stepCount):.2f}")
    else:
        print ('ValueError: Exception: Negative step count entered.')
"""
def steps_to_miles(stepCov):
    if stepCov < 0:
        raise ValueError("Exception: Negative step count entered.")
    return (stepCov / 2000)
    

if __name__ == '__main__':
    stepCount = int(input())
    
    try:
        miles_walked = steps_to_miles(stepCount)
    except ValueError:
        print('Exception: Negative step count entered.')
        
    print(f"{steps_to_miles(stepCount):.2f}")

"""
Given a set of text files containing synonyms for different words, complete the main program to output the synonyms for a specific word. Each text file contains synonyms for the word specified in the file’s name, and each row within the file lists the word’s synonyms that begin with the same letter, separated by a space. The program reads a word and a letter from the user and opens the text file associated with the input word. The program then stores the contents of the text file into a dictionary predefined in the program. Finally the program searches the dictionary and outputs all the synonyms that begin with the input letter, one synonym per line, or a message if no synonyms that begin with the input letter are found.

Hints: Use the first letter of a synonym as the key when storing the synonym into the dictionary. Assume all letters are in lowercase.

Ex: If the input of the program is:

educate
c
the program opens the file educate.txt, which contains:

brainwash brief
civilize coach cultivate
develop discipline drill
edify enlighten exercise explain
foster
improve indoctrinate inform instruct
mature
nurture
rear
school
train tutor
then the program outputs:

civilize
coach
cultivate
Ex: If the input of the program is:

educate
a
then the program outputs:

No synonyms for educate begin with a.
"""
synonyms = {}   # Define dictionary

fileOpen = str(input())  # Prompt user for input file name
dictLetter = str(input())  # Prompt user for dictionary letter
wordSplit = ""  # Initialize an empty string for storing the split words
noOutputCheck = True  # Flag to check if there are any output synonyms

with open(fileOpen + ".txt") as file:  # Open the input file
    for x in file:  # Iterate over each line in the file
        if x[0] == dictLetter:  # Check if the first letter of the line matches the dictionary letter
            synonyms = x  # If it matches, store the line as synonyms

    for _ in synonyms:  # Iterate over each character in the synonyms
        if _ != " " and _ != "\t" and _ != "\n":  # Check if the character is not a space, tab, or newline
            wordSplit = wordSplit + _  # Append the character to wordSplit
            noOutputCheck = False  # Set the flag to False since there is at least one output synonym
        else:
            print(wordSplit)  # If a space, tab, or newline is encountered, print the accumulated wordSplit
            wordSplit = ""  # Reset wordSplit to an empty string

if noOutputCheck == True:  # Check if no output synonyms were found and prints a message if true
    print(f"No synonyms for {fileOpen} begin with {dictLetter}.")
