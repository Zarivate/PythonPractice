# Classes here can also function as blueprints for objects just like in JS and Java
class CarExample:

    # Constructor equivalent
    
    def __init__(self, make, name, year, color):
        self.make = make
        self.name = name
        self.year = year
        self.color = color

    def drive(self):
        print("Vroom Vroom! " + self.name + " is going so fast.")

    def stop(self):
        print(self.name + " is now on standby mode")
