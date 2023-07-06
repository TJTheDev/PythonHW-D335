"""
"""

dataInput = str(input())  # Accept a string input representing the data file name

category = []  # List to store the category values
name = []  # List to store the name values
description = []  # List to store the description values
availability = []  # List to store the availability values

count = 0  # Counter variable to keep track of the current field being processed
loopPrint = 0  # Counter variable to keep track of the current index for printing
word = ""  # String variable to build each field value

with open(dataInput) as file:  # Open the data file
    for row in file:  # Iterate over each row in the file
    
        for letter in row:  # Iterate over each letter in the row
        
            if letter != "\t" and letter != "\n":  # Check if the letter is not a tab or newline character
                word = word + letter  # Append the letter to the current field value
                
            else:
                if count == 0:  # Check if it's the category field
                    category.append(word)  # Add the current field value to the category list
                    count = count + 1  # Increment the counter
                    
                elif count == 1:  # Check if it's the name field
                    name.append(word)  # Add the current field value to the name list
                    count = count + 1  # Increment the counter
                    
                elif count == 2:  # Check if it's the description field
                    description.append(word)  # Add the current field value to the description list
                    count = count + 1  # Increment the counter
                    
                else:
                    availability.append(word)  # Add the current field value to the availability list
                    if availability[loopPrint] == "Available":  # Check if the availability is "Available"
                        print(f"{name[loopPrint]} ({category[loopPrint]}) -- {description[loopPrint]}") # Print the desired output with the corresponding values
                        
                    loopPrint = loopPrint + 1  # Increment the printing counter
                    count = 0  # Reset the counter for the next row
                    
                word = ""  # Reset the field value for the next field in the row
