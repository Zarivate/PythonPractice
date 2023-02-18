# Walrus operator is ":=", it's an assignment expression that assigns values to variables as
# part of a larger expression

# Can turn these two lines into one
# melancholic = True
# print(melancholic)

print(melancholic := True)

# More practical example would be for a while loop situation

foods = list()

# while True:
#     food = input("What are your favorite foods? Type (quit) once you are done listing things off: ")
#     if food == "quit":
#             break
#     foods.append(food)

# Above code now becomes this
while food := input("What are your favorite foods? Type (quit) once you are done listing things off: ") != "quit":
    foods.append(food)