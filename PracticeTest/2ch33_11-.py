"""
The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which has an index n as parameter and returns the nth value in the sequence. Any negative index values should return -1.

Ex: If the input is:

7
the output is:

fibonacci(7) is 13
Note: Use a for loop and DO NOT use recursion.
"""

def fibonacci(n):
    if n < 0:
        return -1
    
    x = 0
    y = 1
    for _ in range (n):
        # Assign the value of 'y' to 'x' and the sum of 'x' and 'y' to 'y'
        temp = x + y
        x = y
        y = temp
    return x


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')

"""
Complete the calc_average() function that has an integer list parameter and returns the average value of the elements in the list as a float.

Ex: If the input list is:

1 2 3 4 5
then the returned average will be:

3.0
"""

def calc_average(nums):
    mathUp = 0
    divide = 0
    for _ in nums:
        mathUp = _ + mathUp
        divide = divide + 1
    mathUp = float(mathUp) / float(divide)
    return mathUp
    
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(calc_average(nums))   # calc_average() should return 3.0

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
    num_count = 0
    for _ in input_str:
        num_count = num_count + 1
    return num_count

def output_without_whitespace(input_str):
    output = ""
    for _ in input_str:
        if _ != " " and _ != "\t":
            output = output + _
    return output


if __name__ == '__main__':
    strIn = str(input("Enter a sentence or phrase:\n\n"))
    
    print(f"You entered:", strIn + "\n")

    print(f"Number of characters:", get_num_of_characters(strIn))
    print(f"String with no whitespace:", output_without_whitespace(strIn))
