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

import csv

wordList = []    # List to store unique words
wordCount = {}   # Dictionary to store word frequencies

csvIn = str(input())  # Get input file name from user

with open(csvIn) as file:  # Open the input file
    for rows in csv.reader(file):  # Read the file using csv.reader
        for column in rows:  # Iterate over each column/word in the row
            if column not in wordCount:  # Check if the word is not in the wordCount dictionary
                wordCount[column] = 1  # If it's a new word, add it to wordCount with frequency 1
                wordList.append(column)  # Also add the word to wordList to keep track of unique words
            else:
                wordCount[column] += 1  # If the word is already in wordCount, increment its frequency

for word in wordList:  # Print the unique words and their frequencies
    print(word, wordCount[word])