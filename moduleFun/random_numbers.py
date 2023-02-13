# random numbers, or in this case, pseudo random numbers and neat tricks you can do with them
import random

x = random.randint(1,7)
a_float = random.random()

myList = ['mangos', 'strawberrys', 'pears', 'apples', 'cyanide']
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9, 'A', "Z", "V", "L", "S"]

random.shuffle(cards)

print(x)
print(a_float)
print(z)
print(cards)