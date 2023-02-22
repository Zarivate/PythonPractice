# list comprehension is a way to create a new list with less syntax, they can also be used too
# mimic certain lambda functions like the map() and filter() functions but be easier to read
# There are formulas meant to be followed however, the first 1 being

# list = [expression for item in iterable] like so

# 2nd possible way would be like so
# list = [expression for item in iterable if conditional]

# Final 3rd way would be like so
# list = [expression (if/else) for item in iterable]

# Normal way
squares = []
for i in range(1, 11):
    squares.append(i * i)
print(squares)

# Becomes like this
squares2 = [i * i for i in range(1, 11)]
print(squares2)

# Filter like example
student_grades = [100, 90, 80, 70, 63, 60, 50, 40, 30, 22, 0]
# Normal way of filtering
passed_students = list(filter(lambda x: x >= 60, student_grades))
print(passed_students)
# Big bois way of doing it, 2nd way to be more exact
passed_students2 = [i for i in student_grades if i >= 60]
print(passed_students2)

# 3rd way of doing it,
passed_students3 = [i if i >= 60 else "This student failed" for i in student_grades]
print(passed_students3)
