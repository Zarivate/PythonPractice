# sets are also collections but are unordered and don't allow any duplicate values

# Created similarly to other collections, though now use curly braces instead
# can technically put duplicates in sets but won't be registered. Only 1 fork is printed in the loop below.
silverware = {"spoon", "knife", "spork", "fork", "fork", "fork", "fork"}
dishes = {"plate", "bowl", "mug", "pot", "spork"}

# Sets have similar methods to other collections that can be used on it such as
silverware.add("banana")
# silverware.remove("fork")
# silverware.clear()

# Can also join two sets together as one
# dishes.update(silverware)

# Or make a new set with the union of other sets
sets_together = silverware.union(dishes)

# Sets are faster than lists when it comes to checking if something exists within a set
# The loop below doesn't always print the elements in the same order, what prints first is the fastest at that time
for element in silverware:
    print(element)
print("")

for element in sets_together:
    print(element)
print("")

# Can also compare and print out the differences and similarities between sets like so
# Prints out what silverware has that dishes doesn't
print(silverware.difference(dishes))
print("")

# Prints out whatever element they have in common
print(dishes.intersection(silverware))