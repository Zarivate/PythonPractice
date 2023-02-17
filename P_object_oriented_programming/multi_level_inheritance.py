# Multi-level inheritance is when a child class inherits from another derived child class

class Being:
    alive = True


# Normal level inheritance
class Animal(Being):

    def eat(self):
        print("This animal is eating")


# Multi-level inheritance
class Turtle(Animal):

    def protect(self):
        print("The turtle has resided back into it's shell")


# The created Turtle object still has access to the alive attribute within the Being class
# alongside access to the eat method of Animal
turtle = Turtle()
print(turtle.alive)
turtle.eat()
turtle.protect()