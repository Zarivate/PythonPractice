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

print()

# Can't use the sort method on tuples, the sort function can be used however and returns a sorted list
example2 = ("Bort", "Biff", "Wilburt", "Emily", "Dirkle")

sorted_tuple = sorted(example2)
# Can be reversed as well just like its method counterpart
sorted_tuple2 = sorted(example2, reverse=True)

for i in sorted_tuple:
    print(i)

print()

for i in sorted_tuple2:
    print(i)
print()


# List of tuples examples
students = [("Bort", "C", 73),
            ("Biff", "F", 60),
            ("Dongus", "D", 69),
            ("Quandale", "A", 91),
            ("Dirkle", "B", 73),]

# Can still sort lists of tuples in alphabetical order
students.sort()

for i in students:
    print(i)
print()

# If you want to sort by second or third variable in the tuples, will need to use the key
# second argument alongside a lambda function

grade = lambda grades:grades[1]
# A grade below is a function object, can also still use the "reverse=True" keyword in the second parameter
# if you want things sorted in reverse
students.sort(key=grade)

for i in students:
    print(i)
print()
# Tuple of tuples example, can no longer use sort() method
students2 = (("Bort", "C", 73),
            ("Biff", "F", 60),
            ("Dongus", "D", 69),
            ("Quandale", "A", 91),
            ("Dirkle", "B", 73))

test_score = lambda last_test_score:last_test_score[2]
sorted_students = sorted(students2, key=test_score, reverse=True)

for i in sorted_students:
    print(i)