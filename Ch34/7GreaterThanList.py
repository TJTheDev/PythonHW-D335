#TarrylonToneyPredefList
"""
Create a solution that accepts an integer input to compare against the following list:

predef_list = [4, -27, 15, 33, -10]

Output a Boolean value indicating whether the input value is greater than the maximum value from predef_list

The solution output should be in the format

Greater Than Max? Boolean_value
Sample Input/Output:
If the input is

20
then the expected output is

Greater Than Max? False

OLD:
predef_list = [4, -27, 15, 33, -10]

#solution accepts an integer input
userInput = int(input())

#solution outputs Boolean value indicating if integer input is greater than the maximum value when compared to predef_list
compareMax = max(predef_list)
if compareMax < userInput:
    boolX = True
else:
    boolX = False
    
print ("Greater Than Max?", boolX)
"""

# Define the predefined list of integers
predef_list = [4, -27, 15, 33, -10]

# Get input for the user's integer value
userInput = int(input())  # Enter an integer value for comparison

# Compare the user's input with the maximum value from the predefined list
compareMax = userInput > max(predef_list)  # Check if userInput is greater than the maximum value in predef_list

# Print the result indicating if the user's input is greater than the maximum value
print("Greater Than Max?", compareMax)  # Print a Boolean value indicating if userInput is greater than the maximum value
