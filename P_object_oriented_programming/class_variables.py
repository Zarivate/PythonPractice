# Class variables and instance variables exist in much the same way as they do in other languages
# where the class variables reside outside constructors and set to a default value for each instance
# while instance variables reside within the constructor and are usually unique

from car_example import CarExample

car_1 = CarExample("Boat", "Biff", 2011, "orange")
car_93 = CarExample("Tractor", "Dongus", 2029, "blue")

# Wheels will be the same
print(car_1.wheels)
print(str(car_93.wheels) + "\n")

car_1.wheels = 7

# Wheels for first car will be different
print(car_1.wheels)
print(str(car_93.wheels) + " \n")

CarExample.wheels = 4

# Wheels will change for car_93 but not car_1 as that has already been changed separately
print(car_1.wheels)
print(str(car_93.wheels) + "\n")