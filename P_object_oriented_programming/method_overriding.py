# Method overriding is the same concept found in other programming languages where a class
# that inherits from a parent class can have the same method as it's parent but have it more
# closely related to the child. Don't have to write "override" above overwritten method however
# like you would in Java

class Animal:
    def eat(self):
        print("This animal is eating")

class Rabbit:
    def eat(self):
        print("The rabbit is eating a carrot, om nom nom")


rabbit = Rabbit()
# Will use its own method before resorting to it's parent's method
rabbit.eat()