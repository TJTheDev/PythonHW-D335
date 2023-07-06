"""
Write a program that takes in a line of text as input, and outputs that line of text in reverse. The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

Ex: If the input is:
Hello there
Hey
done

then the output is:
ereht olleH
yeH

"""

userInput = ""  # Initialize an empty string to store user input
revString = True  # Variable to control the reverse string loop

while revString == True:
    userInput = str(input())  # Prompt the user to input a string and store it in the 'userInput' variable
    if userInput == "done" or userInput == "Done" or userInput == "d" or userInput:  # Check if the user wants to exit the loop
        revString = False  # If so, set 'revString' to False to exit the loop
    else:
        reverse = userInput[::-1]  # Reverse the string using slicing and store it in the 'reverse' variable
        print(reverse)  # Print the reversed string
