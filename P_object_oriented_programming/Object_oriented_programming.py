# Follows the same concept of other languages like Java and Javascript where objects
# can be created by assigning them attributes and methods that can then be used when programming

from car_example import CarExample

car_1 = CarExample("Boat", "Biff", 2011, "orange")
car_93 = CarExample("Tractor", "Dongus", 2029, "blue")

print(car_1.name)
print(car_1.make)
print(car_1.year)
print(car_1.color)
print()
print(car_93.name)
print(car_93.make)
print(car_93.year)
print(car_93.color)
print()
car_1.drive()
car_1.stop()
