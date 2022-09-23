class Car:
    
    wheels = 4 # Class variable example (Defined outside of the Constructor)

    def __init__(self,make,model,year,color): # Constructor for Class
        # Self are defined as the object itself
        self.make = make        # instance variable (Defined inside the constructor)
        self.model = model      # instance variable (Defined inside the constructor)
        self.year = year        # instance variable (Defined inside the constructor)
        self.color = color      # instance variable (Defined inside the constructor)

    def drive(self):
        print("This " + self.model +" is driving")
    
    def stop(self):
        print("This " + self.model +" is stopped")
