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

strIn = str(input()).strip()  # Prompt the user to input a string and remove leading/trailing whitespace
strCov = ""  # Initialize an empty string to store the input string without whitespace

# Iterate over each character in the input string
for _ in strIn:
    if _ != " " and _ != "\t":  # Check if the character is not a space or tab
        strCov = strCov + _  # Append the character to the 'strCov' string

strRev = strCov[::-1]  # Reverse the 'strCov' string using slicing

# Check if the modified string is equal to its reversed version
if strCov == strRev:
    print(f"{strIn} is a palindrome")  # Output that the input string is a palindrome
else:
    print(f"{strIn} is not a palindrome")  # Output that the input string is not a palindrome
