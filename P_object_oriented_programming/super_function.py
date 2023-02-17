# super() is a function that can be used to give access to the methods of a parent class
# a temporary object of a parent class is returned from it

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):

    def __init__(self, length, width):
        # Super class is called in order to not repeat code
        super().__init__(length, width)

    def area(self):
        return self.length*self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        # Same idea here
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())
