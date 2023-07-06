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

if noOutputCheck == True:  # Check if no output synonyms were found
    print(f"No synonyms for {fileOpen} begin with {dictLetter}.")  # Print a message indicating no output synonyms found