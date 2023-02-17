# Concept that a child class can be derived from more than one parent class

class Prey:

    def flee(self):
        print("This animal is running away")


class Predator:

    def hunt(self):
        print("This animel is on the hunt")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


# Multiple Inheritance, since fish can be both predator and prey depending on the size of the fish
class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
print()
fish.hunt(), fish.flee()


