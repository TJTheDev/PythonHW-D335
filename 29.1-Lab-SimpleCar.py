"""
Given two integers that represent the miles to drive forward and the miles to drive in reverse as user inputs, create a SimpleCar object that performs the following operations:

Drives input number of miles forward
Drives input number of miles in reverse
Honks the horn
Reports car status

Ex: If the input is:
100
4

the output is:
beep beep
Car has driven: 96 miles
"""

class SimpleCar:
    def __init__(self):
        self.miles = 0

    def drive(self, dist):
        self.miles = self.miles + dist
        
    def reverse(self, dist):
        self.miles = self.miles - dist
        
    def get_odometer(self):
        return self.miles
    
    def honk_horn(self):
        print('beep beep')
        
    def report(self):
        print(f'Car has driven: {self.miles} miles')
        
if __name__ == "__main__":
    
    # Taking user inputs for miles to drive forward and in reverse
    driveIn = int(input())
    reverseIn = int(input())
    
    car = SimpleCar() # Creating the SimpleCar object

    # Driving the car forward and in reverse
    car.drive(driveIn)
    car.reverse(reverseIn)

    car.honk_horn() # Honking the horn

    car.report() # Reporting car status
