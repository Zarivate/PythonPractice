# Same concept as in other programming languages, that parent classes can have their children
# inherit attributes and methods, among other things, from them

class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


# Inheritance example
class Rabbit(Animal):

    # Unique method only to the class
    def run(self):
        print("The rabbit is running")


class Turle(Animal):

    def cute(self):
        print("The turtle is being cute")


class Wombat(Animal):

    def chonky(self):
        print("The wombat is being chonky")


rabbit = Rabbit()
turtle = Turle()
wombat = Wombat()

# Despite not having it directly in its class code, it still retains access to methods in Animal
print(rabbit.alive)
turtle.eat()
wombat.sleep()
print()

rabbit.run()
turtle.cute()
wombat.chonky()