# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self # When doing method chaining, return is needed
    
    def drive(self):
        print("You drive the car")
        return self   

    def brake(self):
        print("You step on the brake")
        return self

    def turn_off(self):
        print ("You turn off the engine")
        return self

car = Car()

# Calling Method Chaining
car.turn_on().drive()

# After the function is finished, it will return the class.
car.brake().turn_off()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
# Python will read the code from left or right, so the position is important
# \ is for Continuation