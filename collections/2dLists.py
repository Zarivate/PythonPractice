# 2D lists are just a list of lists/multidimensional lists

drinks = ["water", "soda", "juice", "coffee"]
meals = ["mole", "elote", "borger", "pizza"]
dessert = ["ice cream", "cookies"]

# Like so
foods = [drinks, meals, dessert]

# If you want to only access one of the lists, then have to specify like normal. Below would only print the first list
print(foods[0])

# If you want a specific item from a certain lists, need to specify two points like so. Prints cookies
print(foods[2][1])
