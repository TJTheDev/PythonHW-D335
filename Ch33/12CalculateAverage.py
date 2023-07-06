"""
Complete the calc_average() function that has an integer list parameter and returns the average value of the elements in the list as a float.

Ex: If the input list is:
1 2 3 4 5

then the returned average will be:
3.0

"""

def calc_average(nums):
    mathUp = 0  # Initialize a variable to hold the sum of the numbers
    divide = 0  # Initialize a variable to count the number of elements in 'nums'
    
    # Iterate over each element in 'nums'
    for _ in nums:
        mathUp = _ + mathUp  # Add the current number to the running sum
        divide = divide + 1  # Increment the count of elements
        
    mathUp = float(mathUp) / float(divide)  # Calculate the average by dividing the sum by the count
    return mathUp  # Return the average


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 33]  # List of numbers to calculate the average
    print(calc_average(nums))  # Print the result of calling the calc_average() function with 'nums'