"""
Write a program to calculate the total price for car wash services. A base car wash is $10. A dictionary with each additional service and the corresponding cost has been provided. Two additional services can be selected. A '-' signifies an additional service was not selected. Output all selected services, according to the input order, along with the corresponding costs and then the total price for all car wash services.

Ex: If the input is:
Tire shine
Wax

the output is:
ZyCar Wash
Base car wash -- $10
Tire shine -- $2
Wax -- $3
----
Total price: $15

Ex: If the input is:
Rain repellent
-

the output is:
ZyCar Wash
Base car wash -- $10
Rain repellent -- $2
----
Total price: $12

"""

services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = 0

service_choice1 = input()    # Prompt the user to enter the first service choice
service_choice2 = input()    # Prompt the user to enter the second service choice

print("ZyCar Wash")
print("Base car wash -- $10")
total = base_wash    # Set the initial total to the base wash price

if service_choice1 != "-":
    print(f"{service_choice1} -- ${services[service_choice1]}")    # Print the first service choice and its corresponding price
    total = total + services[service_choice1]    # Add the price of the first service to the total

if service_choice2 != "-":
    print(f"{service_choice2} -- ${services[service_choice2]}")    # Print the second service choice and its corresponding price
    total = total + services[service_choice2]    # Add the price of the second service to the total

print("----")
print(f"Total price: $" + str(total))    # Print the total price of the car wash service
