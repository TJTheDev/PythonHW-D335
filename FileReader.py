# Create a solution that accepts an input identifying the name of a text file, for example, "WordTextFile1.txt".
# Each text file contains three rows with one word per row.
# Using the open() function and write() and read() methods, interact with the input text file to write a new sentence string composed of the three existing words to the end of the file contents on a new line.
# Output the new file contents.
#open, write, and read text file (e.g., "WordTextFile1.txt") using open(), write(), read()
#solution accepts file input to insert sentence composed of file content into text file on a new line
#solution outputs the text file contents including the new sentence

inputA = str(input())
outPut = []

with open(inputA) as file:
    fileOutput = file.readlines()
    for lineOut in fileOutput:
        print(lineOut.rstrip())
        outPut.append(lineOut.rstrip())        
for item in outPut:
    print (item, end=" ")

