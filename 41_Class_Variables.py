from car import Car

car_1 = Car("Chevy","Corvette","2021","blue")
car_2 = Car("Ford","Mustang","2022","red")

car_1.wheels = 2

print(car_1.wheels)  # Output will be 2 as the value is modified
print(car_2.wheels)  # It will stay at 4 because thats the default value

print(Car.wheels)    # Calling the class variables dirctly from the class.variables

Car.wheels = 2       # Modifying the class variables value directly at other modules
print(Car.wheels)    # Calling the class variables dirctly from the class.variables