# Duck typing is the idea that the methods and variables of a class are more important than
# the class of the object. The class type isn't checked if the minimum methods/attributes exist
# Comes from famous saying, "If it walks like a duck, talks like a duck, then it's a duck"

class Duck:

    def walk(self):
        print("Walking walk, duck is walking")


    def talk(self):
        print("Quack quack")

class Turtle:

    def walk(self):
        print("Turtle is walking, slowly of course")

    def talk(self):
        print("I don't know what sounds turtles make but it's making a sound")


class Human:

    # Object sent in doesn't have to be of the same class, just has to have a walk() and talk() method
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("The animal is caught!")

duck = Duck()
turtle = Turtle()
person = Human()

person.catch(duck)
# Because the turtle class has the required methods to be passed into Human's catch method,
# It doesn't matter if it's not actually a duck object.
person.catch(turtle)