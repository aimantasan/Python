class Car:
    color:None

class Motorcycle:
    color:None

def change_color(vehicle,color): # The name for the object doesnt need to be same with the class name
    vehicle.color = color # Pass the variable from said class to class attributes


car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

#print(car_1.color) # Should be none as the default value is still unassigned

change_color(car_1,"Red") # Pass object (Car class) and value (Color)
change_color(car_2,"White")
change_color(car_3,"Blue")
change_color(bike_1,"Black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)