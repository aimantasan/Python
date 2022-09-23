# Inheritance: To receive, derive or left with
# Class could inherit attributes or method from another class (Parent - Child relationship)

class Animal: # This is Parent Class that define the Animal

    alive = True

    def eat(self):
        print("This animal is eating")
    
    def sleep(self):
        print("This animal is sleeping")


class Rabbit(Animal): # This is Child Class that will derive attributes from the Parent Class # format : class Name(Parent)
    def run(self):
        print("This rabbit is running")

class Fish(Animal): # This is Child Class that will derive attributes from the Parent Class # format : class Name(Parent)
    def swim(self):
        print("This fish is swimning")

class Hawk(Animal): # This is Child Class that will derive attributes from the Parent Class # format : class Name(Parent)
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive) # Attributes could be found as it was inherited from the parent (Animal)
fish.eat()
hawk.sleep()

# Try to call their own attributes from Child Class
rabbit.run()
fish.swim()
hawk.fly()