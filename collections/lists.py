# Lists are used similarly as in other languages, where they can store multiple variables instead of just a single one
# can be seen as a variable that stores multiple elements/items

# Difference between a variable and a list
food = "pizza"
foods = ["pizza", "hamburger", "tamale", "mango", "mole", "rice"]

# They can be updated the same as in other languages too
foods[0] = "hotdog"
# Adds ice cream to end of list
foods.append("ice cream")
foods.remove("rice")
# Removes last element from list, in this case "ice cream"
foods.pop()
foods.insert(0, "cake")
foods.sort()
foods.clear()

for element in foods:
    print(element)