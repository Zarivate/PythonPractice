# Sort technically has two variations, the sort() method and the sort() function
# The method is used for lists while the function is used for iterables, does the same
# thing as it would in other languages. Where it sorts a series of data in a variety of ways

example = ["Bort", "Biff", "Wilburt", "Emily", "Dirkle"]

# Sorts alphabetically
example.sort()

for i in example:
    print(i)

print()

# Can also sort in reverse alphabetically order depending on what you put in the sort(field)
example.sort(reverse=True)
for i in example:
    print(i)

# Can't use the sort method on tuples, the sort function can be used however and returns a sorted list
example2 = ("Bort", "Biff", "Wilburt", "Emily", "Dirkle")

sorted_tuple = sorted(example2)