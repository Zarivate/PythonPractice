# tuples are similar to lists, they're collections that are ordered and are unchangeable,
# they're used to group together related data

# Tuples are created similarly to lists but use parentheses instead of brackets

# Tuple with student information
student = ("Bort", 97, "female")

# Has various methods that can be used on it, not all but couple useful ones are

# How many times an element appears in the tuple
print(student.count("Bort"))

# Returns the index of the element you're looking for, if it exists that is
print(student.index("female"))

# Can still print out all the contents with a for loop like can with other data structures
for element in student:
    print(element)

# Can also do if statement to check if an element exists within the tuple
if "female" in student:
    print("The student is female")