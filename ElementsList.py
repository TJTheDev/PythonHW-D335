#TarrylonToneyElementsList
"""

Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.
 
Task:
Create a solution that accepts one integer input representing the index value for any of the string elements in the following list:
frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]
Output the string element of the index value entered. The solution should be placed in a try block and implement an exception of "Error" if an incompatible integer input is provided.
The solution output should be in the format
frameworks_element
 
Sample Input/Output:
If the integer input is
2
then the expected output is
CherryPy
Alternatively, if the integer input is
7
then the expected output is
Error

"""

indexCheck = int(input())
frameworks=["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

if frameworks[indexCheck] > 0 and < 6:
	print(frameworks[indexCheck])
else:
	print(Error)


