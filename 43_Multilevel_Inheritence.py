# multi-level inheritence = when a derived (child) class inherits another derived (child) class
# Grandparent -> Parent -> Child

class Organism:             # Parent Class
    alive = True

class Animals(Organism):    # First Child class
    
    def eat(self):
        print("This animal is eating")

class Dog(Animals):
    
    def bark(self):
        print("This dog is barking")


dog  = Dog()    # Define variable from class

print(dog.alive)    # Inherit from Grandparent
dog.eat()           # Inherit from Parent
dog.bark()          # Call for self function