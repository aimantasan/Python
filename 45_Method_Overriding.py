# method overriding = an ability of OOP to allow a child class to provide a specific implementation by one of its parent

class Animals:   # Parent Class
    
    def eat(self):
        print("This animal is eating")

class Rabbit(Animals):  # Child Class
    
     def eat(self):
        print("This rabbit is eating a carrot") # To override, the name must be same from the other targeted class



# Define variable for class
rabbit = Rabbit()

rabbit.eat() # Output will be called from the Rabbit Class of eat function
             # Initially the value is "This animal is eating" but being overrided
