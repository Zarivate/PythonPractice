# Classes here can also function as blueprints for objects just like in JS and Java
class CarExample:

    # Class variable, will be the same for all instances unless otherwise changed
    wheels = 97

    # Constructor equivalent
    def __init__(self, make, name, year, color):
        self.make = make # Instance variable
        self.name = name # Instance variable
        self.year = year # Instance variable
        self.color = color # Instance variable

    def drive(self):
        print("Vroom Vroom! " + self.name + " is going so fast.")

    def stop(self):
        print(self.name + " is now on standby mode")
