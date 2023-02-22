# zip(*iterables) takes elements from two or more iterable objects (list, tuples, sets, etc), aggregates their
# elements and creates a zip object with paired elements stored in tuples for each element

# The two iterables
usernames = ["Biff", "Bort", "Dij"]
passwords = ("12346@3", "fri3dshrimprice", "zoow33m4ma")

# Type cast zip object into a dictionary, so they are paired as kye value pairs
users = dict(zip(usernames, passwords))

# Turns out it hold a dictionary because we type-casted it above as a dictionary
print(type(users))

# Since it's a dictionary we use .items() to access the objects
for key, value in users.items():
    print(key + " : " + value)
print()
# Can zip up more than just 2 iterable objects like so
last_login = ["3/9/1991", "1/5/2091", "7/7/1777"]

new_users = zip(usernames, passwords, last_login)

# Prints out a tuple of each element with 3 elements each now
for i in new_users:
    print(i)

