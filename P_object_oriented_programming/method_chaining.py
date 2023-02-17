# method chaining is when multiple methods are called sequentially, where each call performs
# an action on the same abject and returns self. Because self is returned in the methods,
# a following method can be called right away.

class Car:

    def on(self):
        print("Engine has been started")
        return self

    def drive(self):
        print("The car is being driven")
        return self

    def brake(self):
        print("Brakes have been activated")
        return self

    def off(self):
        print("Car has been turned off")
        return self

car = Car()

# Method chaining, not necessary but can be placed on separate lines. The \ inserted is a line continuation character
car.on().\
    drive().\
    brake().\
    off()