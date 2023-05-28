#TarrylonToneySumOf5
"""
Create a solution that accepts five integer inputs. Output the sum of the five inputs three times, 
converting the inputs to the requested data type prior to finding the sum.

First output: sum of five inputs maintained as integer values
Second output: sum of five inputs converted to float values
Third output: sum of five inputs converted to string values (concatenate)
The solution output should be in the format

Integer: integer_sum_value
Float: float_sum_value
String: string_sum_value
Sample Input/Output:
If the input is

1
3
6
2
7
then the expected output is

Integer: 19
Float: 19.0
String: 13627
"""

#solution accepts five integer inputs
val1 = int(input())
val2 = int(input())
val3 = int(input())
val4 = int(input())
val5 = int(input())

#solution outputs three sums of input values; convert before calculating sum
#first output: sum of five inputs maintained as integer values
sum1 = val1 + val2 + val3 + val4 + val5
print("Integer:", sum1)

#second output: sum of five inputs converted to float values
sum2 = float(val1) + float(val2) + float(val3) + float(val4) + float(val5)
print("Float:", sum2)

#third output: sum of five inputs converted to string values (concatenate)
sumString = str(val1) + str(val2) + str(val3) + str(val4) + str(val5)
print("String:", sumString)