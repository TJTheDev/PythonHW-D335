"""
A pedometer treats walking 2,000 steps as walking 1 mile. Write a steps_to_miles() function that takes the number of steps as a parameter and returns the miles walked. The steps_to_miles() function throws a ValueError object with the message "Exception: Negative step count entered." when the number of steps is negative. Complete the main() program that reads the number of steps from a user, calls the steps_to_miles() function, and outputs the returned value from the steps_to_miles() function. Use a try-except block to catch any ValueError object thrown by the steps_to_miles() function and output the exception message.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

Ex: If the input of the program is:
5345

the output of the program is:
2.67

Ex: If the input of the program is:
-3850

the output of the program is:
Exception: Negative step count entered.

"""

def steps_to_miles(stepCov):
    if stepCov < 0:
        raise ValueError("Exception: Negative step count entered.")    # Raise a value error if stepCov is negative
    return (stepCov / 2000)    # Convert stepCov to miles by dividing it by 2000

if __name__ == '__main__':
    stepCount = int(input())    # Prompt the user to enter the step count
    
    try:
        miles_walked = steps_to_miles(stepCount)    # Convert the step count to miles using the steps_to_miles function
    except ValueError:
        print('Exception: Negative step count entered.')    # Handle the value error exception and print an error message
        
    print(f"{steps_to_miles(stepCount):.2f}")    # Print the miles walked with two decimal places