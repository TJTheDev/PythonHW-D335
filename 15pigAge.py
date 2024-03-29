"""
Instructions:
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.
 
Task:
Create a solution that accepts an integer input representing the age of a pig. Import the existing module pigAge and use its pre-built pigAge_converter() function to calculate the human equivalent age of a pig. A year in a pig's life is equivalent to five years in a human's life. Output the human-equivalent age of the pig.
The solution output should be in the format
input_pig_age is converted_pig_age in human years
 
Sample Input/Output:
If the input is
8
then the expected output is
8 is 40 in human years
"""

import pigAge  # Import the pigAge module

pigAgeInput = int(input())  # Get an integer input for pig age

# Call the pigAge_converter function from the pigAge module to convert pig age to human years
pigAgeConv = pigAge.pigAge_converter(pigAgeInput)

# Print the original pig age and the converted age in human years using f-string formatting
print(f"{pigAgeInput} is {pigAgeConv} in human years")
