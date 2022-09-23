# super() = Function used to give access to the methods of a parent class
#           Return a temporary object of a parent class when used

class Rectangle:
    def __init__(self,length,width):        # Define once at the parent class
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)      # Reuse the function by using the super() 
    
    def area(self):
        return self.length*self.width       # Will fetch the self value


class Cube(Square):

    def __init__(self, length, width,height):   
        super().__init__(length,width)      # Reuse the function by using the super()
        self.height = height
    
    def volume(self):
        return self.length*self.width*self.height   

square = Square(3,3)
print(square.area())

cube = Cube(3,3,3)
print(cube.volume())

