"""
(1) Prompt the user to enter a string of their choosing. Output the string. (1 pt)

Ex:
Enter a sentence or phrase:
The only thing we have to fear is fear itself.

You entered: The only thing we have to fear is fear itself.

(2) Complete the get_num_of_characters() function, which returns the number of characters in the user's string. We encourage you to use a for loop in this function. (2 pts)

(3) Extend the program by calling the get_num_of_characters() function and then output the returned result. (1 pt)

(4) Extend the program further by implementing the output_without_whitespace() function. output_without_whitespace() outputs the string's characters except for whitespace (spaces, tabs). Note: A tab is '\t'. Call the output_without_whitespace() function in main(). (2 pts)

Ex:
Enter a sentence or phrase: 
The only thing we have to fear is fear itself.

You entered: The only thing we have to fear is fear itself.

Number of characters: 46
String with no whitespace: Theonlythingwehavetofearisfearitself.

"""

def get_num_of_characters(input_str):
    num_count = 0  # Initialize a variable to count the number of characters
    for _ in input_str:
        num_count = num_count + 1  # Increment the count for each character in the input string
    return num_count  # Return the total count of characters


def output_without_whitespace(input_str):
    output = ""  # Initialize an empty string to store the output without whitespace
    for _ in input_str:
        if _ != " " and _ != "\t":  # Check if the character is not a space or tab
            output = output + _  # Add the character to the output string
    return output  # Return the resulting output without whitespace


if __name__ == '__main__':
    strIn = str(input("Enter a sentence or phrase:\n\n"))  # Prompt the user to enter a sentence or phrase
    
    print(f"You entered:", strIn + "\n")  # Print the original input sentence or phrase
