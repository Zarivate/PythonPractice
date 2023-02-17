# Abstract classes are classes that have one or more abstract methods
# An abstract method is a method that had a declaration but doesn't have an implementation

# These prevent a user from making an object of that class and compels a user to
# override abstract methods in child classes

# abc is short for abstract based class, this is needed for abstract class creation
from abc import ABC, abstractmethod


class Vehicle(ABC):

    # Needed for abstract method declaration
    @abstractmethod
    def go(self):
        pass


class Car(Vehicle):

    # This method is required since Vehicle is abstract, in order to inherit it from it, an
    # implementation is required for the go() method
    def go(self):
        print("Car is being driven")


class Motorcycle(Vehicle):

    # Same idea here
    def go(self):
        print("Motorcycle is being driven")

# Because Vehicle is now an abstract class, can't create an object from it.
# vehicle = Vehicle() returns an error

car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()