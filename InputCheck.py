#TarrylonToneyInputChecker
"""
Create a solution that accepts an integer input representing the index value for any any of the five elements in the following list:

various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

Using the built-in function type() and getting its name by using the .name attribute, output data type (e.g., int”, “float”, “bool”, “str”) based on the input index value of the list element.

The solution output should be in the format

Element index_value: data_type
Sample Input/Output:
If the input is
4

then the expected output is
Element 4: tuple

"""

various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

#use built-in function type()
#solution accepts integer input representing list element index
userIn = int(input())

#get name by using the built-in attribute __name__ I don't understand how this works
#index = various_data_types.index(userIn)
#print(type(various_data_types[userIn]))
#solution outputs data type of list element based on input index value

#print("Element", various_data_types[4])
#if userIn in various_data_types:
#    print ("Element")
#indexList = various_data_types.index(userIn)

stringCut = type(various_data_types[userIn])
#Sliced the string from position 0-8 at the beginning and slices the last two characters from the end
stringCut = str(stringCut)[8:-2]
print("Element", str(userIn) + ":", stringCut)