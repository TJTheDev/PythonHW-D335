"""
The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which has an index n as parameter and returns the nth value in the sequence. Any negative index values should return -1.

Ex: If the input is:
7

the output is:
fibonacci(7) is 13

"""

def fibonacci(n):
    if n < 0: # Checks if the input number is negative
        return -1  # Fibonacci series is not defined for negative numbers
    
    x = 0  # Initialize the first number of the Fibonacci sequence
    y = 1  # Initialize the second number of the Fibonacci sequence

    for _ in range(n): # Iterate 'n' times to generate the nth Fibonacci number

        temp = x + y  # Calculate the next number in the Fibonacci sequence
        x = y  # Update 'x' to the previous value of 'y'
        y = temp  # Update 'y' to the calculated value
        
    return x  # Return the final number in the Fibonacci sequence


if __name__ == '__main__':
    start_num = int(input())  # Prompt the user to enter a starting number for the Fibonacci sequence
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')  # Print the result of the Fibonacci sequence with the input number as an argument