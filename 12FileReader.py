# Create a solution that accepts an input identifying the name of a text file, for example, "WordTextFile1.txt".
# Each text file contains three rows with one word per row.
# Using the open() function and write() and read() methods, interact with the input text file to write a new sentence string composed of the three existing words to the end of the file contents on a new line.
# Output the new file contents.
#open, write, and read text file (e.g., "WordTextFile1.txt") using open(), write(), read()
#solution accepts file input to insert sentence composed of file content into text file on a new line
#solution outputs the text file contents including the new sentence

# Get the filename as input
inputA = str(input())

# Create an empty list to store the output
outPut = []

with open(inputA) as file:
    
    # Read the contents of the file as a list of lines
    fileOutput = file.readlines()
    
    # Remove trailing whitespace, including newline character
    for lineOut in fileOutput:
        line = lineOut.rstrip()
        
        # Print the line without trailing whitespace
        print(line)
        
        # Add the line to the output list
        outPut.append(line)

# Join the lines in the output list with a space separator and print
print(" ".join(outPut))
