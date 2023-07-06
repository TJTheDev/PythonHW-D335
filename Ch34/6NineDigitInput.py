#TarrylonToney9-DigitInput
"""
Create a solution that accepts an integer input representing a 9-digit unformatted student identification number. Output the identification number as a string with no spaces.

The solution output should be in the format

111-22-3333
Sample Input/Output:
If the input is

154175430
then the expected output is

154-17-5430

"""

#hint: modulo (%) and floored division (//) may be used
#solution accepts a 9-digit integer representing an unformatted student identification number (i.e.,"5417543010")
studentNum = int(input())

#solution outputs formatted student identification number as a string (i.e.,"541-75-3010")
#Converted the integer input into a string
studentNum = str(studentNum)

#Used the slicing function to break apart the string while concatenating the '-' digit break
studentNumOut = (studentNum[0:3] + "-" + studentNum[3:5] + "-" + studentNum[5:9])
print(studentNumOut)
