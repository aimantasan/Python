# multiple inheritence = when a child class is deriverd from more than one parent class

class Prey:             # This is a parent class
    def flee(self):
        print("This animal flee")

class Predator:         # This is a parent class
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish (Prey,Predator):
    pass

# Defineing variables for class
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()   # Only inherits from Prey Class
hawk.hunt()     # Only inherits from Predator Class

fish.hunt()     # Inherits from both Predator and Prey Class
fish.flee()