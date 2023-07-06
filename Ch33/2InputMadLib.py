"""
Mad Libs are activities that have a person provide various words, which are then used to complete a short story in unexpected (and hopefully funny) ways.

Complete a program that reads four values from input and stores the values in variables first_name, generic_location, whole_number, and plural_noun. The program then uses the input values to output a short story. The first input statement is provided in the code as an example.

Notes: To test your program in the Develop mode, pre-enter four values (in separate lines) in the input box and click the Run program button. The auto-grader in the Submit mode will test your program with different sets input of values.

Ex: If the input values are:
Eric
Chipotle
12
cars

then the program uses the input values and outputs a story:
Eric went to Chipotle to buy 12 different types of cars

Ex: If the input values are:
Brenda
Philadelphia
6
bells

then the program uses the input values and outputs a story:
Brenda went to Philadelphia to buy 6 different types of bells

"""

first_name = str(input())  # Prompt the user to input their first name and store it in the variable 'first_name'

generic_location = str(input())  # Prompt the user to input a generic location and store it in the variable 'generic_location'

whole_number = int(input())  # Prompt the user to input a whole number and convert it to an integer, then store it in the variable 'whole_number'

plural_noun = str(input())  # Prompt the user to input a plural noun and store it in the variable 'plural_noun'

print(f"{first_name} went to {generic_location} to buy {whole_number} different types of {plural_noun}")  # Output a short story using the input values