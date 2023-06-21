#TarrylonToneyDistanceTracker
"""
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.
Create a solution that accepts three integer inputs representing the number of times an employee travels to a job site. 
Output the total distance traveled to two decimal places given the following miles per employee commute to the job site. 
Output the total distance traveled to two decimal places given the following miles per employee commute to the job site:

Employee A: 15.62 miles
Employee B: 41.85 miles
Employee C: 32.67 miles
The solution output should be in the format.
Distance: total_miles_traveled

Sample Input/Output:

If the input is
1
2
3
then the expected output is

Distance: 197.33 miles
"""

# Get input values for employeeA, employeeB, and employeeC
employeeA = float(input())
employeeB = float(input())
employeeC = float(input())

# Calculate the distance for each employee
employeeA = (employeeA * 15.62)
employeeB = (employeeB * 41.85)
employeeC = (employeeC * 32.67)

# Calculate the total distance
distance = "{:.2f}".format(employeeA + employeeB + employeeC)

# Prints the distance
print("Distance: " + distance, "miles")
