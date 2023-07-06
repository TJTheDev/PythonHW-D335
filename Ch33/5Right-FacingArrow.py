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

base_char = input()  # Prompt the user to input the base character and store it in the variable 'base_char'
head_char = input()  # Prompt the user to input the head character and store it in the variable 'head_char'

row1 = '      ' + head_char  # Create the first row by concatenating five spaces with the 'head_char'
row2 = (base_char * 6) + (head_char * 2)  # Create the second row by concatenating six occurrences of 'base_char' and two occurrences of 'head_char'
row3 = (base_char * 6) + (head_char * 3)  # Create the third row by concatenating six occurrences of 'base_char' and three occurrences of 'head_char'

print(row1)  # Print the first row
print(row2)  # Print the second row
print(row3)  # Print the third row
print(row2)  # Print the second row again
print(row1)  # Print the first row again