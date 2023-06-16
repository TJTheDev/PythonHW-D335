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

#Employee A: 15.62 miles
employeeA = float(input())
employeeA = employeeA * 15.62

#Employee B: 41.85 miles
employeeB = float(input())
employeeB = employeeB * 41.85

#Employee C: 32.67 miles
employeeC = float(input())
employeeC = employeeC * 32.67

#solution accepts three integer inputs representing the number of times an employee travels to the job site
totalDistance = f"{:.2}".format(employeeA + employeeB + employeeC)

#solution outputs "Distance: " followed by the total value to two decimal places
print("Distance:", totalDistance)
