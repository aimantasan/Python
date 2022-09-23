# abstract class / ghost class = a class which contains one or more abstract methods
# abstract methods = a method that has a declaration but does not have an implementation

from abc import ABC,abstractmethod # Prevent someone from accessing or modify from this class

class Vehicle(ABC): # The vehicle class inherits form Abstract Based Class
    @abstractmethod #Prevents from creating a new object
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print ("You drive the car")

    def stop(self): # Override method from Vehicle Class
        print("This car has stopped")

class Motorcycle(Vehicle):
    def go(self):
        print ("You ride the motorcycle")

    def stop(self): # Override method from Vehicle Class
        print("This motorcycle has stopped")

# vehicle = Vehicle() # If this is called, Type Error will be executed 
car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go() 

car.stop() # Overriding could prevent Abstract Method
motorcycle.stop()

# Abstract Class compels any user to override any abstract method within a child class
# 
# class Motorcycle(Vehicle):
#    pass

# Error will be given on this case (Cant instantiate abstract vehicle with abstract methods go)
# Make sure that the children clas are not missing any kind of implementation that they inherit
